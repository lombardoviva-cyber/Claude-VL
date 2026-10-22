# Clustering and momentum

## Clustering signals into trends

After logging new signals, assign each one to a trend:

1. Read every trend that is not Dormant (name and thesis).
2. For each new signal, ask: does this signal give evidence for, or against,
   one of these theses? If yes, link it. A signal links to at most one trend:
   pick the closest.
3. Signals with no fitting trend stay `Unclustered`. Look at all unclustered
   signals from the last 30 days together. When two or more from different
   sources point to the same underlying change, create a new trend for them.
   One signal alone is never a trend.
4. If a trend's linked signals have drifted away from its thesis, rewrite the
   thesis rather than forcing new signals to fit the old wording.
5. If two trends describe the same change, merge them: move signals to the
   older trend, mark the other Dormant and note "Merged into <name>" in its thesis.

## Momentum

For each trend touched this run, and for every non-Dormant trend once a week:

- `W` = `momentum.window_days` from `config/radar.yaml` (default 14).
- **Recent score** = sum of Strength of linked signals dated in the last `W` days.
- **Prior score** = sum of Strength of linked signals dated `W` to `2W` days ago.

Set Momentum with the first rule that matches:

| Momentum      | Rule |
|---------------|------|
| Dormant       | No linked signal in the last `dormant_after_days` |
| Emerging      | First seen within the last `W` days |
| Accelerating  | Recent ≥ 1.5 × Prior and Recent ≥ 6 |
| Cooling       | Recent ≤ 0.5 × Prior, or Recent = 0 |
| Steady        | Anything else |

## Confidence

- **High**: 6+ signals from 3+ different sources, at least two with Strength ≥ 4.
- **Medium**: 3+ signals from 2+ sources.
- **Low**: everything else.

Momentum says how fast a trend is moving; confidence says how sure you are it
is real. Report both. An Accelerating trend with Low confidence is the
interesting early bet, so call it out.
