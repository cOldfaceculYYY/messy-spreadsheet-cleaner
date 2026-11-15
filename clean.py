#!/usr/bin/env python3
"""Messy spreadsheet cleaner — sample build.

Reads a messy CSV (exported from Excel/Sheets), then:
  - trims whitespace everywhere
  - drops fully empty rows and exact duplicates
  - normalises date columns to YYYY-MM-DD
  - lowercases email columns and flags invalid ones
Writes clean.csv + a short report.txt of what changed.

Usage: python clean.py messy.csv
"""
import csv, re, sys
from datetime import datetime

DATE_FORMATS = ("%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d", "%m-%d-%Y", "%B %d, %Y")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def norm_date(v):
    for f in DATE_FORMATS:
        try:
            return datetime.strptime(v, f).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return v

def main(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = [[c.strip() for c in r] for r in csv.reader(fh)]
    header, body = rows[0], rows[1:]
    date_cols = [i for i, h in enumerate(header) if "date" in h.lower()]
    mail_cols = [i for i, h in enumerate(header) if "mail" in h.lower()]
    seen, out, bad_mail = set(), [], 0
    for r in body:
        if not any(r):
            continue
        for i in date_cols:
            if i < len(r) and r[i]:
                r[i] = norm_date(r[i])
        for i in mail_cols:
            if i < len(r) and r[i]:
                r[i] = r[i].lower()
                if not EMAIL_RE.match(r[i]):
                    bad_mail += 1
        key = tuple(r)
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    with open("clean.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(out)
    with open("report.txt", "w", encoding="utf-8") as fh:
        fh.write(f"rows in: {len(body)}\nrows out: {len(out)}\n"
                 f"duplicates/empty dropped: {len(body) - len(out)}\n"
                 f"invalid emails flagged: {bad_mail}\n")
    print("done -> clean.csv, report.txt")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "messy.csv")
