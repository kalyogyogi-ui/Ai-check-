# Author Voice Pass — Changelog

Applied to all **22 chapters** + **4 appendices** (2026-05-25).

## Every chapter now includes

1. **Author opener** — practitioner framing (India + global deployments)  
2. **Figure X.1** — Mermaid architecture / flow at chapter start  
3. **Figure X.2** — second diagram at second major section (where configured)  
4. **2–4 `Author's note` boxes** — judgment calls, India/regulatory caveats, implementation warnings  
5. **`§N.99 Author's Closing Perspective`** — actionable wrap-up  
6. **Global tone substitutions** — reduced "comprehensive / Furthermore / this book" phrasing  

## Appendices

- Author framing intro  
- **Appendix A:** Figure A.1 math-to-PQC map  
- **Appendix C:** Figure C.1 deployment stack  

## What you must still do manually

- Replace `[Your Name]` in front matter  
- Rewrite long encyclopedic **middle paragraphs** (especially Ch. 1–4, 17 benchmarks)  
- Add **inline citations** (NIST, RFC, papers, RBI/MeitY circulars)  
- Export Mermaid to PNG for print publishers  

## Regenerate

```bash
python3 scripts/apply_author_voice.py && python3 scripts/deepen_voice.py
```
