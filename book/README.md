# Tokenomics in the Quantum Age — Manuscript Package

**Edition:** Audit implementation complete (2026-05-30)

## Primary file

[`Tokenomics_in_the_Quantum_Age_Complete_Book.md`](Tokenomics_in_the_Quantum_Age_Complete_Book.md) (~153k words)

## Supporting files

| File | Purpose |
|------|---------|
| [`ART_BRIEF.md`](ART_BRIEF.md) | Print-figure production specs |
| [`FACT_CHECK_MANIFEST.md`](FACT_CHECK_MANIFEST.md) | Pre-print verification checklist |
| [`tools/qri_stress_model.csv`](tools/qri_stress_model.csv) | SCR / stress parameters |
| [`tools/README.md`](tools/README.md) | How to use the CSV model |

## Implemented (full audit pass)

- Executive Summary + About This Book (no draft/audit meta in body)
- Detailed TOC + Print TOC + LOF/LOT
- Legal disclaimer; (Data) / (Estimate) / (Scenario) labels
- Competitive comparison table (Preface)
- Master Timeline (Ch. 5) + Ch. 13 cross-reference
- Preview: Cryptoeconomic Substrate (duplicate heading fix)
- Chapter at a Glance × 16
- Chapter Exercises × 16 (Appendix E for solutions)
- Worked SCR example; Cases 1–9
- Mermaid figures 1.1, 1.2, 2.1, 4.1, 5.1, 6.1
- Expanded Appendices B, C; new F (RACI), G (EMC budgets)
- Footnotes [^1]–[^6]; reviewer table in Acknowledgments
- Em-dash reduction (~34%); placement notes in ART_BRIEF only

## Regenerate safely

```bash
cd book
cp Tokenomics_in_the_Quantum_Age_Complete_Book.md.bak Tokenomics_in_the_Quantum_Age_Complete_Book.md
python3 scripts/repair_manuscript.py
```

## Still human-required before print

1. Commission print figures from `ART_BRIEF.md`
2. Complete `FACT_CHECK_MANIFEST.md`
3. Assign named reviewers in Acknowledgments
4. Professional copyedit pass
