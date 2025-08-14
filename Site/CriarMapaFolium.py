import folium
import pandas as pd
from branca.colormap import linear
import re

def criarMapa(geojsonFile:str, taxaRegiao:pd.DataFrame, legenda:str):
    geo_json_data = geojsonFile
    colormap = linear.YlGn_09.scale(taxaRegiao.taxa.min(), taxaRegiao.taxa.max())
    taxaRegiao_dict = taxaRegiao.set_index("estados")["taxa"]

    print(legenda)

    m = folium.Map(location=[-15.5, -54],     zoom_start=4.5,  # Zoom inicial mais "suave"
    min_zoom=3,
    max_zoom=7, tiles="cartodbpositron")
    
    popup = folium.GeoJsonPopup(fields=["nome"])

    folium.GeoJson(
        geo_json_data,
        zoom_on_click=False,
        name=legenda,
        style_function=lambda feature: {
            "fillColor": colormap(taxaRegiao_dict.get(feature["id"], "#cccccc")),
            "color": "black",
            "weight": 1,
            "dashArray": "5, 5",
            "fillOpacity": 0.9,
        },
        highlight_function=lambda feature: {
            "fillColor": "orange",
        },
        popup=popup,
        popup_keep_highlighted=True,
    ).add_to(m)

    folium.LayerControl().add_to(m)
    colormap.caption = legenda
    colormap.add_to(m)

    m.save('mapa.html')

    with open('mapa.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Regex: encontra o bloco de opções do L.map(...) e insere zoomSnap e zoomDelta
    html_modificado = re.sub(
        r'(zoom:\s*[\d\.]+,)',
        r'\1\n        zoomSnap: 0.1,\n        zoomDelta: 0.1,',
        html
    )

    with open('mapa.html', 'w', encoding='utf-8') as f:
        f.write(html_modificado)


# %%


# %%



