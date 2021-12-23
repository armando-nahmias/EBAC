import pandas as pd
import seaborn as sns
gasolina = pd.read_csv('./dados/gasolina.csv')
with sns.axes_style('whitegrid'):
    grafico = sns.lineplot(data=gasolina, x='dia', y='venda', palette='pastel')
    grafico.set(title='Variação do Preço da galina por dia', xlabel='Dia', ylabel='Preço (R$');
