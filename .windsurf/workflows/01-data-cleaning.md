---
description: Guides you through profiling, correcting, and versioning raw data so it is trustworthy for modeling
---

## Overview
Data must be **accurate, consistent, complete, and correctly typed** before any modeling; unclean inputs propagate irreparable error downstream.

### Step 1 — Profile the Raw Table
Inspect schema, data types, ranges, and missing‑value counts with `pandas.info()` and `describe()`.

### Step 2 — Enforce Correct Types
Cast columns to canonical numeric, categorical, datetime, or boolean types; reject or coerce on error.

### Step 3 — Handle Missing Data
Impute (mean, median, mode, or model‑based) only when semantically valid; otherwise label or drop records.

### Step 4 — Remove Duplicates
Use composite business keys or full‑row hashes to drop exact and near‑duplicate rows.

### Step 5 — Standardize & Normalize
Strip whitespace, unify case, convert units, and apply scaling or encoding so models treat values comparably.

### Step 6 — Detect Outliers
Flag extreme z‑scores or IQR deviations; correct obvious data‑entry errors, otherwise cap or exclude.

### Step 7 — Validate & Version
Re‑run profiling; commit cleaned dataset to DVC or Git‑LFS with checksums to guarantee reproducibility.