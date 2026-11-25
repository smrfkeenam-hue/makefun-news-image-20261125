# AGENT.md — news-image-20261125

Entry for "Sum up 25 November's world news in one image" ($100, top 50).

## What the image is
A 1024x1024 newspaper front page, drawn with Python PIL (DejaVu fonts),
masthead "WEDNESDAY — 25 NOVEMBER 2026" plus six panels, each with a simple
drawn icon, a headline and one factual caption. No photographs, no copied
artwork, all original drawing and text.

## Stories chosen (all reported on 25 Nov 2026, verified by web search)
- US PCE + Q3 GDP due 25 Nov 21:30 WITA (8:30 ET), the Fed's last inflation
  read before the 9 Dec decision; Dec 25bp hike ~90-97% priced (CME).
  Framed as "due today" — no forecast presented as an actual result.
- Zelenskyy confirms Ukraine's drone strikes on a Russian cargo ship in the
  Gulf of Finland and on Russian vessels off Benghazi, Libya (Reuters/RFE).
- COP31 climate summit in Antalya ends without a final agreement after
  oil/gas producers block fossil-fuel phaseout language.
- Nvidia founder Jensen Huang reinstated as CEO; shares +31.5% on Monday,
  ~$1T market value regained (Forbes/ATFX).
- Gold ~$3,550 and Bitcoin below $60,000 after Tuesday's slide; record
  November ETF outflows (checked against live market data 25 Nov morning).
- Thanksgiving eve: Trump pardons turkeys Freedom and Feathers (Reuters).

## Build
- `entry.png` drawn by /tmp/draw_newsimg20261125.py (PIL), 1024x1024.
- `main.py` stdlib-only: copies entry.png to MAKEFUN_OUTPUT_DIR/entry.png.
- Verified locally: run main.py, output byte-identical to entry.png.
