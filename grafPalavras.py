# Exibir gráfico as palavras mais frequentes em toda a base de dados

# biblioteca Pandas
import pandas as pd
import plotly.express as px

# link em variável
sms = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTU8zYASHDKNCjZ2EyK7kINt_e34XvFqC5mlXWa5Q5OED1xkDpQnMb1iPq3oCXDIabyGBRQpi1GzugL/pub?gid=1902221185&single=true&output=csv'
# variável em tabela
tabela = pd.read_csv(sms)
# pra organizar em ordem decrescente (maior para o menor)
organizado = tabela.sort_values(by = 'vezes', ascending = False) 
# transforma os dados em gráfico
fig = px.bar(organizado, x='letras', y='vezes')
fig.show()