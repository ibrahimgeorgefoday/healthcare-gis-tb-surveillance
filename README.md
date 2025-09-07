# Healthcare GIS — TB Surveillance (Sierra Leone)

Map crude TB incidence per 100,000 by admin area and publish an interactive Folium choropleth.

![CI](https://github.com/ibrahimgeorgefoday/healthcare-gis-tb-surveillance/actions/workflows/ci.yml/badge.svg)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ibrahimgeorgefoday/healthcare-gis-tb-surveillance/blob/main/notebooks/02_maps.ipynb)

## Problem
Programs need a quick, reproducible view of **where** TB burden concentrates using safe (de-identified) data.

## Data
- `data/sample/tb_cases_sample.csv` — columns: `admin_name,cases,population` (sample only)
- `data/sample/admin_boundaries.geojson` — simplified boundaries (sample)

**Incidence (per 100k)** = `cases / population * 100000`.

## Method
1. Load cases + admin boundaries
2. Join by `admin_name`
3. Compute crude incidence
4. Visualize (Folium choropleth + markers)
5. Export `reports/tb_map.html`

## Result
- Quick hotspot map for review
- Reproducible notebook for audits

## Reproduce
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -e .[dev]
jupyter lab
