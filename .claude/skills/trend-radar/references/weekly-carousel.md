# Weekly carousel

Built from the Trends database. 8 slides, one idea per slide, short enough to
read on a phone.

## Pick the content

From the **This week** view (or the same filter: Last seen within 7 days):

- 1 trend with Momentum = Accelerating and the highest Recent score: the lead.
- 2 more Accelerating or Emerging trends.
- 1 Cooling trend, if any. People like to know what is fading.
- For each picked trend, its 1-2 strongest signals from this week, with links.

Never put a Low-confidence trend in the lead slot. Label it "early" if it appears.

## Slides

1. **Hook**: "4 trends moving in <industry> this week". One line, no more.
2. **Lead trend**: name + one-sentence thesis.
3. **Lead evidence**: 2 signals, each one short line.
4. **Trend 2**: name + thesis + 1 signal.
5. **Trend 3**: name + thesis + 1 signal.
6. **Fading**: the Cooling trend and why it is losing steam.
7. **What to do**: one practical action for the `audience` in `config/radar.yaml`.
8. **CTA**: "Comment RADAR for the guide" (or the user's own CTA).

Max ~25 words per slide. No jargon the audience would not use.

## Output

Write the slides as Markdown to `output/carousel-YYYY-MM-DD.md` with a
`## Slide N` heading each, plus a caption (under 150 words) and the source links
at the end. If the user has a design tool connected (Canva, Gamma) and asks for it,
build the visual carousel from this file.
