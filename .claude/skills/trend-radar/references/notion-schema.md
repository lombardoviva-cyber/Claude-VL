# Notion schema

Two databases under one parent page. `/trend-radar setup` creates them; this file
is the source of truth for their properties.

## Signals

One row per early signal: a single observable fact that hints at change.

| Property      | Type         | Values / notes |
|---------------|--------------|----------------|
| Signal        | Title        | One sentence stating what happened, not why it matters |
| Date seen     | Date         | Date the scan found it |
| Source        | Select       | Source `name` from `config/sources.yaml` |
| URL           | URL          | Link to the original item |
| Type          | Select       | Product launch, Funding, Research, Regulation, Behaviour shift, Hiring, Platform change, Opinion |
| Strength      | Number       | 1-5, see `signal-rubric.md` |
| Why it matters| Text         | One or two sentences: the change this could point to |
| Trend         | Relation     | → Trends (zero or one) |
| Status        | Select       | New, Clustered, Unclustered, Noise |
| Fingerprint   | Text         | Lower-case canonical URL, used to skip duplicates |

## Trends

One row per larger pattern that two or more signals point to.

| Property        | Type     | Values / notes |
|-----------------|----------|----------------|
| Trend           | Title    | Short name, 3-6 words, e.g. "Agents replace SaaS dashboards" |
| Thesis          | Text     | What is changing and where it leads, 2-3 sentences |
| Signals         | Relation | ← Signals.Trend (two-way) |
| Signal count    | Rollup   | Count of Signals |
| First seen      | Date     | Date of the oldest linked signal |
| Last seen       | Date     | Date of the newest linked signal |
| Recent score    | Number   | Sum of Strength over the last window (see `momentum.md`) |
| Prior score     | Number   | Sum of Strength over the window before that |
| Momentum        | Select   | Emerging, Accelerating, Steady, Cooling, Dormant |
| Horizon         | Select   | Now (0-6 mo), Next (6-18 mo), Later (18 mo+) |
| Confidence      | Select   | Low, Medium, High |
| Last reviewed   | Date     | Last scan that updated this row |

## Suggested views

- Signals → **Inbox**: Status = New or Unclustered, sorted by Strength desc.
- Trends → **Radar**: board grouped by Momentum.
- Trends → **This week**: Last seen within the past 7 days, sorted by Recent score desc.
  The weekly carousel is built from this view.
