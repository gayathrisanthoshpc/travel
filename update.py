import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fonts and Global Background/Typography
html = re.sub(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Lora.*?rel="stylesheet">',
    r'<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">',
    html
)

html = html.replace("'Nunito'", "'DM Sans'")
html = html.replace("'Lora'", "'Cormorant Garamond'")

# Body background
html = re.sub(
    r'html,body\{([\s\S]*?)background:var\(--s0\);([\s\S]*?)\}',
    r'html,body{\1background:radial-gradient(ellipse at top, #2C1810 0%, #1C1410 50%, #0D0A08 100%);\2}\nbody::before{\n  content:""; position:absolute; inset:0; pointer-events:none; z-index:9990;\n  background-image:url("data:image/svg+xml,%3Csvg viewBox=\'0 0 200 200\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cfilter id=\'n\'%3E%3CfeTurbulence type=\'fractalNoise\' baseFrequency=\'0.85\' numOctaves=\'4\' stitchTiles=\'stitch\'/%3E%3C/filter%3E%3Crect width=\'100%25\' height=\'100%25\' filter=\'url(%23n)\'/%3E%3C/svg%3E");\n  opacity:0.04;\n}',
    html
)

# 9. Page Transitions (Ease-in-out, -10px, 400ms)
html = html.replace("transform:translateY(22px);", "transform:translateY(-10px);")
html = html.replace("transition:opacity .45s cubic-bezier(.4,0,.2,1), transform .45s cubic-bezier(.4,0,.2,1);", "transition:opacity .4s ease-in-out, transform .4s ease-in-out;")
html = html.replace("transform:translateY(-14px)", "transform:translateY(-10px)")

# 5. Button Shimmer
btn_old = "transition:transform .15s, box-shadow .15s;\n  position:relative; overflow:hidden;"
btn_new = "transition:transform .15s, box-shadow .15s;\n  position:relative; overflow:hidden;\n}\n.btn::after {\n  content:''; position:absolute; top:-50%; left:-60%; width:20%; height:200%;\n  background:linear-gradient(to right, transparent, rgba(255,255,255,0.4), transparent);\n  transform:rotate(30deg); transition:left .6s ease-in-out;\n}\n.btn:hover::after{left:140%;"
html = html.replace(btn_old, btn_new)

# 10. Feature cards stagger fade-in
html = html.replace("animation:cardIn .5s cubic-bezier(.4,0,.2,1) both;", "opacity:0;")
html = html.replace("@keyframes cardIn{from{opacity:0;transform:translateX(-16px)}to{opacity:1;transform:translateX(0)}}", ".splash-card.show{animation:cardIn .5s cubic-bezier(.4,0,.2,1) forwards;}\n@keyframes cardIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}")
# Add JS to trigger stagger fade-in on load
js_stagger = """document.querySelectorAll('.splash-card').forEach((el,i)=>{ setTimeout(()=>el.classList.add('show'), i*150 + 100); });"""
html = html.replace("function startApp() {", f"{js_stagger}\nfunction startApp() {{")


# 6. Compass Icon Rotation
html = html.replace("animation:emblemFloat 4s ease-in-out infinite;", "/* compass anim removed from container */")
html = html.replace(".logo-emblem svg{width:38px;height:38px}", ".logo-emblem svg{width:38px;height:38px;animation:spinC 8s linear infinite}\n@keyframes spinC{to{transform:rotate(360deg)}}")

# 3 & 7. Mood cards unique glows + pulse
html = html.replace(".mood-pill.on{border-color:var(--clay); background:rgba(194,113,79,.12)}", 
                    ".mood-pill.on{border-color:var(--g,var(--clay)); background:rgba(194,113,79,.12); transform:scale(1.05); box-shadow:0 0 20px rgba(0,0,0,0.4), inset 0 0 10px var(--g,var(--clay));}")

html = html.replace("transition:all .2s; user-select:none;", "transition:transform 0.3s ease, box-shadow 0.3s ease; user-select:none;\n}")
html = html.replace(".mood-pill:active{transform:scale(.95)}", ".mood-pill:hover{transform:translateY(-4px); box-shadow:0 8px 16px var(--g,rgba(255,255,255,0.05));}\n.mood-pill:active{transform:scale(.95)}")
pulse_anim = """
@keyframes pulseSelect{ 0%{transform:scale(1)} 50%{transform:scale(1.05)} 100%{transform:scale(1)} }
.mood-pill.pulse{animation:pulseSelect 0.3s ease-out;}
"""
html = html.replace(".mood-pill-ico{font-size:26px}", pulse_anim + ".mood-pill-ico{font-size:26px}")

# Add inline styles for the distinct glows to the elements directly
html = html.replace("""<div class="mood-pill on" onclick="pickMood(this,'Chill')">""", """<div class="mood-pill on" style="--g:#4FC3F7;" onclick="pickMood(this,'Chill')">""")
html = html.replace("""<div class="mood-pill" onclick="pickMood(this,'Adventure')">""", """<div class="mood-pill" style="--g:#81C784;" onclick="pickMood(this,'Adventure')">""")
html = html.replace("""<div class="mood-pill" onclick="pickMood(this,'Peace')">""", """<div class="mood-pill" style="--g:#A5D6A7;" onclick="pickMood(this,'Peace')">""")
html = html.replace("""<div class="mood-pill" onclick="pickMood(this,'Culture')">""", """<div class="mood-pill" style="--g:#FFB74D;" onclick="pickMood(this,'Culture')">""")
html = html.replace("""<div class="mood-pill" onclick="pickMood(this,'Romance')">""", """<div class="mood-pill" style="--g:#F48FB1;" onclick="pickMood(this,'Romance')">""")
html = html.replace("""<div class="mood-pill" onclick="pickMood(this,'Spiritual')">""", """<div class="mood-pill" style="--g:#CE93D8;" onclick="pickMood(this,'Spiritual')">""")

# And JS pulse adding
html = html.replace("el.classList.add('on'); mood=m;", "el.classList.add('on'); el.classList.add('pulse'); setTimeout(()=>el.classList.remove('pulse'),300); mood=m;")

# 8. Budget Number Animation
budget_js = """
let bAnim=null;
function onBudget(el) {
  budget=parseInt(el.value);
  const pct=((budget-1000)/24000)*100;
  el.style.setProperty('--pct',pct+'%');
  const bn=document.getElementById('budgetNum');
  const start=parseInt(bn.textContent.replace(/,/g,''))||budget;
  const target=budget;
  const t0=performance.now();
  if(bAnim) cancelAnimationFrame(bAnim);
  function step(t) {
    let p=Math.min((t-t0)/300,1);
    let e = 1-Math.pow(1-p,3);
    bn.textContent=Math.round(start+(target-start)*e).toLocaleString('en-IN');
    if(p<1) bAnim=requestAnimationFrame(step);
  }
  bAnim=requestAnimationFrame(step);
}
"""
html = re.sub(r'function onBudget\(el\) \{[\s\S]*?\}', budget_js, html)

# 11. Reveal page Loading State
loading_html_old = """    <div class="route-anim">
      <svg class="route-svg" viewBox="0 0 260 140">
        <defs>
          <filter id="gf"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
        </defs>
        <!-- Background map grid -->
        <rect width="260" height="140" fill="none"/>
        <line x1="0" y1="70" x2="260" y2="70" stroke="rgba(194,113,79,.08)" stroke-width="1" stroke-dasharray="4 4"/>
        <line x1="130" y1="0" x2="130" y2="140" stroke="rgba(194,113,79,.08)" stroke-width="1" stroke-dasharray="4 4"/>
        <!-- Route path -->
        <path class="route-path" d="M30,110 Q80,40 130,70 Q180,100 230,30" filter="url(#gf)"/>
        <!-- Destination dots -->
        <circle class="route-dot a" cx="30" cy="110" r="5" filter="url(#gf)"/>
        <circle class="route-dot b" cx="130" cy="70" r="5" filter="url(#gf)"/>
        <circle class="route-dot c" cx="230" cy="30" r="5" filter="url(#gf)"/>
        <!-- Labels -->
        <text x="30" y="128" text-anchor="middle" fill="rgba(194,113,79,.5)" font-size="9" font-family="Nunito,sans-serif">You</text>
        <text x="130" y="88" text-anchor="middle" fill="rgba(194,113,79,.4)" font-size="9" font-family="Nunito,sans-serif">?</text>
        <text x="230" y="20" text-anchor="middle" fill="rgba(194,113,79,.6)" font-size="9" font-family="Nunito,sans-serif">Dest</text>
      </svg>
      <div class="plane-travel">✈️</div>
    </div>"""

loading_html_new = """    <div class="route-anim" style="display:flex; justify-content:center; align-items:center;">
      <div class="particle-dust"></div>
      <div style="font-size:64px; animation:spinC 3s linear infinite; filter:drop-shadow(0 0 15px rgba(194,113,79,0.5));">🧭</div>
      <style>
        .particle-dust { position:absolute; inset:-50px; background-image:radial-gradient(circle, #E8C99A 1.5px, transparent 1.5px); background-size:25px 25px; opacity:0.3; animation:dustMove 15s linear infinite; pointer-events:none;}
        @keyframes dustMove { 100% { background-position:50px -50px; transform:rotate(15deg); } }
      </style>
    </div>"""
html = html.replace(loading_html_old, loading_html_new)
html = html.replace('id="lPhase">Scanning hidden gems...', 'id="lPhase" style="font-style:italic;">The oracle is searching...')


# 12 & 13: Reveal Page restructuring
hero_css_old = """.hero-grad{
  position:absolute; inset:0;
  background-size:cover; background-position:center;
  animation:heroZoom 12s ease-out both;
}"""
hero_css_new = """.hero-grad{
  position:absolute; inset:0;
  background-size:cover; background-position:center;
  background-image:url('https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&q=80') !important;
  animation:heroZoom 12s ease-out both;
}"""
html = html.replace(hero_css_old, hero_css_new)
html = html.replace("height:48vh; min-height:240px;", "height:40vh; min-height:240px;")
html = html.replace(".reveal-body{\n  padding:20px 16px 28px;", ".reveal-body{\n  padding:30px 20px 28px;\n  margin-top:-15vh;\n  position:relative;\n  z-index:10;\n  background:rgba(28,20,16,0.7);\n  backdrop-filter:blur(12px);\n  -webkit-backdrop-filter:blur(12px);\n  border-radius:24px 24px 0 0;\n  box-shadow:0 -10px 40px rgba(0,0,0,0.5);")

hero_content_old = """    <div class="hero-content">
      <div class="hero-badges">
        <span class="hero-badge hb-mood" id="heroBadgeMood">Peace</span>
        <span class="hero-badge hb-dur" id="heroBadgeDur">3 Days</span>
      </div>
      <div class="hero-dest serif" id="heroDest">Vagamon</div>
      <div class="hero-state" id="heroState">Kerala, India</div>
      <div class="hero-tagline serif" id="heroTagline">"Where mist is the morning prayer"</div>
    </div>"""
html = html.replace(hero_content_old, "")

reveal_body_head = """  <div class="reveal-body">

    <!-- Moved content to frosted glass -->
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
      <div>
        <div class="hero-dest serif" id="heroDest" style="font-size:2.5rem; color:var(--clay); line-height:1.1; margin-bottom:4px; opacity:1; animation:none; text-shadow:none; letter-spacing:0;"></div>
        <div class="hero-tagline serif" id="heroTagline" style="font-size:15px; color:var(--sand); opacity:1; animation:none; margin:0;"></div>
      </div>
      <div id="heroBadgeMood" style="background:var(--sage); color:#fff; padding:6px 14px; border-radius:20px; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:1px; flex-shrink:0; white-space:nowrap;">Budget Fit</div>
    </div>

    <!-- Hidden gem & Reasons -->
    <div style="margin-bottom:20px;">
      <h3 style="font-size:16px; color:var(--sand); margin-bottom:10px;">Three reasons it's yours</h3>
      <div id="threeReasons" style="font-size:13px; color:var(--t2); line-height:1.6; padding-left:16px; display:flex; flex-direction:column; gap:8px;"></div>
    </div>

    <div style="border:1px solid rgba(206,147,216,0.25); background:rgba(206,147,216,0.06); border-radius:12px; padding:16px; margin-bottom:24px;">
      <div style="color:#CE93D8; font-weight:700; font-size:12px; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">🔮 Hidden Gem</div>
      <div id="hiddenGem" style="font-size:13px; color:var(--t1); line-height:1.5;"></div>
    </div>"""

html = html.replace('  <div class="reveal-body">', reveal_body_head)

# Dest reveal typing effect JS
reveal_js = """function goReveal() {
  if(cdTimer) clearInterval(cdTimer);
  const d=dest;
  document.getElementById('heroTagline').textContent=d.tagline;
  document.getElementById('heroBadgeMood').textContent=mood + ' Fit';
  document.getElementById('budgetTag').textContent='₹'+budget.toLocaleString('en-IN');
  document.getElementById('mapName').textContent=d.name.toUpperCase();
  
  // typewriter
  const elD = document.getElementById('heroDest');
  elD.textContent='';
  let idx=0;
  const nm=d.name;
  const iv = setInterval(()=>{
    if(idx<nm.length) { elD.textContent+=nm[idx]; idx++; }
    else clearInterval(iv);
  }, 40);

  // Hidden gem and Three reasons
  document.getElementById('hiddenGem').innerHTML = d.hints[d.hints.length-1].t;
  document.getElementById('threeReasons').innerHTML = d.hints.slice(0,3).map((h,i)=>`<div>✨ ${h.t}</div>`).join('');
"""
html = html.replace("""function goReveal() {
  if(cdTimer) clearInterval(cdTimer);
  const d=dest;

  document.getElementById('heroGrad').style.background=d.bg;
  document.getElementById('heroDest').textContent=d.name;
  document.getElementById('heroState').textContent=d.state+', India';
  document.getElementById('heroTagline').textContent=d.tagline;
  document.getElementById('heroBadgeMood').textContent=mood;
  document.getElementById('heroBadgeDur').textContent=dur;
  document.getElementById('budgetTag').textContent='₹'+budget.toLocaleString('en-IN');
  document.getElementById('mapName').textContent=d.name.toUpperCase();""", reveal_js)

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully.")
