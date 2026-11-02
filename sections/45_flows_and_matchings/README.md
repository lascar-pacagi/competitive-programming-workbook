# Section 45: Flows and Matchings

Start with A-C to implement and inspect the algorithms. Attempt D from its
standalone statement before opening the editorial. E-N form a second track:
ten original modeling problems, intended to be attempted in order.

| Problem | Title | Indicative difficulty |
| --- | --- | --- |
| E | [Separated Light Marks](problems/e_separated_light_marks/README.md) | 1400 |
| F | [Crate Routing](problems/f_crate_routing/README.md) | 1500 |
| G | [Silent Rehearsal](problems/g_silent_rehearsal/README.md) | 1700 |
| H | [Emergency Corridors](problems/h_emergency_corridors/README.md) | 1800 |
| I | [Directional Relay Modes](problems/i_directional_relay_modes/README.md) | 2000 |
| J | [Exhibit Pacts](problems/j_exhibit_pacts/README.md) | 2100 |
| K | [Quota Manifests](problems/k_quota_manifests/README.md) | 2200 |
| L | [Calendar Reinforcement](problems/l_calendar_reinforcement/README.md) | 2300 |
| M | [Resilient Reservations](problems/m_resilient_reservations/README.md) | 2400 |
| N | [Signal Concentration](problems/n_signal_concentration/README.md) | 2500 |

These are author estimates on a Codeforces-like scale, not official ratings.
The difficulty comes mainly from finding and proving the model. The statements
do not identify the reduction. Each editorial gives the construction, a proof,
a sample trace, complete C++ and Python solutions, and targeted tests.

The lesson includes reusable C++ and Python implementations and a short primer
on the extra mathematical tools used in the advanced track. Open
[the interactive laboratory](flow_playground/index.html) to step through flow
and matching searches on a custom graph. It also works offline.

Run all reference solutions:

```bash
CP_TARGET=solution python3 sections/45_flows_and_matchings/check.py --keep-going
```

Select one exercise with `--problem e --lang cpp`, or a range by listing letters:
`--problem k,l,m,n`. Public `solve.*` files remain TODO stubs; use the private
submissions overlay for your own attempts.
