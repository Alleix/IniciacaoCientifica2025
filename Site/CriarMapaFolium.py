# %%

import folium
import pandas
from branca.colormap import linear
import branca.colormap as cm

# %%
#Criar o mapa


def criarMapa(geojsonFile:str, taxaRegiao:pandas.DataFrame,legenda:str):

    geo_json_data = geojsonFile

    taxaRegiao = taxaRegiao

    colormap = linear.YlGn_09.scale(
        taxaRegiao.taxa.min(), taxaRegiao.taxa.max()
    )

    taxaRegiao_dict = taxaRegiao.set_index("estados")["taxa"]

    print(legenda)

    m = folium.Map([-15.5, -54], zoom_start=4.5, tiles="BaseMapDE.Grey")
    popup = folium.GeoJsonPopup(fields=["nome"])


    folium.GeoJson(
        geo_json_data,                       #estados americanos
        zoom_on_click=False,                  #permite zoom ao clicar nos estados
        name=legenda,
        style_function=lambda feature: {     #estilo, diferencia a cor e cria linhas pontilhadas nas divisas dos estados
            "fillColor": colormap(taxaRegiao_dict[feature["id"]]),
            "color": "black",
            "weight": 1,
            "dashArray": "5, 5",
            "fillOpacity": 0.9,
        },
        highlight_function=lambda feature: { #highlight azul ao passar o mouse em um estado
            "fillColor": (
                "orange"
            ),
        },
        popup=popup,                         #Informação ao clicar em um estado
        popup_keep_highlighted=True,
    ).add_to(m)

    folium.LayerControl().add_to(m)


    colormap.caption = legenda
    colormap.add_to(m)
    m
    m.save('mapa.html')


# %%


# %%



