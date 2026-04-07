import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

fixes = """
/* —— INJECTED REFINEMENTS & USER FIXES —— */

/* 1. Start My Journey Button */
.btn-primary {
  background: var(--grad-button) !important;
  color: var(--t1) !important;
  border: none !important;
  padding: 16px 40px !important;
  border-radius: 50px !important;
  font-size: 1rem !important;
  letter-spacing: 0.05em !important;
  cursor: pointer !important;
}

/* 2. Compass icon on landing page */
.logo-emblem {
  background: var(--grad-button) !important;
  border-radius: var(--radius-md) !important;
  padding: 12px !important;
  width: auto !important;
  height: auto !important;
  display: inline-flex !important;
}

/* 3. Mood cards selected state */
.mood-pill.on {
  border: 1px solid var(--glow, var(--clay)) !important;
  transform: scale(1.05) !important;
  box-shadow: 0 0 20px var(--glow, var(--clay)) !important;
}

/* 4. Landing feature cards */
.splash-card {
  border: 1px solid var(--b1) !important;
  border-left: 3px solid var(--clay) !important;
  background: rgba(46, 28, 20, 0.6) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  overflow: hidden;
}
"""

if "INJECTED REFINEMENTS" not in text:
    text = text.replace('</style>', fixes + '\n</style>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully patched index.html with the 4 fixes.")
else:
    print("Already refined.")
