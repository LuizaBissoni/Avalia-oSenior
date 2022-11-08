#Exibir o dia de cada mês que possui a maior sequência de mensagens comuns (não spam)

# spam por dia e mês
# link em variável
spam = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTU8zYASHDKNCjZ2EyK7kINt_e34XvFqC5mlXWa5Q5OED1xkDpQnMb1iPq3oCXDIabyGBRQpi1GzugL/pub?gid=871013319&single=true&output=csv'
# transforma em tabela
qntSpam = pd.read_csv(spam, header=1)
qntSpam.head()

# dia do mes 1 que teve mais spam
maximoSpam = 0

for linhas in qntSpam['1']: 
  valorMaximoSpam = qntSpam.iat[linhas, 1]
  if(valorMaximoSpam > maximoSpam):
    maximoSpam = valorMaximoSpam
    linha = linhas

print(f'O dia {qntSpam.iat[linha, 0]} do mês {qntSpam.columns.values[1]} teve {qntSpam.iat[linha, 1]} palavras')

# dia do mes 2 que teve mais spam
# coloca 0 onde não tem valor
qntSpam['2'] = qntSpam['2'].fillna(0)
# deixa os valores inteiros
qntSpam = qntSpam.astype('int32')

maximoSpam = 0
for linhas in qntSpam['2']: 
  valorMaximoSpam = qntSpam.iat[int(linhas), 2]
  if(valorMaximoSpam > maximoSpam):
    maximoSpam = valorMaximoSpam
    linha = linhas

print(f'O dia {qntSpam.iat[linha, 0]} do mês {qntSpam.columns.values[2]} teve {qntSpam.iat[linha, 2]} palavras')

# dia do mês 3 que teve mais spam
maximoSpam = 0

for linhas in qntSpam['3']: 
  valorMaximoSpam = qntSpam.iat[linhas, 3]
  if(valorMaximoSpam > maximoSpam):
    maximoSpam = valorMaximoSpam
    linha = linhas

print(f'O dia {qntSpam.iat[linha, 0]} do mês {qntSpam.columns.values[3]} teve {qntSpam.iat[linha, 3]} palavras')
