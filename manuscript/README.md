# Post-Quantum Cryptography Manuscript

Author-voice revision with embedded **Mermaid figures** and **Author's note** callouts.

## Layout

| Path | Content |
|------|---------|
| `00-front-matter.md` | Title, preface, conventions — **replace [Your Name]** |
| `chapters/01` … `22` | Main chapters (voice pass applied) |
| `appendices/appendix-a` … `d` | Reference appendices |
| `VOICE-GUIDE.md` | Editorial standards |

## Regenerate voice pass

```bash
# Restore from uploads if needed, then:
python3 scripts/apply_author_voice.py
python3 scripts/deepen_voice.py
```

## Figures

Diagrams use **Mermaid** inside chapters (renders on GitHub, many static site generators, and VS Code). For print PDF, export via [mermaid-cli](https://github.com/mermaid-js/mermaid-cli) into `figures/png/`.

## Next manual steps for the author

1. Replace `[Your Name]` in `00-front-matter.md`
2. Rewrite middle sections where prose still feels encyclopedic (especially Ch. 1–4 openings)
3. Add primary-source citations for statistics and policy claims
4. Peer review FIPS chapters against official NIST PDFs
