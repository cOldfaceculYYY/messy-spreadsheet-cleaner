# messy-spreadsheet-cleaner

**Your spreadsheet is a mess. This fixes it in one command.**

Takes a messy CSV exported from Excel or Google Sheets and returns a clean,
normalised file plus a plain-English report of everything that changed.

## What it fixes

- Mixed date formats (`2026/1/5`, `Jan 5 2026`, `05-01-2026`) → one ISO format
- Stray spaces, doubled spaces, inconsistent casing
- Duplicate rows (exact and near-duplicates)
- Inconsistent emails / phone formats
- Empty trailing rows and columns from sloppy exports

## Run it

```
python clean.py messy.csv
```

**Output:** `clean.csv` (normalised) + `report.txt` (rows in, rows out, what changed and how much).

No heavy dependencies. Pure standard library.

## Want this done on YOUR files?

This is a sample of paid client work. Typical commissions:

- One-off cleanup of Excel / CSV / Google Sheets exports
- Multi-sheet workbooks merged, deduped, standardised
- Recurring reports: same messy export in → same clean report out, every week
- Data → slides: clean numbers turned into a PPT that reads well

Flat fee agreed up front, 50% prepayment in USDC (Polygon), delivery in 24–48h.

**DM on X: [@cOldfaceculYYY](https://x.com/cOldfaceculYYY)** — send a sample of the mess, get a fixed quote.
