import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# 数据json
filename = "./data/eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

# 读取地震数据
all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=["经度", "纬度", "位置", "震级"])
data.head()

# 基本数据展示
# fig = px.scatter(data, x="经度", y="纬度", size='震级', size_max=10, color="震级",
#                  range_x=[-200, 200], range_y=[-90, 90], hover_name="位置",
#                  width=800, height=800, title="全球地震散点图")
#
# fig.write_html('global_eq.html')
# fig.show()

# 地图形式展示
fig = px.scatter_mapbox(data, lon="经度", lat="纬度", size='震级', size_max=10, color="震级",
                        hover_name="位置", title="全球地震散点图")

token = "pk.eyJ1IjoiZHh4enN0IiwiYSI6ImNrbnB1OWZsYTA3eTMydm15M3prbHZyOTQifQ.OYTQ6DVNpsuSTF60j96FVQ"
fig.update_layout(mapbox={'accesstoken': token, "zoom": 1, "style": 'dark'})
fig.write_html('global_eq2.html')
fig.show()
