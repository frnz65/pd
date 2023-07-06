import plotly.express as px
import pandas as pd
filename = 'track.csv'
data = pd.read_csv(filename)

fig = px.line_mapbox(data,lat='LAT',lon='LON',hover_name='SHIPNAME')
fig.update_layout(mapbox_style="carto-positron", margin={"r":0,"t":0,"l":0,"b":0}, height = 768)

fig.write_html("./map.html")
