import plotly.graph_objects as go

def criarGraficoBarras(x, y, titulo, x_label, y_label):

    estados = x[:(len(x) // 2)]
    y_estados = y[:(len(y) // 2)]

    capitais = x[(len(x) // 2):]
    y_capitais = y[(len(y) // 2):]

    # Tratamento caso as listas estejam vazias
    if len(y_estados) == 0 and len(y_capitais) == 0:
        min_y, max_y = 0, 1  # valores padrão
    else:
        # Calcula mínimo considerando listas não vazias
        min_y_candidates = []
        if len(y_estados) > 0:
            min_y_candidates.append(min(y_estados))
        if len(y_capitais) > 0:
            min_y_candidates.append(min(y_capitais))
        min_y = min(min_y_candidates)

        max_y_candidates = []
        if len(y_estados) > 0:
            max_y_candidates.append(max(y_estados))
        if len(y_capitais) > 0:
            max_y_candidates.append(max(y_capitais))
        max_y = max(max_y_candidates)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=estados, 
        y=y_estados, 
        name='Estados', 
        visible=True,
        text=[f'{v:.1f}' for v in y_estados],
        textposition='auto'
    ))
    fig.add_trace(go.Bar(
        x=capitais,
        y=y_capitais,
        name='Capitais',
        visible=False,
        text=[f'{v:.1f}' for v in y_capitais],
        textposition='auto'
    ))

    fig.update_layout(
        title=titulo,
        xaxis_title=x_label,
        yaxis_title=y_label,

        # Define range fixo para eixo y, adicionando margem para visualização melhor
        yaxis=dict(range=[min_y*0.9, max_y*1.1]),

        updatemenus=[

            dict(
                type='buttons',
                direction='right',
                active=0,
                x=0.57,
                y=1.1,
                buttons=[
                    dict(
                        label='Estados',
                        method='update',
                        args=[
                            {'visible': [True, False]},
                        ]
                    ),
                    dict(
                        label='Capitais',
                        method='update',
                        args=[
                            {'visible': [False, True]},
                        ]
                    )
                ]
            )
        ]
    )
    return fig

# %%
#graficoBarras([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,#18,19,20], "Gráfico de Barras", "Eixo X", "Eixo Y").show(width=600, height=600)

# %%



