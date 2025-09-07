# python
from pathlib import Path
import pandas as pd, folium, json

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data" / "sample"
REPORTS = ROOT / "reports"
SAMPLE.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)

csv_fp = SAMPLE / "tb_cases_sample.csv"
if not csv_fp.exists():
    pd.DataFrame({
        "admin_name": ["Western Urban","Western Rural","Bombali","Bo","Kenema"],
        "cases": [120,65,40,70,55],
        "population": [1000000,500000,350000,600000,500000],
    }).to_csv(csv_fp, index=False)

df = pd.read_csv(csv_fp)
df["incidence_100k"] = (df["cases"] / df["population"]) * 100000

geo = {
  "type": "FeatureCollection",
  "features": [
    {"type":"Feature","properties":{"admin_name":"Western Urban"},"geometry":{"type":"Polygon","coordinates":[[[-13.25,8.43],[-13.15,8.43],[-13.15,8.53],[-13.25,8.53],[-13.25,8.43]]]}},
    {"type":"Feature","properties":{"admin_name":"Western Rural"},"geometry":{"type":"Polygon","coordinates":[[[-13.35,8.33],[-13.25,8.33],[-13.25,8.53],[-13.35,8.53],[-13.35,8.33]]]}},
    {"type":"Feature","properties":{"admin_name":"Bombali"},"geometry":{"type":"Polygon","coordinates":[[[-12.75,9.0],[-12.55,9.0],[-12.55,9.2],[-12.75,9.2],[-12.75,9.0]]]}},
    {"type":"Feature","properties":{"admin_name":"Bo"},"geometry":{"type":"Polygon","coordinates":[[[-11.9,8.6],[-11.7,8.6],[-11.7,8.8],[-11.9,8.8],[-11.9,8.6]]]}},
    {"type":"Feature","properties":{"admin_name":"Kenema"},"geometry":{"type":"Polygon","coordinates":[[[-11.4,8.4],[-11.2,8.4],[-11.2,8.7],[-11.4,8.7],[-11.4,8.4]]]}}
  ]
}

m = folium.Map(location=[8.6, -12.7], zoom_start=7, tiles="cartodbpositron")
folium.Choropleth(
    geo_data=json.dumps(geo),
    data=df,
    columns=["admin_name","incidence_100k"],
    key_on="feature.properties.admin_name",
    fill_opacity=0.85, line_opacity=0.6, nan_fill_opacity=0.2,
    legend_name="TB incidence per 100k"
).add_to(m)

out = REPORTS / "tb_map.html"
m.save(out.as_posix())
print("Wrote:", out)
