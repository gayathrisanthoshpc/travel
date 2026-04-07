import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_injection = """
/* —— INJECTED DESKTOP & PREMIUM GLASSMORPHISM THEME —— */
body {
  background-color: #0D0A08 !important;
  background-image: 
    radial-gradient(ellipse at top, rgba(200, 100, 60, 0.25), transparent 70%),
    url('https://images.unsplash.com/photo-1543387807-77fb7cfb9195?q=80&w=2400&auto=format&fit=crop') !important;
  background-size: cover !important;
  background-position: center !important;
  background-attachment: fixed !important;
}
body::after {
  content: ""; position: fixed; inset: 0;
  background: rgba(20, 14, 10, 0.70);
  backdrop-filter: blur(40px);
  -webkit-backdrop-filter: blur(40px);
  z-index: -1; pointer-events: none;
}

/* Glassmorphism for Blocks & Cards */
.form-block, .seal-card, .ticket, .hint-card, .trip-card, .share-row, .info-block {
  background: rgba(30, 22, 18, 0.45) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(242, 235, 224, 0.08) !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25) !important;
}
.seal-bottom, .tc-foot, .ib-head, .ticket-head {
  background: rgba(0,0,0,0.25) !important;
  border-bottom: 1px solid rgba(255,255,255,0.05) !important;
  border-top: 1px solid rgba(255,255,255,0.05) !important;
}
.mood-pill {
  background: rgba(30, 22, 18, 0.45) !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
}

/* Centering responsive max-width */
.home-top, .mood-scroll-wrap, .form-body, .cta-wrap, 
.mystery-inner, .reveal-body, .saved-grid, 
.saved-h-row, .reveal-hero {
  max-width: 680px !important;
  margin-left: auto !important;
  margin-right: auto !important;
  width: 100% !important;
}
#p-home > div:nth-child(2) {
  max-width: 680px !important;
  margin-left: auto !important;
  margin-right: auto !important;
}

.reveal-hero {
  border-radius: 0 0 32px 32px;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}

/* LAPTOP / DESKTOP OPTIMIZATIONS */
@media (min-width: 720px) {
  #nav {
    max-width: 480px;
    margin: 0 auto;
    border-radius: 36px;
    bottom: 30px;
    background: rgba(28, 20, 16, 0.75) !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    box-shadow: 0 16px 50px rgba(0,0,0,0.6) !important;
    height: 72px !important;
  }
  .pane {
    padding-bottom: 140px !important;
  }
  
  /* Home View Lap Optimizations */
  .home-top {
    border-radius: 32px;
    margin-top: 40px;
    padding: 60px 40px 40px !important;
    text-align: center;
    background: rgba(40, 28, 22, 0.3) !important;
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  }
  .compass-watermark {
    left: 50%;
    transform: translateX(-50%);
    top: -20px;
    right: auto;
    opacity: 0.08;
    width: 240px;
    height: 240px;
  }
  .home-h {
    font-size: 52px !important;
  }
  .greeting {
    font-size: 15px; margin-bottom: 12px;
  }
  .home-sub {
    font-size: 15px; margin-top: 12px;
  }
  
  .mood-scroll-wrap {
    overflow: visible !important;
  }
  .mood-row {
    flex-wrap: wrap;
    justify-content: center;
    padding: 10px 0;
  }
  .mood-pill {
    min-width: 90px !important;
    padding: 20px 14px !important;
  }
  .mood-pill-ico {
    font-size: 30px !important;
  }
  .mood-pill-name {
    font-size: 12px !important;
  }
  
  /* Form Grid */
  .form-body {
    display: grid !important;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }
  .form-block {
    height: 100%;
  }
  .form-block:nth-child(1) {
    grid-column: 1 / -1; /* Budget takes full width */
  }
  .cta-wrap {
    margin-top: 24px;
    margin-bottom: 40px;
  }
  .btn-primary {
    font-size: 16px !important;
    padding: 20px !important;
  }
  
  /* Reveal Hero tweaks */
  .reveal-hero {
    height: 48vh !important;
    margin-top: 20px;
    border-radius: 32px;
  }
  .reveal-body {
    margin-top: -10vh !important;
    padding: 40px 32px !important;
    border: 1px solid rgba(255,255,255,0.06);
  }
  
  /* Splash desktop */
  .splash-content {
    max-width: 500px !important;
  }
  .splash-card {
    padding: 20px;
    font-size: 15px;
    border-radius: 20px;
  }
  .sc-ico {
    font-size: 32px;
  }
  .logo-name {
    font-size: 56px !important;
  }
}
"""

if "INJECTED DESKTOP" not in html:
    html = html.replace('</style>', css_injection + '\n</style>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Injected responsive CSS correctly.")
else:
    print("CSS already injected.")
