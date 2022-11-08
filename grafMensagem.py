# Exibir gráfico com as quantidades de mensagens comuns e spas parma cada mês

# biblioteca Pandas
import pandas as pd
import plotly.express as px

# link em variável
mes = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTU8zYASHDKNCjZ2EyK7kINt_e34XvFqC5mlXWa5Q5OED1xkDpQnMb1iPq3oCXDIabyGBRQpi1GzugL/pub?gid=1235580450&single=true&output=csv'
# variável em tabela
tabelaMes = pd.read_csv(mes, header=1) # header=1 > a partir da linha 1
# transforma os dados em gráfico
figMes = px.bar(tabelaMes, x='Mes', y=['no', 'yes'])
figMes.show()
