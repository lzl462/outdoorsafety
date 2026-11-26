import subprocess, pathlib
K = pathlib.Path('/workspace/instagram-kit'); S = K/'src'
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
'''
def page(body, cls=''):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="post {cls}">{body}</div></body></html>'
def foot(dark=False):
    bg = '#d7ec8b'
    return f'''<div class="foot"><div class="brand">{mark()}<div>OUTDOOR SAFETY<small>SEA-TO-SKY</small></div></div>
<div class="url"><b>lzl462.github.io/outdoorsafety</b><br>Not an official rescue site. In an emergency, call 9-1-1.</div></div>'''

posts = {}
# 1 intro (dark hero + photo)
posts['01-intro'] = page(f'''
<div style="margin:-84px -84px 0;height:560px;background:url(stawamus-chief-1600.webp) center/cover;position:relative">
<div style="position:absolute;left:0;right:0;bottom:0;padding:16px 84px;font-size:19px;color:#f6f5ee;background:linear-gradient(transparent,#0008);display:flex;justify-content:space-between"><span>Stawamus Chief · Squamish</span><span>Photo: James Abbott · CC BY 2.0</span></div></div>
<div style="padding-top:64px"><p class="eyebrow">A little planning goes a long way</p>
<h1 style="font-size:124px">Big days.<br><span>Better prepared.</span></h1>
<p class="lead">Plain-English preparation for beginners and visitors planning day trips in the Sea-to-Sky area of British Columbia.</p>
<p class="lead" style="margin-top:22px;font-size:30px">A school capstone by Liz. Made for the Sea-to-Sky.</p></div>
<div class="grow"></div>{foot(True)}''', 'dark')

# 2 trip plan
posts['02-before-you-go'] = page(f'''
<p class="eyebrow">01 / Before you go</p>
<h1 style="font-size:116px;margin-bottom:28px">The good part starts with a plan.</h1>
<p class="lead" style="margin-bottom:34px">You choose the adventure. Start with these three things.</p>
<div class="rows">
<div class="row"><span class="num">01</span><div><h2>Make a plan</h2><p>Choose a realistic route. Leave it with someone reliable.</p></div></div>
<div class="row"><span class="num">02</span><div><h2>Take the essentials</h2><p>Prepare for your activity, the conditions and an unexpected wait.</p></div></div>
<div class="row"><span class="num">03</span><div><h2>Know when to turn around</h2><p>Watch the weather, the time and the people you are with.</p></div></div>
</div>
<p style="margin-top:40px;font-size:30px;line-height:1.42"><b>Give your contact a job:</b> agree on a time for them to call 9-1-1 if you have not returned or checked in.</p>
<div class="grow"></div>{foot()}''', 'light')

# 3 pack list
items = [('Light','a headlamp and spare batteries'),('Fire-making kit','matches or a lighter and a fire starter'),('Signalling','a whistle or signalling mirror'),('Extra food and water','enough for an unexpected delay'),('Extra clothing','warm layers and a rain shell'),('Navigation','map, compass, offline maps, a way to call for help'),('First aid kit','and know how to use it'),('Emergency shelter','an emergency blanket or shelter'),('Pocket knife','or multi-tool'),('Sun protection','sunglasses, sunscreen and a hat')]
grid = ''.join(f'<div style="display:flex;gap:22px;padding:15px 0;border-bottom:2px solid var(--line)"><span style="flex:none;width:40px;height:40px;border:3px solid var(--pine);border-radius:4px;margin-top:4px"></span><div><b style="font-size:30px">{a}</b><br><span style="color:var(--muted);font-size:25px;line-height:1.35;display:block">{b}</span></div></div>' for a,b in items)
posts['03-pack-list'] = page(f'''
<p class="eyebrow">Prepare / Essentials</p>
<h1 style="font-size:96px;margin-bottom:24px">Pack for the wait, not only for the walk.</h1>
<div style="display:grid;grid-template-columns:1fr 1fr;column-gap:48px;border-top:2px solid var(--line)">{grid}</div>
<p style="margin-top:26px;font-size:26px;color:var(--muted);line-height:1.4">The ten shared essentials, from AdventureSmart. Bring personal medication and spare glasses if you need them.</p>
<div class="grow"></div>{foot()}''', 'light')

# 4 if lost
posts['04-if-lost'] = page(f'''
<p class="eyebrow">Get help / What to do if…</p>
<h1 style="margin-bottom:34px">If you are lost.</h1>
<div class="call"><h2>Lost or hurt? Call <em>9-1-1</em></h2><p>Tell the call taker where you are and what has happened. Stay on the line and follow their instructions.</p></div>
<ul class="steps">
<li data-n="1"><b>Stop.</b> Do not keep walking to find the route.</li>
<li data-n="2"><b>Stay</b> with your group in that spot unless it is unsafe.</li>
<li data-n="3"><b>Call 9-1-1.</b> Give your GPS position if you can, the route, and where you started.</li>
<li data-n="4"><b>Stay warm.</b> Put on warm layers. Use three whistle blasts to signal for help.</li>
</ul>
<p style="margin-top:14px;font-size:30px;line-height:1.42;color:var(--muted);border-top:2px solid var(--line);padding-top:30px">Do not guess a downhill route through unfamiliar terrain. Staying put when safe helps searchers narrow the area they need to search.</p>
<div class="grow"></div>{foot()}''', 'light')

# 5 no service
posts['05-no-service'] = page(f'''
<p class="eyebrow">Get help / No cell service</p>
<h1 style="font-size:120px">Your phone is <span>a weak plan.</span></h1>
<p class="lead" style="margin-bottom:40px;color:#e3e9df">Reception can disappear soon after you leave the parking area. Plan another way to call for help.</p>
<ul class="steps" style="color:var(--paper)">
<li data-n="1">Download a map that works offline and learn how to find your GPS position.</li>
<li data-n="2">Save phone battery for emergency communication and carry a separate light.</li>
<li data-n="3">Choose an emergency communication device suited to the route and learn how to use its SOS function before leaving.</li>
<li data-n="4">Leave a trip plan and an agreed check-in time with someone reliable.</li>
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
('05','“I know this trail; it will not happen to me.”','Leave a trip plan and an agreed check-in time, and plan how to call for help.')]
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
def render(name, html, w, h, outdir):
    f = S/f'{name}.html'; f.write_text(html)
    out = outdir/f'{name}.png'
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=1',f'--window-size={w},{h}','--virtual-time-budget=3000',f'--screenshot={out}',f'file://{f}'],check=True,capture_output=True)
for n,h in posts.items(): render(n,h,1080,1350,K/'posts')
for n,h in prof.items(): render(n,h,1080,1080,K/'profile')
