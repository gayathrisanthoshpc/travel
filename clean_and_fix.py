import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove all previously injected styles
text = re.sub(
    r'/\*\s*—— INJECTED DESKTOP.*?<\/style>',
    '</style>',
    text,
    flags=re.DOTALL
)
text = re.sub(
    r'/\*\s*—— INJECTED REFINEMENTS.*?<\/style>',
    '</style>',
    text,
    flags=re.DOTALL
)
# Just in case there are multiple, repeat the substitution
text = re.sub(r'/\*\s*—— INJECTED .*?<\/style>', '</style>', text, flags=re.DOTALL)

optimized_css = """
/* —— MASTER RESPONSIVE & THEME FIX —— */

/* 1. Fast, performant ambient travel background without slow backdrop-filters */
body {
  background-color: var(--ink) !important;
  background-image: 
    linear-gradient(to bottom, rgba(13, 10, 8, 0.8), rgba(28, 20, 16, 0.9)),
    url('https://images.unsplash.com/photo-1543387807-77fb7cfb9195?q=80&w=1200&auto=format&fit=crop') !important;
  background-size: cover !important;
  background-position: center !important;
  background-attachment: fixed !important;
}
/* Revert the mystic night background safely */
body.reveal-page {
  background-image: var(--grad-reveal) !important;
  background-color: var(--mystic-bg) !important;
}

/* 2. Fix the user's specific requested styles seamlessly */
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

.logo-emblem {
  background: var(--grad-button) !important;
  border-radius: var(--radius-md) !important;
  padding: 12px !important;
  width: auto !important;
  height: auto !important;
  display: inline-flex !important;
}

.mood-pill.on {
  border: 1px solid var(--glow, var(--clay)) !important;
  transform: scale(1.05) !important;
  box-shadow: 0 0 20px var(--glow, var(--clay)) !important;
  background: rgba(30, 22, 18, 0.6) !important;
}

.splash-card {
  border: 1px solid var(--b1) !important;
  border-left: 3px solid var(--clay) !important;
  background: rgba(46, 28, 20, 0.5) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  overflow: hidden;
}

/* 3. Global performance optimization for glassmorphism */
.form-block, .seal-card, .ticket, .hint-card, .trip-card, .share-row, .info-block {
  background: rgba(30, 22, 18, 0.6) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
}

/* 4. Perfect Centered Laptop View (Like a beautiful iPhone app widget) */
@media (min-width: 600px) {
  .pane {
    max-width: 480px !important;
    left: 0;
    right: 0;
    margin: 0 auto;
    border-radius: 20px 20px 0 0;
    box-shadow: 0 0 50px rgba(0,0,0,0.5);
    background: rgba(28, 20, 16, 0.4);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.05);
    border-bottom: none;
    padding-bottom: 24px; /* remove bottom padding offset of nav on laptop */
    inset: 40px 0 calc(var(--nav-h) + 40px) 0 !important; /* Float in middle */
  }
  
  .pane.full {
    inset: 40px 0 40px 0 !important; /* Splash screen float */
    border-radius: 20px;
  }
  
  #nav {
    max-width: 480px !important;
    left: 0;
    right: 0;
    margin: 0 auto;
    bottom: 40px !important;
    border-radius: 0 0 20px 20px; /* Connect to pane */
    border: 1px solid rgba(255,255,255,0.05);
    border-top: 1px solid rgba(255,255,255,0.1);
    background: rgba(37, 28, 22, 0.8) !important;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
  }
  
  .compass-watermark {
    opacity: 0.1 !important;
  }
}
"""

text = text.replace('</style>', optimized_css + '\n</style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied safe performant CSS.")
