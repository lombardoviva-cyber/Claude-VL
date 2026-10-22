# Trend Radar

A trend forecasting system that runs in Claude. Every day it reads your sources,
pulls out early signals, logs each one to a Notion database, then groups related
signals into bigger trends and tracks which ones are gaining momentum and which
are fading. Once a week it turns the strongest trends into a carousel.

```
sources ──► signals ──► trends ──► momentum ──► weekly carousel
 (daily)    (Notion)    (Notion)   (scored)     (output/*.md)
```

Reading headlines doesn't connect anything. The radar keeps a running record so
that a small launch on Tuesday and a funding round three weeks later end up
under the same trend, and you can see the pattern build.

## What's in here

| Path | What it is |
|------|------------|
| `.claude/skills/trend-radar/SKILL.md` | The skill: setup, daily scan, weekly carousel, report |
| `.claude/skills/trend-radar/references/notion-schema.md` | Signals and Trends database properties and views |
| `.claude/skills/trend-radar/references/signal-rubric.md` | What counts as a signal, and how to rate strength 1-5 |
| `.claude/skills/trend-radar/references/momentum.md` | Clustering rules and the momentum / confidence formulas |
| `.claude/skills/trend-radar/references/weekly-carousel.md` | The 8-slide carousel template |
| `config/radar.yaml` | Your industry, audience, thresholds, and Notion IDs |
| `config/sources.yaml` | The feeds, sites, searches and newsletters to scan |

## Setup guide

### 1. Connect your tools

In Claude (claude.ai, Claude Code or Cowork), connect:

- **Notion** (required): where signals and trends live.
- **Gmail** (optional): to read newsletters as a source.
- Web fetch / search is built in.

### 2. Tell it what you're watching

Edit `config/radar.yaml`: set `industry`, `audience` and `adjacent_topics`.
The more specific the industry, the better the signals.

### 3. Pick your sources

Edit `config/sources.yaml`. Aim for 10-20 sources, mixed across four kinds:

- **Mainstream** (big newsletters, trade press): low surprise, high reliability.
- **Edge** (niche subreddits, indie hackers, small Substacks): where things start.
- **Hard evidence** (funding trackers, changelogs, job boards, regulators).
- **Adjacent industries**: trends often arrive from next door.

Give each a `weight` from 1 to 3 for how much you trust it.

### 4. Create the Notion databases

Run:

```
/trend-radar setup
```

It creates a **Trends** and a **Signals** database with the right properties,
relations and views, and writes their IDs into `config/radar.yaml`.

### 5. Run it daily

```
/trend-radar scan
```

Run it once by hand and check the Signals inbox. If it logs too much noise,
raise `scan.min_strength` or trim sources; if it logs too little, add edge sources.

Then schedule it so it runs without you: a Claude Code scheduled task, or
`/loop 1d /trend-radar scan` in an open session.

### 6. Weekly carousel

```
/trend-radar weekly
```

Writes `output/carousel-YYYY-MM-DD.md`: 8 slides covering the lead trend, two
more risers, one fading trend, and an action for your audience. Paste into your
design tool, or ask Claude to build it in Canva or Gamma if connected.

### Anytime

```
/trend-radar report
```

Read-only view of the radar: trends by momentum, with early bets called out.

## How momentum works

Every signal gets a strength from 1 to 5. For each trend, the radar sums the
strength of its signals in the last 14 days (**recent**) and in the 14 days
before that (**prior**):

- **Emerging**: first seen in the last 14 days
- **Accelerating**: recent ≥ 1.5× prior, and at least 6
- **Cooling**: recent ≤ 0.5× prior, or nothing recent
- **Steady**: anything in between
- **Dormant**: no new signal in 45 days

Confidence (Low / Medium / High) is tracked separately, based on how many signals
and independent sources back the trend. Full rules in
`.claude/skills/trend-radar/references/momentum.md`.
