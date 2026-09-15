#!/usr/bin/env python3
"""Build printable Sea-to-Sky outdoor safety PDFs."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1] / "pdfs"
ROOT.mkdir(exist_ok=True)

PINE = colors.HexColor("#10261a")
ALERT = colors.HexColor("#c23b22")
CREAM = colors.HexColor("#f6f1e6")
GOLD = colors.HexColor("#c9a24a")


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "TitleX",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=22,
            leading=26,
            textColor=PINE,
            spaceAfter=6,
            alignment=0,
        ),
        "sub": ParagraphStyle(
            "SubX",
            parent=base["Normal"],
            fontSize=10,
            textColor=ALERT,
            spaceAfter=12,
        ),
        "h": ParagraphStyle(
            "HX",
            parent=base["Heading2"],
            fontName="Times-Bold",
            fontSize=13,
            textColor=PINE,
            spaceBefore=8,
            spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "BodyX",
            parent=base["BodyText"],
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#1a1a16"),
        ),
        "small": ParagraphStyle(
            "SmallX",
            parent=base["Normal"],
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#5c5a52"),
        ),
        "box": ParagraphStyle(
            "BoxX",
            parent=base["BodyText"],
            fontSize=10.5,
            leading=14,
            textColor=colors.white,
        ),
    }


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PINE)
    canvas.rect(0, letter[1] - 28, letter[0], 28, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 9)
    canvas.drawString(0.75 * inch, letter[1] - 18, "Outdoor Safety  ·  Sea-to-Sky District")
    canvas.drawRightString(letter[0] - 0.75 * inch, letter[1] - 18, "Call 9-1-1 in an emergency")
    canvas.setFillColor(colors.HexColor("#5c5a52"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(
        0.75 * inch,
        0.45 * inch,
        "Educational handout. Not an official SAR or government document. Rescue in B.C. is free.",
    )
    canvas.restoreState()


def bullets(items, sty):
    return ListFlowable(
        [ListItem(Paragraph(item, sty["body"]), leftIndent=8, bulletColor=PINE) for item in items],
        bulletType="bullet",
        leftIndent=16,
    )


def numbered(items, sty):
    return ListFlowable(
        [ListItem(Paragraph(item, sty["body"]), leftIndent=8, bulletColor=PINE) for item in items],
        bulletType="1",
        leftIndent=16,
    )


def banner(text, sty):
    data = [[Paragraph(text, sty["box"])]]
    table = Table(data, colWidths=[6.5 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), ALERT),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return table


def build(name, story):
    path = ROOT / name
    doc = SimpleDocTemplate(
        str(path),
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch,
        title=name.replace("-", " ").replace(".pdf", ""),
        author="Outdoor Safety Sea-to-Sky",
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("wrote", path)


def day_hike(sty):
    story = [
        Paragraph("Day hike checklist", sty["title"]),
        Paragraph("Sea-to-Sky corridor  ·  Howe Sound, Squamish, Whistler, Pemberton", sty["sub"]),
        banner("Call 9-1-1 if you are lost, injured, or overdue. Rescue in B.C. is free.", sty),
        Spacer(1, 10),
        Paragraph("Before you leave", sty["h"]),
        bullets(
            [
                "Route matches the group’s fitness, skills, and available daylight.",
                "Weather, trail, road, wildfire, and avalanche conditions checked this morning.",
                "Written trip plan left with someone who will call 9-1-1 if you are late.",
                "Turnaround time set — and you will use it.",
                "Phone charged, offline map downloaded, battery pack packed.",
                "Satellite messenger for areas without cell service.",
            ],
            sty,
        ),
        Paragraph("The 10 essentials", sty["h"]),
        bullets(
            [
                "Navigation: map, compass or GPS, and the skill to use them.",
                "Headlamp and spare batteries.",
                "Sun protection.",
                "Extra food and at least 1 litre of water per person.",
                "Extra warm layer and rain shell.",
                "First aid kit.",
                "Knife or multi-tool.",
                "Fire starter in a waterproof bag.",
                "Emergency shelter or bivy.",
                "Whistle / signalling device.",
            ],
            sty,
        ),
        Paragraph("Sea-to-Sky extras", sty["h"]),
        bullets(
            [
                "Trail shoes or boots with grip — not fashion sneakers.",
                "Microspikes if snow or ice is possible (Chief, Gondola trails, Joffre, Garibaldi).",
                "Bear spray where legal, and knowledge of how to use it.",
                "Do not start long alpine trips after late morning.",
            ],
            sty,
        ),
        Spacer(1, 8),
        Paragraph(
            "Busy rescue trails include Rubble Creek / Garibaldi Lake, Black Tusk, Panorama Ridge, Stawamus Chief, Joffre Lakes, and the Sea to Sky Gondola / Habrich area.",
            sty["small"],
        ),
    ]
    build("day-hike-checklist.pdf", story)


def winter(sty):
    story = [
        Paragraph("Winter & avalanche checklist", sty["title"]),
        Paragraph("Sea-to-Sky is avalanche country, including some hiking trails.", sty["sub"]),
        banner("No training + no kit = do not go into avalanche terrain.", sty),
        Spacer(1, 10),
        Paragraph("Check before you go", sty["h"]),
        bullets(
            [
                "Read the Avalanche Canada bulletin for the South Coast / Sea-to-Sky: avalanche.ca",
                "Mountain weather, not only the town forecast.",
                "DriveBC for Highway 99. Stay off unmaintained forest service roads.",
                "Resort boundary is not a safety boundary. Out-of-bounds is backcountry.",
            ],
            sty,
        ),
        Paragraph("Every person in the group", sty["h"]),
        bullets(
            [
                "Transceiver (beacon) worn on the body, tested that morning.",
                "Shovel and probe.",
                "Partner who can search. Do not travel alone in avalanche terrain.",
                "AST 1 (or equivalent) training at minimum.",
            ],
            sty,
        ),
        Paragraph("If someone is buried", sty["h"]),
        numbered(
            [
                "Watch the last-seen point. Shout. Switch transceivers to search.",
                "Search, probe, shovel. Companions are the best chance of survival.",
                "Call 9-1-1 as soon as you can without stopping the search.",
                "Treat for trauma and hypothermia. Keep the airway clear.",
            ],
            sty,
        ),
        Paragraph("Snow immersion (tree well / deep snow)", sty["h"]),
        bullets(
            [
                "Ski or ride with a partner who can see you.",
                "If you go down: fight to keep your head up. Pack a breathing space.",
                "Do not pull a buried partner by the legs if the head is downhill.",
            ],
            sty,
        ),
    ]
    build("winter-backcountry-checklist.pdf", story)


def trip_plan(sty):
    story = [
        Paragraph("Trip plan — leave this behind", sty["title"]),
        Paragraph("Give this to someone who will call 9-1-1 if you are overdue.", sty["sub"]),
        banner("If we are not back by the time below, call 9-1-1 and ask for police / Search and Rescue.", sty),
        Spacer(1, 12),
    ]
    labels = [
        "Name(s) and phone numbers",
        "Date of trip",
        "Trail / area / parking lot / GPS",
        "Planned route and turnaround time",
        "Expected return time",
        "Call 9-1-1 if we are not back by",
        "Vehicle make, colour, plate",
        "Number of people / dogs",
        "Gear notes (satellite messenger, inReach address)",
        "Medical notes the group should know",
    ]
    rows = []
    body = sty["body"]
    for label in labels:
        rows.append(
            [
                Paragraph(f"<b>{label}</b>", body),
                Paragraph(" ", body),
            ]
        )
    table = Table(rows, colWidths=[2.6 * inch, 3.9 * inch], rowHeights=36)
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#cfc8b8")),
                ("BACKGROUND", (0, 0), (0, -1), CREAM),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.extend(
        [
            table,
            Spacer(1, 12),
            Paragraph(
                "Sea-to-Sky 9-1-1 dispatches Squamish, Whistler, Pemberton, Lions Bay, or North Shore Rescue as needed. You will not be charged for a rescue.",
                sty["small"],
            ),
        ]
    )
    build("trip-plan.pdf", story)


def if_lost(sty):
    story = [
        Paragraph("If you are lost", sty["title"]),
        Paragraph("Sea-to-Sky backcountry  ·  print and keep in the pack", sty["sub"]),
        banner("STOP: Stop. Think. Observe. Plan. Then call 9-1-1.", sty),
        Spacer(1, 10),
        numbered(
            [
                "Stop walking. Stay together. Sit down if you need to calm the group.",
                "Call or text 9-1-1. Ask for police. Say you need Search and Rescue.",
                "Give GPS coordinates from the Compass or Maps app. Describe the last clear landmark.",
                "Stay put if you left a trip plan, unless the spot is immediately dangerous.",
                "Put on extra layers. Eat. Drink. Build or unpack shelter before dark.",
                "Signal: whistle in threes, bright clothing, fire or light at night if safe.",
                "Do not bushwhack downhill through cliffs. Many Sea-to-Sky slopes cliff out.",
            ],
            sty,
        ),
        Paragraph("If there is no cell service", sty["h"]),
        bullets(
            [
                "Try 9-1-1 anyway. Emergency calls can use any available tower.",
                "Use a satellite messenger (inReach, Zoleo, SPOT) SOS.",
                "Move only to a nearby ridge, clearing, or known trail if you are sure.",
                "Keep one person with the injured or tired. Do not split the group far apart.",
            ],
            sty,
        ),
    ]
    build("if-lost.pdf", story)


def if_injured(sty):
    story = [
        Paragraph("If someone is hurt", sty["title"]),
        Paragraph("Call 9-1-1 early. Rescues in this corridor can take hours.", sty["sub"]),
        banner("You will not be billed for Search and Rescue in British Columbia.", sty),
        Spacer(1, 10),
        numbered(
            [
                "Make the scene safe. Do not become the second patient.",
                "Call 9-1-1. Ask for police. They activate SAR.",
                "Give: location (GPS), number of people, what happened, injuries, weather, and your phone number.",
                "Treat life-threatening bleeding. Keep the person warm and dry. Hypothermia is common here.",
                "Stay with them. Send a competent person to a cell-service spot only if 9-1-1 cannot connect.",
                "Prepare for a long wait: extra layers, headlamp, water, a way to signal a helicopter (bright tarp).",
            ],
            sty,
        ),
        Paragraph("Tell the operator", sty["h"]),
        bullets(
            [
                "Trail name and last junction (example: Rubble Creek, 2 km below Garibaldi Lake).",
                "Whether you can walk, need a helicopter, or are on steep rock or snow.",
                "If anyone has a satellite messenger.",
            ],
            sty,
        ),
    ]
    build("if-injured.pdf", story)


def numbers(sty):
    story = [
        Paragraph("Sea-to-Sky emergency numbers", sty["title"]),
        Paragraph("Keep this card in the glove box and a photo on your phone.", sty["sub"]),
        banner("Backcountry emergency: 9-1-1  ·  ask for police  ·  rescue is free", sty),
        Spacer(1, 12),
    ]
    body = sty["body"]
    rows = [
        [Paragraph("<b>Service</b>", body), Paragraph("<b>Number</b>", body), Paragraph("<b>Notes</b>", body)],
        [Paragraph("Police / Fire / Ambulance / SAR", body), Paragraph("9-1-1", body), Paragraph("No special local SAR number", body)],
        [Paragraph("Wildfire", body), Paragraph("1-800-663-5555 or *5555", body), Paragraph("Or BC Wildfire app", body)],
        [Paragraph("Marine distress", body), Paragraph("1-800-567-5111", body), Paragraph("VHF Channel 16", body)],
        [Paragraph("Squamish RCMP (non-emergency)", body), Paragraph("604-892-6100", body), Paragraph("squamishsar.org", body)],
        [Paragraph("Whistler RCMP (non-emergency)", body), Paragraph("604-932-3044", body), Paragraph("whistlersar.com", body)],
        [Paragraph("Pemberton RCMP (non-emergency)", body), Paragraph("604-894-6634", body), Paragraph("pembertonsar.ca", body)],
        [Paragraph("Conservation Officer Service", body), Paragraph("1-877-952-7277", body), Paragraph("Wildlife / #7277", body)],
        [Paragraph("DriveBC", body), Paragraph("1-800-550-4997", body), Paragraph("drivebc.ca", body)],
        [Paragraph("Poison Control", body), Paragraph("1-800-567-8911", body), Paragraph("", body)],
        [Paragraph("Crisis support", body), Paragraph("9-8-8", body), Paragraph("Call or text", body)],
    ]
    table = Table(rows, colWidths=[2.4 * inch, 2.0 * inch, 2.1 * inch], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PINE),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d7d1c4")),
                ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#f8d7d0")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("ROWBACKGROUNDS", (0, 2), (-1, -1), [colors.white, CREAM]),
            ]
        )
    )
    # Header cells need white text - Paragraphs already have default dark color.
    # Rebuild header with white paragraph style.
    white = ParagraphStyle("W", parent=body, textColor=colors.white)
    rows[0] = [
        Paragraph("<b>Service</b>", white),
        Paragraph("<b>Number</b>", white),
        Paragraph("<b>Notes</b>", white),
    ]
    table = Table(rows, colWidths=[2.4 * inch, 2.0 * inch, 2.1 * inch], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PINE),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d7d1c4")),
                ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#f8d7d0")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("ROWBACKGROUNDS", (0, 2), (-1, -1), [colors.white, CREAM]),
            ]
        )
    )
    story.extend(
        [
            table,
            Spacer(1, 12),
            Paragraph("Clinics and hospitals", sty["h"]),
            bullets(
                [
                    "Squamish General Hospital — 38140 Behrner Drive",
                    "Whistler Health Care Centre — 4380 Lorimer Road",
                    "Pemberton Health Care Centre — 1403 Portage Road",
                ],
                sty,
            ),
            Paragraph(
                "Sources: BC AdventureSmart, Squamish / Whistler / Pemberton SAR, RCMP, BC Wildfire Service, Canadian Coast Guard. Verify numbers before you travel.",
                sty["small"],
            ),
        ]
    )
    build("emergency-numbers.pdf", story)


def main():
    sty = styles()
    day_hike(sty)
    winter(sty)
    trip_plan(sty)
    if_lost(sty)
    if_injured(sty)
    numbers(sty)


if __name__ == "__main__":
    main()
