# Calcular o máximo, o mínimo, a média, a mediana, o desvio padrão e a variância da quantidade total de palavras (Word_Count) para cada mês;

# biblioteca Pandas
import pandas as pd
import plotly.express as px

# link em variável
palavras = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTU8zYASHDKNCjZ2EyK7kINt_e34XvFqC5mlXWa5Q5OED1xkDpQnMb1iPq3oCXDIabyGBRQpi1GzugL/pub?gid=2086507550&single=true&output=csv'
# variável em tabela
tabelaPalavras = pd.read_csv(palavras)
tabelaPalavras.head()

# calcula qual mês teve o valor maximo
maximo = 0
for linhas in tabelaPalavras.index: 
  valorMaximo = tabelaPalavras.iat[linhas, 1]
  if( valorMaximo > maximo):
    maximo = valorMaximo
    mes = linhas
    print(f'O mês {tabelaPalavras.iat[mes, 0]} teve {tabelaPalavras.iat[mes, 1]} palavras')

# calcula qual mês teve o valor minimo
minimo = maximo
for linhas in tabelaPalavras.index:
  valorMinimo = tabelaPalavras.iat[linhas, 1]
  if(valorMinimo < minimo):
    minimo = valorMinimo
    mes = linhas
    print(f'O mês {tabelaPalavras.iat[mes, 0]} teve {tabelaPalavras.iat[mes, 1]} palavras')

# média dos valores da quantidade total de palavras
total = 0
quantidade = 0
for linhas in tabelaPalavras.index:
  valor = tabelaPalavras.iat[linhas, 1]
  total = total + valor
  quantidade = quantidade + 1
media = total / quantidade
print(media)

# valor do meio da quantidade total de palavras
# pra organizar em ordem decrescente (menor para o maior)
organizado2 = tabelaPalavras.sort_values(by = 'Palavras', ascending = True)
# quantidade de linhas da coluna
total = len(organizado2['Palavras']) %2
# se a quantidade for ímpar
if(total):
  quantidadenumeros = len(organizado2['Palavras']) 
  metadeim = int((quantidadenumeros / 2) - 0.5) 
  medianaimpar = organizado2.iat[metadeim,1]
  print(medianaimpar)
# se a quantidade for par
else:
  quantidadenumeros2 = len(organizado2['Palavras'])
  metadepar = int((quantidadenumeros2 / 2))
  medianapar = ((quantidadenumeros2[metadepar] + quantidadenumeros2[metadepar-1])/2)
  print(medianapar)

# desvio padrão da quantidade total de palavras
desviopadrao = tabelaPalavras['Palavras'].std()
print(desviopadrao)

# variancia da quantidade total de palavras
variancia = tabelaPalavras['Palavras'].var()
print(variancia)

