# Yatr — Mystery Travel India 🧭

> *Tell us your mood. We'll craft a mystery journey through hidden India.*

Yatr is a single-file mobile-first web app that generates AI-powered mystery travel itineraries across India. Users pick a mood, budget, and travel style — and an AI-curated destination is revealed with a full day plan, budget breakdown, food guide, and travel notes.

---

## Features

- **Mood-based discovery** — 6 moods (Chill, Adventure, Peace, Culture, Romance, Spiritual)
- **AI travel notes** — calls the Anthropic Claude API to generate a unique, poetic travel note for each destination
- **Mystery reveal flow** — destination stays sealed behind a 24-hour countdown, with cryptic clues
- **Full itinerary** — day-by-day plan, budget bars, experiences, food guide, and a local map
- **Save & reroll** — save trips to localStorage, reroll for a different destination
- **Share** — native share sheet or clipboard copy with a mystery teaser
- **Single HTML file** — zero build step, zero dependencies, runs anywhere

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/gayathrisanthoshpc/yatr.git
cd yatr

# Open directly in browser — no server needed
open index.html

# Or serve locally for Anthropic API calls (avoids CORS on some browsers)
npx serve .
# → http://localhost:3000
```

---

## Anthropic API Setup

Yatr calls `https://api.anthropic.com/v1/messages` to generate personalised travel notes.

**If using in a browser directly**, you need to proxy the API key — never expose it in client-side code.

```
Recommended: run a lightweight proxy (e.g. with Cloudflare Workers or Vercel Edge Functions)
that injects the Authorization header server-side.
```

If you're hosting via a backend that injects the key, no changes are needed. The fetch call in `goLoad()` already formats the request correctly.

**Model used:** `claude-sonnet-4-20250514`

---

## Project Structure

```
yatr/
└── index.html          # Entire app — HTML, CSS, JS in one file
    ├── Splash screen
    ├── Discover (home form)
    ├── Loading (AI call + progress)
    ├── Mystery (sealed destination + hints)
    ├── Reveal (full itinerary)
    └── Saved trips
```

---

## Destination Database

Destinations live in the `DB` object in the `<script>` section, keyed by mood:

```js
const DB = {
  Chill:     [ { name, state, tagline, hints, budget, days, acts, food, notes, ... } ],
  Adventure: [ ... ],
  Peace:     [ ... ],
  Culture:   [ ... ],
  Romance:   [ ... ],
  Spiritual: [ ... ]
}
```

Each destination includes:
| Field | Description |
|-------|-------------|
| `name` / `state` | Place name and Indian state |
| `tagline` | One-line poetic descriptor |
| `bg` | CSS gradient for card backgrounds |
| `emoji` | Destination emoji |
| `hints` | 3 mystery clues shown before reveal |
| `budget` | Array of cost line items with percentages |
| `days` | Time-stamped day plan |
| `acts` | 4 recommended experiences |
| `food` | 4 recommended eateries |
| `notes` | Static fallback travel notes (used if AI call fails) |

---

## Known Issues & Suggested Improvements

### High Priority

| # | Issue | Fix |
|---|-------|-----|
| 1 | Budget not used in destination selection | Add `minBudget`/`maxBudget` per destination; filter `pickDest()` |
| 2 | Season preference ignored | Add a `seasons` array per destination; filter on `pickDest()` |
| 3 | Hardcoded hero image on reveal page | Map an Unsplash photo URL per destination in the DB |
| 4 | `openSaved()` name collision | Store the full destination object in the saved record |
| 5 | API key exposed in client | Add a lightweight server-side proxy to inject the `x-api-key` header |

### Medium Priority

| # | Issue | Fix |
|---|-------|-----|
| 6 | Loading screen waits full 4.8s regardless of AI speed | Resolve transition on `Promise.all([aiCall, minDelay(2000)])` |
| 7 | Only ~12 destinations — reroll fatigue | Add 20+ destinations across Northeast, Ladakh, Odisha, Telangana, Andaman |
| 8 | No keyboard / accessibility support | Add `aria-label`, `role="button"`, and focus styles to mood pills and chips |
| 9 | No PWA support | Add `manifest.json` + service worker for home screen install |
| 10 | Share produces plain text | Use Canvas API to render a visual share card |

### Low Priority

| # | Issue | Fix |
|---|-------|-----|
| 11 | AI error shows no message | Add a styled fallback state in the AI box |
| 12 | Countdown resets every reroll | Persist countdown start time in `sessionStorage` |
| 13 | No onboarding for first-time users | Add a one-time tooltip on the mood row |

---

## Customisation

### Adding a Destination

```js
DB.Peace.push({
  name: 'Majuli',
  state: 'Assam',
  tagline: '"The world\'s largest river island, slowly disappearing"',
  bg: 'linear-gradient(160deg,#0A1A10 0%,#2A5A38 50%,#7AAA72 100%)',
  emoji: '🏝️',
  hints: [
    { i: '🏝️', t: 'This island shrinks every monsoon — it may vanish in 30 years.' },
    { i: '🎭', t: 'Home to the Sattriya dance, a 600-year-old classical tradition.' },
    { i: '🐦', t: 'Over 200 migratory bird species land here each winter.' }
  ],
  budget: [ /* ... */ ],
  days:   [ /* ... */ ],
  acts:   [ /* ... */ ],
  food:   [ /* ... */ ],
  notes:  '...'
});
```

### Changing Moods

Edit the mood pill row in the HTML and add a matching key to `DB`:

```html
<div class="mood-pill" style="--glow:rgba(255,200,100,0.5);" onclick="pickMood(this,'Festival')">
  <span class="mood-pill-ico">🎊</span>
  <span class="mood-pill-name">Festival</span>
</div>
```

```js
DB.Festival = [ { name: 'Pushkar', ... } ];
```

---

## Tech Stack

| Layer | Choice |
|-------|--------|
| UI | Vanilla HTML/CSS/JS — no framework |
| Fonts | Cormorant Garamond (display) + DM Sans (body) via Google Fonts |
| AI | Anthropic Claude (`claude-sonnet-4-20250514`) |
| Storage | `localStorage` for saved trips |
| Hosting | Any static host — GitHub Pages, Netlify, Vercel, Cloudflare Pages |

---

## Deploying

### Netlify (one command)
```bash
npx netlify deploy --prod --dir .
```

### GitHub Pages
Push to `main`, enable Pages in repo settings, set source to `/root`.

### Vercel
```bash
npx vercel --prod
```

---

## License

MIT — use it, fork it, send people to hidden India.

---

*Built with ☕ and a deep love for underrated India.*