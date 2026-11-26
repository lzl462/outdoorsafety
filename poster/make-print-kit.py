#!/usr/bin/env python3
"""Assemble vector card artwork into measured Legal sheets and board previews."""
from pathlib import Path
import argparse
import json
import pymupdf as pdf

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--monochrome", action="store_true", help="Build the black & white variant.")
options = parser.parse_args()
HERE = Path(__file__).resolve().parent
SCRATCH = HERE / ".render"
ART = SCRATCH / "monochrome" if options.monochrome else SCRATCH
SUFFIX = "-bw" if options.monochrome else ""
INK = (0, 0, 0) if options.monochrome else (.09, .24, .20)
ROOT = HERE.parent
PT = 72 / 25.4
layout = json.loads((SCRATCH / "layout.json").read_text())
board, paper, cards = layout["board"], layout["paper"], layout["cards"]
mm = lambda value: value * PT


def save(doc, name, title):
    if options.monochrome:
        title += " — Black & white"
    doc.set_metadata({"title": title, "author": "Liz", "subject": "Outdoor Safety — Sea-to-Sky"})
    doc.subset_fonts()
    output = Path(name)
    doc.save(HERE / (output.stem + SUFFIX + output.suffix), garbage=4, deflate=True)


def text(page, position, wording, size=9, color=None, bold=False):
    page.insert_font(fontname="body", fontfile=str(ROOT / "fonts/dm-sans-400.ttf"))
    page.insert_font(fontname="bold", fontfile=str(ROOT / "fonts/dm-sans-700.ttf"))
    page.insert_text(position, wording, fontsize=size, fontname="bold" if bold else "body", color=INK if color is None else color)


master = pdf.open()
board_page = master.new_page(width=mm(board["widthMm"]), height=mm(board["heightMm"]))
kit = pdf.open()
paper_w, paper_h, margin = mm(paper["widthMm"]), mm(paper["heightMm"]), mm(paper["marginMm"])
trim = pdf.Rect(margin, margin, paper_w - margin, paper_h - margin)
checks = []
for card in cards:
    source = pdf.open(ART / (card["id"] + ".pdf"))
    assert len(source) == 1
    expected = (mm(card["widthMm"]), mm(card["heightMm"]))
    assert abs(source[0].rect.width - expected[0]) < .1
    assert abs(source[0].rect.height - expected[1]) < .1
    page = kit.new_page(width=paper_w, height=paper_h)
    # Every PDF sheet is portrait Legal; landscape cards turn after cutting.
    page.show_pdf_page(trim, source, 0, rotate=0 if card["portrait"] else 90)
    turn = "Portrait" if card["portrait"] else "Landscape · Turn this card after trimming"
    title = f'{card["number"]:02d} · {card["label"]} · {turn}'
    if options.monochrome:
        title += " · Black & white"
    text(page, (margin, 28), title, size=7.5, bold=True)
    for x in (trim.x0, trim.x1):
        direction = -1 if x == trim.x0 else 1
        for y in (trim.y0, trim.y1):
            vertical = -1 if y == trim.y0 else 1
            page.draw_line((x + direction * 4, y), (x + direction * 12, y), width=.55)
            page.draw_line((x, y + vertical * 4), (x, y + vertical * 12), width=.55)
    ruler_y = paper_h - 25
    ruler_x = margin + 18
    page.draw_line((ruler_x, ruler_y), (ruler_x + mm(100), ruler_y), width=.5)
    for x in (ruler_x, ruler_x + mm(100)):
        page.draw_line((x, ruler_y - 3), (x, ruler_y + 3), width=.5)
    text(page, (ruler_x + mm(100) + 5, ruler_y + 2.5), "100 mm · Actual size / 100%", size=7)
    rect = pdf.Rect(mm(card["xMm"]), mm(card["yMm"]),
                    mm(card["xMm"] + card["widthMm"]), mm(card["yMm"] + card["heightMm"]))
    board_page.show_pdf_page(rect, source, 0)
    checks.append({"number": card["number"], "id": card["id"], "printPagePoints": [paper_w, paper_h],
                   "trimSizeMm": [card["widthMm"], card["heightMm"]],
                   "positionMm": [card["xMm"], card["yMm"]]})
    source.close()

save(kit, "trifold-legal.pdf", "Outdoor Safety — twelve Legal print cards")
save(master, "trifold-full-size.pdf", "Outdoor Safety — full-size trifold layout")

# A review PDF and PNG show the composition; the twelve-page kit is for printing.
preview = pdf.open()
page = preview.new_page(width=mm(420), height=mm(297))
page.show_pdf_page(pdf.Rect(mm(12), mm(10), mm(408), mm(280)), master, 0)
text(page, (mm(12), mm(290)), "A3 review preview — not a full-size print file. Use the twelve-page Legal print set.", size=9)
save(preview, "display-preview.pdf", "Outdoor Safety — scaled trifold review preview")
board_page.get_pixmap(dpi=100).save(HERE / ("display-preview" + SUFFIX + ".png"))

# One Legal sheet is the practical cutting and placement guide.
guide = pdf.open()
page = guide.new_page(width=paper_w, height=paper_h)
text(page, (margin, 49), "ASSEMBLY GUIDE", size=21, bold=True)
subtitle = "Outdoor Safety — Sea-to-Sky · Twelve Legal sheets"
if options.monochrome:
    subtitle = "Outdoor Safety — Sea-to-Sky · Black & white · Twelve Legal sheets"
text(page, (margin, 67), subtitle, size=10)
text(page, (margin, 83), "Four portrait and eight landscape cards · Based on the supplied measurements", size=8.5)
map_box = pdf.Rect(margin, 113, paper_w - margin, 113 + (paper_w - 2 * margin) * board["heightMm"] / board["widthMm"])
page.show_pdf_page(map_box, master, 0)
page.draw_rect(map_box, color=(.55, .55, .55) if options.monochrome else (.55, .62, .55), width=.7)
scale = map_box.width / board["widthMm"]
for fold in (board["leftMm"], board["leftMm"] + board["centreMm"]):
    x = map_box.x0 + fold * scale
    page.draw_line((x, map_box.y0), (x, map_box.y1), color=(.45, .45, .45) if options.monochrome else (.45, .52, .45), width=.6, dashes="[3 3]")
for c in cards:
    x = map_box.x0 + c["xMm"] * scale + 3
    y = map_box.y0 + c["yMm"] * scale + 3
    badge = pdf.Rect(x, y, x + 18, y + 14)
    page.draw_rect(badge, fill=(1, 1, 1), color=INK if options.monochrome else (.1, .25, .2), width=.5)
    text(page, (x + 3, y + 10), str(c["number"]), size=8, bold=True)
text(page, (margin, 101), f'Panels: {board["leftMm"]/10:.2f} / {board["centreMm"]/10:.2f} / {board["rightMm"]/10:.2f} cm', size=9)
y = map_box.y1 + 17
text(page, (margin, y), f'Open board: {board["widthMm"]/10:.2f} × {board["heightMm"]/10:.2f} cm. Right panel assumed equal to left.', size=8.5)
y += 15
text(page, (margin, y), "Positions from the upper-left corner of the open, flat board; measurements in cm.", size=8.5)
y += 19
columns = [margin, margin + 28, margin + 226, margin + 300, margin + 364, margin + 430]
for x, word in zip(columns, ["Card", "Content", "Panel", "Left", "Top", "Trim size"]):
    text(page, (x, y), word, size=8.5, bold=True)
for c in cards:
    y += 13
    values = [f'{c["number"]:02d}', c["label"], c["panel"].title(),
              f'{c["xMm"]/10:.2f}', f'{c["yMm"]/10:.2f}',
              f'{c["widthMm"]/10:.2f} × {c["heightMm"]/10:.2f}']
    for x, word in zip(columns, values):
        text(page, (x, y), word, size=8)
y += 22
instructions = [
    "Legal 8.5 × 14 in · Actual size / 100% · Single-sided · One page per sheet.",
    "All PDF sheets are portrait. Turn the eight landscape cards after trimming.",
    "Write each card's number on its back before trimming.",
    "Cut on the marks. Keep QR white borders. Place by card number.",
    "Do not use Fit, Poster or Booklet for the twelve-page print set.",
    "Confirm paper at school: Letter 8.5 × 11 in is shorter. Printing/mounting remain to be done.",
]
for line in instructions:
    text(page, (margin, y), line, size=8.1)
    y += 13
assert y < paper_h - 20, "Assembly guide exceeds one page"
save(guide, "trifold-assembly.pdf", "Outdoor Safety — Legal printing and assembly guide")

(ART / "print-checks.json").write_text(json.dumps({"cards": checks, "guidePages": len(guide), "monochrome": options.monochrome,
    "boardPoints": list(board_page.rect), "kitPages": len(kit)}, indent=2) + "\n")
print(json.dumps({"kitPages": len(kit), "paper": "Legal portrait, 612 × 1008 pt", "guidePages": len(guide),
    "boardMm": [board["widthMm"], board["heightMm"]], "monochrome": options.monochrome}))
