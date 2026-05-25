# Figure & Architecture Placement Rules

Every chapter follows this **in-section** layout (not in the chapter opener):

```
## N.M Section title

[1–2 introductory sentences — what this section decides]

> **Author's note:** (optional, on-topic only)

**Figure N.M — Caption (architecture / flow / sizes)**

```mermaid
...
```

*Italic caption: what decision this figure supports.*

[Remainder of section body — may reference “Figure N.M” in prose]
```

## Do not

- Place figures between `# Chapter` and the first `##` section
- Put figures **before** the section’s first explanatory paragraph
- Merge `## 1.1` with `**Figure**` on one line
- Paste the same hybrid-TLS note into unrelated chapters

## Figure types by chapter

| Chapters | Figure content |
|----------|----------------|
| 1–4 | Threat stack, HNDL, Mosca, family map |
| 5–9 | Math / construction intuition |
| 10–14 | NIST timeline, FIPS byte sizes, FO transform |
| 15–18 | **TLS/PKI architecture** (sequence + PKI chain) |
| 19–21 | Migration phases, CBOM CI/CD, India stakeholder map |
| 22 | Research funnel |

## Regenerate placement

```bash
python3 scripts/place_figures.py      # registry-based insert
python3 scripts/fix_figure_order_all.py  # figure after first § paragraph
python3 scripts/repair_figure_headings.py
```

Then rebuild `COMPLETE-BOOK.md` from `manuscript/`.
