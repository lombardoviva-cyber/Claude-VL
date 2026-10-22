# What counts as a signal

A signal is a concrete, dated event that suggests something may be changing in
the industry in `config/radar.yaml`. Headlines that restate what everyone
already knows are not signals.

## Keep

- Something new happened: a launch, a funding round, a paper, a policy, a hire,
  a pricing change, a platform rule change.
- Unusual behaviour: users, buyers or creators doing something in a new way,
  especially when it shows up in more than one place.
- Something at the edge: a small player, a niche community, or an adjacent
  industry trying something the mainstream has not.
- A contrarian data point that cuts against an existing trend.

## Drop (mark as Noise or skip)

- Opinion pieces and predictions with no new fact behind them.
- Coverage of a story already logged (same event, different outlet).
  Instead, raise the strength of the existing signal by 1 if the new outlet
  adds real confirmation.
- Routine updates: minor version bumps, earnings that match expectations,
  partnership announcements with no product.
- Anything you cannot tie back to a URL.

## Strength (1-5)

Start at 2 and adjust:

| Adjust | When |
|--------|------|
| +1 | Hard evidence: money moved, a product shipped, a rule was enacted, data was published |
| +1 | Source `weight` is 3 |
| +1 | It is the second or later independent sighting of the same idea this month |
| +1 | It comes from outside the usual players (new entrant, niche community, adjacent industry) |
| -1 | Source `weight` is 1 and there is no hard evidence |
| -1 | Speculative: announced, rumoured or "plans to" |

Clamp to 1-5. A 5 should be rare: a few per month at most.

## Writing the row

- **Signal**: what happened, plainly. "Canva adds AI video avatars to free plan."
  Not "Canva is changing video forever."
- **Why it matters**: the change it might point to, hedged honestly.
  "Avatar video may become a default feature rather than a paid product."
