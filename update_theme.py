import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove font <link> tags
text = re.sub(
    r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*<link href="https://fonts\.googleapis\.com/css2[^"]+" rel="stylesheet">',
    '',
    text,
    flags=re.IGNORECASE | re.DOTALL
)

root_new = """@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=DM+Sans:wght@400;500&display=swap');

:root {
  /* BASE PALETTE */
  --clay:        #C2714F;   /* terracotta — primary brand color */
  --sand:        #E8BC99;   /* warm sand — highlights */
  --ember:       #A84A2A;   /* deep ember — hover states */
  --dusk:        #6B3A2A;   /* dusk brown — borders */
  --sage:        #4A7A5A;   /* sage green — success/budget badge */
  --fog:         #8BFABA0;  /* misty teal — subtle accents */
  --ivory:       #F2EBE0;   /* warm ivory — primary text */
  --ink:         #1C1410;   /* warm black — base background */
  --paper:       #2E1C14;   /* paper — card backgrounds */

  /* SURFACES */
  --s0:          #1C1410;
  --s1:          #251C16;
  --s2:          #2E2318;
  --s3:          #382A20;

  /* TEXT */
  --t1:          #F2EBE0;
  --t2:          rgba(242,235,224,0.65);
  --t3:          rgba(242,235,224,0.35);

  /* MOOD GLOWS */
  --glow-chill:      #4FC3F7;
  --glow-adventure:  #81C784;
  --glow-peace:      #A5D6A7;
  --glow-culture:    #FFB74D;
  --glow-romance:    #F48FB1;
  --glow-spiritual:  #CE93D8;

  /* MYSTIC NIGHT — reveal page only */
  --mystic-bg:       #0D0B1A;
  --mystic-s1:       #151228;
  --mystic-s2:       #1E1A38;
  --mystic-accent:   #B76E79;
  --mystic-glow:     #7B5EA7;
  --mystic-star:     #E8D5B7;
  --mystic-border:   rgba(183,110,121,0.3);

  /* GRADIENTS */
  --grad-hero:    radial-gradient(ellipse at top, #2C1810 0%, #1C1410 50%, #0D0A08 100%);
  --grad-reveal:  radial-gradient(ellipse at top, #1A1535 0%, #0D0B1A 60%, #080610 100%);
  --grad-card:    linear-gradient(135deg, #251C16 0%, #1C1410 100%);
  --grad-button:  linear-gradient(135deg, var(--clay) 0%, var(--ember) 100%);

  /* TYPOGRAPHY */
  --font-display: 'Cormorant Garamond', serif;
  --font-body:    'DM Sans', sans-serif;

  /* BORDER RADIUS */
  --radius-sm:   8px;
  --radius-md:   16px;
  --radius-lg:   24px;
  --radius-xl:   32px;
}

/* REVEAL PAGE THEME SWITCH */
body.reveal-page {
  background-image: var(--grad-reveal) !important;
  background-color: var(--mystic-bg) !important;
  --clay: var(--mystic-accent);
  --ink: var(--mystic-bg);
  --t1: var(--mystic-star);
}
body.reveal-page::after {
  content: none !important; /* Hide overlay/glass masking for mystic night */
}

h1, h2, h3, .brand-name, .destination-name { font-family: var(--font-display) !important; }
body, p, button, label, input, .chip, .text { font-family: var(--font-body); }
"""

# Replace existing :root up to --rf
if ":root{" in text:
    text = re.sub(r':root\s*\{[\s\S]*?--rf:\s*24px;\s*\}', root_new, text)

# Fonts hardcodes
text = text.replace("font-family:'Cormorant Garamond',serif", "font-family: var(--font-display)")
text = text.replace("font-family:'DM Sans',sans-serif", "font-family: var(--font-body)")
text = text.replace("font-family:'DM Sans',monospace", "font-family: var(--font-body)")

# Specific replacements
replaces = {
    "#C2714F": "var(--clay)",
    "#E8BC99": "var(--sand)",
    "#E8C99A": "var(--sand)", # Catch old version
    "#A84A2A": "var(--ember)",
    "#1C1410": "var(--ink)",
    "#4FC3F7": "var(--glow-chill)",
    "#81C784": "var(--glow-adventure)",
    "#A5D6A7": "var(--glow-peace)",
    "#FFB74D": "var(--glow-culture)",
    "#F48FB1": "var(--glow-romance)",
    "#CE93D8": "var(--glow-spiritual)",
    "linear-gradient(135deg, var(--clay) 0%, var(--ember) 100%)": "var(--grad-button)",
    
    # Border
    "border-radius:8px": "border-radius: var(--radius-sm)",
    "border-radius:10px": "border-radius: var(--radius-sm)",
    "border-radius:12px": "border-radius: var(--radius-md)",
    "border-radius:14px": "border-radius: var(--radius-md)",
    "border-radius:16px": "border-radius: var(--radius-md)",
    "border-radius:20px": "border-radius: var(--radius-lg)",
    "border-radius:24px": "border-radius: var(--radius-lg)",
    "border-radius:32px": "border-radius: var(--radius-xl)",
    "border-radius:36px": "border-radius: var(--radius-xl)",
    
    # Glows
    "--g:": "--glow:",
    "var(--g,": "var(--glow,"
}

for k, v in replaces.items():
    text = text.replace(k, v)

# Handle mystic JS toggles safely
if "document.body.classList.add('reveal-page');" not in text:
    text = text.replace("function goReveal() {", "function goReveal() {\n  document.body.classList.add('reveal-page');")

if "document.body.classList.remove('reveal-page');" not in text:
    text = text.replace("function nav(paneId, btnId) {", "function nav(paneId, btnId) {\n  if(paneId !== 'p-reveal') document.body.classList.remove('reveal-page');")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied strict color system, font variables, and Mystic Night theme switch!")
