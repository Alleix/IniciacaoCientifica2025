import pandas as pd

perguntas = pd.read_csv('codigoPerguntas.csv')

indices = perguntas.index[perguntas['B02019A'] == 0].tolist()
print(indices)