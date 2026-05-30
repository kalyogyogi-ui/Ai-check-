# Quantum Tokenomics — Stress Testing Tools

Companion artifacts for *Tokenomics in the Quantum Age* (Chapter 11, Appendix E).

## Files

| File | Purpose |
|------|---------|
| `qri_stress_model.csv` | Editable parameters for SCR, fee shock, TVL bands, governance participation |

## Quick start

1. Open `qri_stress_model.csv` in Excel, Google Sheets, or LibreOffice.  
2. Enter your protocol’s bytes per signature (legacy vs PQC), block capacity, and TVL.  
3. Review computed **SCR**, **throughput ratio**, and **illustrative fee multiplier** columns.  
4. Tag outputs as **(Estimate)** in any external report.

## Python (optional)

```bash
python3 -c "
import csv
from pathlib import Path
rows = list(csv.DictReader(Path('qri_stress_model.csv').open()))
for r in rows:
    if r.get('parameter'):
        print(r['parameter'], '=', r.get('example_value',''))
"
```

## Repository

When publishing, mirror this folder at:

`https://github.com/kalyogyogi-ui/Ai-check-/tree/main/book/tools`

*(Update URL to match your final repository path.)*

## Disclaimer

Models are educational. Not investment or security advice.
