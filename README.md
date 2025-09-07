# Healthcare GIS — TB Surveillance (Sierra Leone)
[![CI](https://github.com/ibrahimgeorgefoday/healthcare-gis-tb-surveillance/actions/workflows/ci.yml/badge.svg)](https://github.com/ibrahimgeorgefoday/healthcare-gis-tb-surveillance/actions/workflows/ci.yml)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ibrahimgeorgefoday/healthcare-gis-tb-surveillance/blob/main/notebooks/01_eda.ipynb)

Map crude TB incidence (per 100k) by admin area and publish an interactive Folium choropleth.

---

## Problem
Programs need a fast, reproducible view of **where** TB burden concentrates using de-identified data.

## Data
Sample files only (safe for Git):
- `data/sample/tb_cases_sample.csv` → `admin_name,cases,population`
- `data/sample/admin_boundaries.geojson` → simplified admin polygons (WGS84)

**Incidence** = `cases / population * 100000`.

## Method
1. Load cases + boundaries.
2. Join on `admin_name`.
3. Compute `incidence_100k`.
4. Visualize with Folium (choropleth + markers).
5. Export `reports/tb_map.html`.

## Quickstart
```bash
# 1) set up env
python -m venv .venv
. .venv/Scripts/activate   # (Windows PowerShell: .\.venv\Scripts\Activate.ps1)
pip install -U pip pandas geopandas folium jupyter nbconvert ruff pytest

# 2) run notebooks
jupyter lab
# open: notebooks/01_eda.ipynb (smoke), notebooks/02_maps.ipynb (mapping)
