# remo tables

[![CI](https://github.com/remo-rcm/tables/actions/workflows/ci.yaml/badge.svg)](https://github.com/remo-rcm/tables/actions/workflows/ci.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/remo-rcm/tables/main.svg)](https://results.pre-commit.ci/latest/github/remo-rcm/tables/main)

machine readable tables with data and meta info for the remo model.

You can read these tables directly using, e.g.,

```python
import pandas as pd

table = pd.read_csv('https://raw.githubusercontent.com/remo-rcm/tables/master/code-list/code-list.csv')

```

## code-list

The Remo code table which describes most common Remo variables and code identifiers.

## domains

Domain tables following the Cordex standard. Note, that domains for the REMO model are slightly larger
than the official Cordex domains to account for the nudging zone.

## vc

Tables of terrain-following vertical hybrid sigma pressure coordinates that define model levels for Remo.
To compute the pressure at a model level, the surface pressure is required (e.g., `ps`). The pressure at a
certain model level `lev` can be computed like, e.g.

```math
p(lev) =  ak(lev) + bk(lev) * ps
```
