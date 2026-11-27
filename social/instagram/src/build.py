"""Build repository-owned Instagram artwork and its preview sheets.

Run from any working directory. Browser rendering uses the adjacent Playwright
helper; use --html-only when only editable previews are needed.
"""
import argparse
import json
import os
import pathlib
import shutil
import subprocess
import zipfile

K = pathlib.Path(__file__).resolve().parents[1]
S = K / 'src'
MARK = '''<svg viewBox="0 0 40 40" class="{cls}"><rect width="40" height="40" rx="5" fill="{bg}"/><g fill="none" stroke="{fg}" stroke-width="2.4" stroke-linejoin="round"><path d="M5 29 16 10l8 13 5-8 7 14H5Z"/><path d="m12 17 4 3 3-4M6 34h28"/></g></svg>'''
def mark(cls='mk', bg='#d7ec8b', fg='#173c32'): return MARK.format(cls=cls, bg=bg, fg=fg)
CSS = '''
@font-face{font-family:BC;src:url(barlow-condensed-700.ttf);font-weight:700}
@font-face{font-family:DM;src:url(dm-sans-400.ttf);font-weight:400}
@font-face{font-family:DM;src:url(dm-sans-700.ttf);font-weight:700}
:root{--paper:#f6f5ee;--white:#fff;--ink:#192e27;--pine:#173c32;--muted:#56645b;--line:#d4dbd0;--lime:#d7ec8b;--soft:#e9eee3;--alert:#9c3827;--alert-soft:#fbede7}
*{box-sizing:border-box;margin:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{background:var(--paper);color:var(--ink);font:400 34px/1.45 DM,sans-serif;-webkit-font-smoothing:antialiased}
.post{position:relative;width:1080px;height:1350px;padding:84px 84px 0;display:flex;flex-direction:column}
.dark{background:var(--pine);color:var(--paper)}
.eyebrow{font:700 22px/1.4 DM;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);margin-bottom:28px}
.dark .eyebrow{color:var(--lime)}
h1{font:700 132px/.94 BC;text-transform:uppercase;letter-spacing:-.012em;margin-bottom:36px}
h1 span{color:var(--lime)} .light h1 span{color:inherit}
h2{font:700 40px/1.2 DM;letter-spacing:-.02em;margin-bottom:10px}
.lead{font-size:36px;line-height:1.45;color:var(--muted);max-width:860px}
.dark .lead{color:#e3e9df}
.grow{flex:1}
.foot{display:flex;align-items:center;justify-content:space-between;border-top:2px solid var(--line);margin:0 -84px;padding:30px 84px 40px;font-size:22px}
.dark .foot{border-color:#2f574a}
.brand{display:flex;align-items:center;gap:18px;font:700 26px/1.1 DM;letter-spacing:.01em}
.brand small{display:block;font-size:17px;letter-spacing:.14em;margin-top:5px}
.mk{width:64px;height:64px}
.url{text-align:right;color:var(--muted);line-height:1.35}
.dark .url{color:#c9d4c6}
.url b{color:var(--ink);font-weight:700} .dark .url b{color:var(--paper)}
.rows{border-top:2px solid var(--line)}
.row{display:grid;grid-template-columns:90px 1fr;padding:26px 0;border-bottom:2px solid var(--line)}
.num{font:700 24px DM;color:var(--muted);padding-top:10px;letter-spacing:.06em}
.row p{color:var(--muted);font-size:31px;line-height:1.4}
.steps{list-style:none;padding:0}
.steps li{position:relative;padding-left:84px;margin-bottom:26px;font-size:33px;line-height:1.4}
.steps li::before{content:attr(data-n);position:absolute;left:0;top:0;width:52px;height:52px;border-radius:50%;background:var(--soft);color:var(--pine);font:700 24px/52px DM;text-align:center}
.call{background:var(--alert-soft);border-top:6px solid var(--alert);padding:34px 40px;margin-bottom:46px}
.call h2{font-size:44px} .call h2 em{font-style:normal;color:var(--alert)}
.call p{font-size:30px;line-height:1.42}
.btn{display:inline-block;background:var(--lime);color:var(--pine);font:700 28px DM;padding:22px 34px;border-radius:3px}
.chips{display:flex;gap:28px;font:700 20px DM;letter-spacing:.13em;color:#c9d4c6;text-transform:uppercase}
.slide{position:absolute;top:84px;right:84px;font:700 22px DM;letter-spacing:.1em;color:var(--muted)}
.dark .slide{color:var(--lime)}
.launch{padding:0;background:var(--pine);color:var(--paper)}
.launch-photo{position:absolute;inset:0 0 auto;height:850px;background:url(stawamus-chief-1600.webp) center 38%/cover}
.launch-shade{position:absolute;inset:0;background:linear-gradient(180deg,#102b2490 0%,#102b2410 24%,#173c32a8 49%,#173c32 62%)}
.launch-brand{position:absolute;left:76px;right:76px;top:64px;display:flex;align-items:center;gap:20px;font:700 30px/1.15 DM;letter-spacing:.04em}
.launch-brand .mk{width:76px;height:76px}
.launch-brand small{display:block;margin-top:10px;font-size:20px;letter-spacing:.18em;color:var(--lime)}
.launch h1{position:absolute;left:76px;right:76px;top:422px;margin:0;font-size:166px;line-height:.96;letter-spacing:-.01em}
.launch h1 span{color:var(--lime)}
.launch-value{position:absolute;left:80px;right:76px;top:945px;font-size:36px;line-height:1.35;color:#e3e9df}
.launch-credit{position:absolute;left:80px;right:76px;top:350px;font-size:20px;line-height:1.5;color:#dce5d7;text-align:right;text-shadow:0 1px 4px #102b24}
.launch-cta{position:absolute;left:76px;right:76px;bottom:90px;padding:26px 30px;background:var(--lime);color:var(--pine)}
.launch-cta strong{display:flex;align-items:center;justify-content:space-between;font:700 28px/1.2 DM;letter-spacing:.1em;text-transform:uppercase}
.launch-cta .launch-arrow{font-size:42px;line-height:1}
.launch-address{display:flex;align-items:end;justify-content:space-between;gap:24px;margin-top:14px}
.launch-address b{font-size:32px;letter-spacing:-.02em;white-space:nowrap}
.launch-address span{font-size:28px;white-space:nowrap}
.launch-disclaimer{position:absolute;left:76px;right:76px;bottom:30px;font-size:22px;line-height:1.4;color:#c9d4c6}
.campaign{padding:0;background:var(--paper);color:var(--pine)}
.campaign-dark{background:var(--pine);color:var(--paper)}
.campaign-brand{position:absolute;left:76px;right:76px;top:64px;display:flex;align-items:center;gap:20px;font:700 30px/1.15 DM;letter-spacing:.04em}
.campaign-brand .mk{width:76px;height:76px}
.campaign-brand small{display:block;margin-top:10px;font-size:20px;letter-spacing:.18em;color:var(--muted)}
.campaign-dark .campaign-brand small{color:var(--lime)}
.campaign h1{position:absolute;left:76px;right:76px;top:188px;margin:0;font-size:145px;line-height:.96}
.planning-steps{position:absolute;left:76px;right:76px;top:514px}
.planning-step{display:grid;grid-template-columns:56px 1fr;gap:26px;min-height:126px;padding:20px 0;border-top:2px solid var(--line)}
.planning-number{display:grid;place-items:center;align-self:start;width:54px;height:54px;margin-top:2px;background:var(--lime);color:var(--pine);font:700 25px/1 DM;border-radius:50%}
.planning-step h2{font-size:40px;line-height:1.16;text-transform:uppercase;margin:0 0 10px}
.planning-step p{font-size:30px;line-height:1.3;color:var(--muted)}
.planning-contact{position:absolute;left:76px;right:76px;top:936px;padding:26px 30px;background:var(--soft);border-left:6px solid var(--pine)}
.planning-contact strong{display:block;margin-bottom:10px;font-size:28px;line-height:1.2;letter-spacing:.04em}
.planning-contact p{font-size:31px;line-height:1.35}
.campaign-cta{position:absolute;left:76px;right:76px;bottom:90px}
.campaign-cta strong{display:flex;align-items:center;justify-content:space-between;font:700 28px/1.2 DM;letter-spacing:.08em}
.campaign-cta .launch-arrow{font-size:38px;line-height:1}
.campaign-cta .launch-address{margin-top:12px}
.campaign-disclaimer{position:absolute;left:76px;right:76px;bottom:30px;font-size:22px;line-height:1.4;color:var(--muted)}
.campaign-dark .campaign-cta strong{color:var(--lime)}
.campaign-dark .campaign-disclaimer{color:#c9d4c6}
.lost-campaign h1{font-size:175px}
.lost-stay{position:absolute;left:80px;right:76px;top:548px;font-size:36px;line-height:1.35}
.lost-call{position:absolute;left:76px;right:76px;top:650px;padding:30px 36px;background:var(--alert-soft);border-top:6px solid var(--alert);color:var(--ink)}
.lost-call h2{margin:0 0 16px;color:var(--alert);font:700 74px/1.05 BC}
.lost-call p{font-size:36px;line-height:1.35}
.lost-warm{position:absolute;left:80px;right:76px;top:960px}
.lost-warm strong{display:block;margin-bottom:8px;color:var(--lime);font-size:42px;line-height:1.2}
.lost-warm p{font-size:36px;line-height:1.35}
.lost-signal{position:absolute;left:80px;right:76px;top:1095px;font-size:28px;line-height:1.35;color:#c9d4c6}
'''
POST_FORMAT_CSS = '''
html,body{width:1080px;height:1080px;overflow:hidden}
.post{left:140.4px;top:40.5px;transform:scale(.74);transform-origin:top left}
'''
def page(body, cls=''):
    background = 'var(--pine)' if cls in ('dark', 'launch', 'campaign campaign-dark lost-campaign') else 'var(--paper)'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{POST_FORMAT_CSS}</style></head><body style="background:{background}"><div class="post {cls}">{body}</div></body></html>'
def foot(dark=False):
    bg = '#d7ec8b'
    return f'''<div class="foot"><div class="brand">{mark()}<div>OUTDOOR SAFETY<small>SEA-TO-SKY</small></div></div>
<div class="url"><b>lzl462.github.io/outdoorsafety</b><br>Not an official rescue site. In an emergency, call 9-1-1.</div></div>'''

posts = {}
# 1 website launch: public-facing campaign promotion, without personal framing.
posts['01-intro'] = page(f'''
<div class="launch-photo"></div><div class="launch-shade"></div>
<div class="launch-brand">{mark()}<div>OUTDOOR SAFETY<small>SEA-TO-SKY</small></div></div>
<p class="launch-credit">Stawamus Chief · Squamish<br>Photo: James Abbott · CC BY 2.0</p>
<h1>Big days.<br><span>Better<br>prepared.</span></h1>
<p class="launch-value">Trip planning. Packing lists.<br>Clear next steps.</p>
<div class="launch-cta"><strong>Explore the website <span class="launch-arrow" aria-hidden="true">↗</span></strong>
<div class="launch-address"><b>lzl462.github.io/outdoorsafety</b><span>Link in bio</span></div></div>
<p class="launch-disclaimer">This is not an official rescue site. In an emergency, call 9-1-1.</p>''', 'launch')

# 2 preparation campaign: three priorities and a separate contact deadline.
posts['02-before-you-go'] = page(f'''
<div class="campaign-brand">{mark()}<div>OUTDOOR SAFETY<small>SEA-TO-SKY</small></div></div>
<h1>BEFORE<br>YOUR TRIP.</h1>
<div class="planning-steps">
<div class="planning-step"><span class="planning-number">01</span><div><h2>PLAN THE ROUTE.</h2><p>Fits the group. Check conditions.</p></div></div>
<div class="planning-step"><span class="planning-number">02</span><div><h2>PACK FOR A DELAY.</h2><p>Take the shared essentials.</p></div></div>
<div class="planning-step"><span class="planning-number">03</span><div><h2>SET A TURNAROUND TIME.</h2><p>Leave time and energy to return.</p></div></div>
</div>
<div class="planning-contact"><strong>LEAVE YOUR PLAN.</strong><p>Agree when your contact should call 9-1-1 if you have not returned or checked in.</p></div>
<div class="campaign-cta"><strong>GET THE CHECKLIST <span class="launch-arrow" aria-hidden="true">↗</span></strong><div class="launch-address"><b>lzl462.github.io/outdoorsafety</b><span>Link in bio</span></div></div>
<p class="campaign-disclaimer">This is not an official rescue site. In an emergency, call 9-1-1.</p>''', 'campaign')

# 3 pack list
items = [('Light','a headlamp and spare batteries'),('Fire-making kit','matches or a lighter and a fire starter'),('Signalling','a whistle or signalling mirror'),('Extra food and water','enough for an unexpected delay'),('Extra clothing','warm layers and a rain shell'),('Navigation & communication','map, compass, offline maps, a way to call for help'),('First aid kit','and know how to use it'),('Emergency shelter','an emergency blanket or shelter'),('Pocket knife','or multi-tool'),('Sun protection','sunglasses, sunscreen and a hat')]
grid = ''.join(f'<div style="display:flex;gap:22px;padding:15px 0;border-bottom:2px solid var(--line)"><span style="flex:none;width:40px;height:40px;border:3px solid var(--pine);border-radius:4px;margin-top:4px"></span><div><b style="font-size:30px">{a}</b><br><span style="color:var(--muted);font-size:25px;line-height:1.35;display:block">{b}</span></div></div>' for a,b in items)
posts['03-pack-list'] = page(f'''
<p class="eyebrow">Prepare / Essentials</p>
<h1 style="font-size:96px;margin-bottom:24px">Pack for the wait, not only for the walk.</h1>
<div style="display:grid;grid-template-columns:1fr 1fr;column-gap:48px;border-top:2px solid var(--line)">{grid}</div>
<p style="margin-top:26px;font-size:26px;color:var(--muted);line-height:1.4">The ten shared essentials. Bring personal medication and spare glasses if you need them.</p>
<div class="grow"></div>{foot()}''', 'light')

# 4 if lost: immediate priorities, with the unsafe-place exception explicit.
posts['04-if-lost'] = page(f'''
<div class="campaign-brand">{mark()}<div>OUTDOOR SAFETY<small>SEA-TO-SKY</small></div></div>
<h1>LOST?<br>STOP.</h1>
<p class="lost-stay">Stay together. Stay put unless it is unsafe.</p>
<div class="lost-call"><h2>CALL 9-1-1 EARLY.</h2><p>Share your location and what happened. Follow instructions.</p></div>
<div class="lost-warm"><strong>Keep warm.</strong><p>Signal for help.</p></div>
<p class="lost-signal">Plan for no signal: read No cell service.</p>
<div class="campaign-cta"><strong>WHAT TO DO NEXT <span class="launch-arrow" aria-hidden="true">↗</span></strong><div class="launch-address"><b>lzl462.github.io/outdoorsafety</b><span>Link in bio</span></div></div>
<p class="campaign-disclaimer">This is not an official rescue site. In an emergency, call 9-1-1.</p>''', 'campaign campaign-dark lost-campaign')

# 5 no service
posts['05-no-service'] = page(f'''
<p class="eyebrow">Get help / No cell service</p>
<h1 style="font-size:120px">No signal.<br><span>Have a plan.</span></h1>
<p class="lead" style="margin-bottom:40px;color:#e3e9df">Reception can disappear soon after you leave the parking area. Plan another way to call for help.</p>
<ul class="steps" style="color:var(--paper)">
<li data-n="1">Download a map that works offline and learn how to find your GPS position.</li>
<li data-n="2">Save phone battery for emergency communication and carry a separate light.</li>
<li data-n="3">Choose an emergency communication device suited to the route and learn how to use its SOS function before leaving.</li>
<li data-n="4">Leave a plan. Agree when your contact should call 9-1-1 if you miss your return/check-in.</li>
</ul>
<p style="font-size:28px;color:var(--lime);margin-top:6px">An offline map helps with navigation. It does not send an SOS.</p>
<div class="grow"></div>{foot(True)}''', 'dark')

# 6 emergency numbers
nums=[('Emergency','police, fire, ambulance, search and rescue','9-1-1',True),('Poison Control','','1-800-567-8911',False),('BC Wildfire Service','report a wildfire · or *5555 from a cell','1-800-663-5555',False),('Marine / Howe Sound','Joint Rescue Coordination Centre · on the water, VHF Channel 16','1-800-567-5111',False)]
tbl=''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;gap:30px;padding:30px {"36px" if hi else "0"};{"background:var(--alert-soft);border-top:6px solid var(--alert);margin-bottom:6px" if hi else "border-bottom:2px solid var(--line)"}"><div><h2 style="margin:0">{a}</h2><span style="color:var(--muted);font-size:26px;line-height:1.35;display:block;max-width:520px">{b}</span></div><b style="font:700 {"92px" if hi else "52px"}/1 BC;color:{"var(--alert)" if hi else "var(--pine)"};white-space:nowrap">{n}</b></div>' for a,b,n,hi in nums)
posts['06-emergency-numbers'] = page(f'''
<p class="eyebrow">Get help / Emergency numbers</p>
<h1 style="font-size:112px">Keep the right number within reach.</h1>
{tbl}
<p style="margin-top:30px;font-size:28px;line-height:1.42">If you cannot connect, see <b>No cell service</b> on the website.</p>
<div class="grow"></div>{foot()}''', 'light')

# 7 carousel: common mistakes
posts['07-mistakes-1'] = page(f'''<span class="slide">1 / 3 →</span>
<div class="grow" style="max-height:260px"></div>
<p class="eyebrow">Learn / Common mistakes</p>
<h1 style="font-size:150px">Five <span>common</span> mistakes.</h1>
<p class="lead">Preparation cannot prevent every incident, but it can reduce how serious one becomes.</p>
<div class="grow"></div>{foot(True)}''', 'dark')
M=[('01','“A beautiful photo is enough research.”','Check reliable route information and talk to people who have done the trip.'),
('02','“The distance looks short.”','Read the elevation gain, terrain, and time for the return.'),
('03','“We are nearly there, so we should keep going.”','Stick to your turnaround time and keep enough daylight and energy for the descent.'),
('04','“I am warm while moving, so I have enough layers.”','Pack extra warmth and emergency shelter. Put layers on before you get cold.'),
('05','“I know this trail; it will not happen to me.”','Leave a trip plan. Agree when your contact should call 9-1-1 if you have not returned or checked in.')]
def mrows(ms): return '<div class="rows">'+''.join(f'<div class="row"><span class="num">{n}</span><div><h2>{t}</h2><p><b style="color:var(--pine)">A better choice:</b> {b}</p></div></div>' for n,t,b in ms)+'</div>'
posts['07-mistakes-2'] = page(f'<span class="slide">2 / 3</span><p class="eyebrow">Common mistakes / 01–03</p><h1 style="font-size:104px">Check the route <span>behind the photo.</span></h1>{mrows(M[:3])}<div class="grow"></div>{foot()}', 'light')
posts['07-mistakes-3'] = page(f'<span class="slide">3 / 3</span><p class="eyebrow">Common mistakes / 04–05</p><h1 style="font-size:104px">Pack for the wait. <span>Leave a plan.</span></h1>{mrows(M[3:])}<p style="margin-top:36px;font-size:30px">Read all five on the website: <b>Learn / Common mistakes</b>.</p><div class="grow"></div>{foot()}', 'light')

# profile pictures 1080x1080
PCSS = CSS.replace('html,body{width:1080px;height:1350px;overflow:hidden}','html,body{width:1080px;height:1080px;overflow:hidden}')
def ppage(b): return f'<!doctype html><html><head><meta charset="utf-8"><style>{PCSS}</style></head><body>{b}</body></html>'
prof = {
 'profile-a-mark': ppage(f'<div style="width:1080px;height:1080px;background:#d7ec8b;display:grid;place-items:center"><svg viewBox="0 0 40 40" width="700" height="700"><g fill="none" stroke="#173c32" stroke-width="2.9" stroke-linejoin="round" stroke-linecap="round"><path d="M5 29 16 10l8 13 5-8 7 14H5Z"/><path d="m12 17 4 3 3-4M6 34h28"/></g></svg></div>'),
 'profile-b-monogram': ppage(f'<div style="width:1080px;height:1080px;background:#173c32;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px"><svg viewBox="0 0 40 30" width="470" height="352"><g fill="none" stroke="#d7ec8b" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"><path d="M5 26 16 7l8 13 5-8 7 14H5Z"/><path d="m12 14 4 3 3-4"/></g></svg><div style="font:700 290px/0.9 BC;color:#f6f5ee;letter-spacing:.01em">OS<span style="color:#d7ec8b">48</span></div></div>'),
}
def preview_sheets():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        raise SystemExit('Preview sheets need Pillow. Run this command in a development Python environment with Pillow installed.')

    font = ImageFont.truetype(str(S / 'dm-sans-700.ttf'), 24)
    files = [K / 'posts' / f'{name}.png' for name in posts]
    files += [K / 'profile' / f'{name}.png' for name in prof]
    columns, tile_width, tile_height, gap = 4, 324, 324, 28
    rows = (len(files) + columns - 1) // columns
    sheet = Image.new('RGB', (gap + columns * (tile_width + gap), gap + rows * (tile_height + 58 + gap)), '#e9eee3')
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(files):
        if not path.exists():
            raise SystemExit(f'Missing export: {path}. Build all artwork before refreshing the overview.')
        artwork = Image.open(path).convert('RGB')
        artwork.thumbnail((tile_width, tile_height), Image.Resampling.LANCZOS)
        x = gap + index % columns * (tile_width + gap)
        y = gap + index // columns * (tile_height + 58 + gap)
        sheet.paste(artwork, (x + (tile_width - artwork.width) // 2, y))
        caption_font = font
        caption_size = 24
        while draw.textbbox((0, 0), path.name, font=caption_font)[2] > tile_width:
            caption_size -= 1
            caption_font = ImageFont.truetype(str(S / 'dm-sans-700.ttf'), caption_size)
        draw.text((x, y + tile_height + 12), path.name, fill='#192e27', font=caption_font)
    sheet.save(K / 'overview.png', optimize=True)

    grid_columns, grid_width, grid_height = 3, 243, 324
    grid_sheet = Image.new('RGB', (gap + grid_columns * (grid_width + gap), gap + 3 * (grid_height + 58 + gap)), '#e9eee3')
    draw = ImageDraw.Draw(grid_sheet)
    for index, name in enumerate(posts):
        artwork = Image.open(K / 'posts' / f'{name}.png').convert('RGB')
        if artwork.size != (1080, 1080):
            raise SystemExit(f'{name}: rebuild all square post exports before refreshing the grid preview.')
        artwork = artwork.crop((135, 0, 945, 1080)).resize((grid_width, grid_height), Image.Resampling.LANCZOS)
        left = gap + index % grid_columns * (grid_width + gap)
        top = gap + index // grid_columns * (grid_height + 58 + gap)
        grid_sheet.paste(artwork, (left, top))
        label_font = font
        label_size = 24
        while draw.textbbox((0, 0), name, font=label_font)[2] > grid_width:
            label_size -= 1
            label_font = ImageFont.truetype(str(S / 'dm-sans-700.ttf'), label_size)
        draw.text((left, top + grid_height + 12), name, fill='#192e27', font=label_font)
    grid_sheet.save(K / 'profile-grid-preview.png', optimize=True)

    with zipfile.ZipFile(K / 'instagram-posts-square.zip', 'w', compression=zipfile.ZIP_STORED) as archive:
        for name in posts:
            archive.write(K / 'posts' / f'{name}.png', arcname=f'{name}.png')

    with zipfile.ZipFile(K / 'instagram-upload-square.zip', 'w', compression=zipfile.ZIP_STORED) as archive:
        for name in posts:
            upload = K / 'upload-square' / f'{name}-square-1080.jpg'
            if not upload.is_file():
                raise SystemExit(f'{name}: render all square JPG files before refreshing the upload ZIP.')
            archive.write(upload, arcname=upload.name)

    crop_sheet = Image.new('RGB', (800, 430), '#e9eee3')
    draw = ImageDraw.Draw(crop_sheet)
    for index, name in enumerate(prof):
        artwork = Image.open(K / 'profile' / f'{name}.png').convert('RGB').resize((280, 280), Image.Resampling.LANCZOS)
        mask = Image.new('L', (280, 280))
        ImageDraw.Draw(mask).ellipse((0, 0, 279, 279), fill=255)
        x = 60 + index * 400
        crop_sheet.paste(artwork, (x, 36), mask)
        draw.text((x, 342), name, fill='#192e27', font=font)
    crop_sheet.save(K / 'profile' / 'circle-crop-preview.png', optimize=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html-only', action='store_true', help='Write all HTML previews without rendering PNGs.')
    parser.add_argument('--only', nargs='+', choices=[*posts, *prof], help='Render only these artwork names; all previews are still synchronized.')
    parser.add_argument('--cdp', help='Connect to an existing Chromium debugging endpoint, using an isolated context.')
    parser.add_argument('--browser', help='Chromium executable when launching a browser instead of connecting over CDP.')
    parser.add_argument('--playwright-module', default=os.environ.get('PLAYWRIGHT_MODULE'), help='Optional path to an installed Playwright index.mjs.')
    parser.add_argument('--previews-only', action='store_true', help='Rebuild overview/circle previews from existing PNGs.')
    args = parser.parse_args()
    for folder in [S, K / 'posts', K / 'profile', K / 'upload-square']:
        folder.mkdir(parents=True, exist_ok=True)
    if args.previews_only:
        preview_sheets()
        return
    targets = []
    for group, size, folder in [(posts, (1080, 1080), 'posts'), (prof, (1080, 1080), 'profile')]:
        for name, markup in group.items():
            (S / f'{name}.html').write_text(markup, encoding='utf-8')
            if not args.only or name in args.only:
                target = {'name': name, 'width': size[0], 'height': size[1], 'output': str(K / folder / f'{name}.png')}
                if folder == 'posts':
                    target['safeBounds'] = {'left': 135, 'top': 24, 'right': 945, 'bottom': 1056}
                    target['uploadOutput'] = str(K / 'upload-square' / f'{name}-square-1080.jpg')
                targets.append(target)
    if args.html_only:
        print(f'Wrote {len(posts) + len(prof)} HTML previews under {S}')
        return
    config = dict(source=str(S), targets=targets, cdp=args.cdp, browser=args.browser, playwrightModule=args.playwright_module)
    node = shutil.which('node')
    if not node:
        raise SystemExit('PNG rendering needs Node.js and Playwright. Install the development tools, or use --html-only.')
    try:
        subprocess.run([node, str(S / 'render.mjs')], input=json.dumps(config), text=True, check=True)
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.returncode)
    preview_sheets()


if __name__ == '__main__':
    main()
