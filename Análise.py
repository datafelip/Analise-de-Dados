import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("Base de Dados.xlsx")
df.columns = df.columns.str.strip().str.replace("\xa0", "", regex=True)


def calcular_media(df, coluna):
    media = df[coluna].mean()
    print(f"Média de '{coluna}': {media:.2f}")

# Médias
for col in ['Erros_Reportados', 'Tempo_Conclusao', 'Produtividade', 'Experiencia']:
    calcular_media(df, col)


def calcular_desvio_padrao(df, coluna):
    desvio = df[coluna].std()
    print(f"Desvio padrão de '{coluna}': {desvio:.2f}")

# Desvios padrão
for col in ['Erros_Reportados', 'Tempo_Conclusao', 'Produtividade', 'Experiencia']:
    calcular_desvio_padrao(df, col)

print("\nVerificação de outliers em 'Erros_Reportados':")
for idx, valor in enumerate(df['Erros_Reportados'], start=1):
    if valor > 6:
        print(f"/\\ Acima do Padrão {idx} = {valor}")
    elif valor < 2:
        print(f"\\/ Abaixo do Padrão {idx} = {valor}")

df['Tempo_Conclusao'] = df['Tempo_Conclusao'].round().astype(int)
df['Produtividade'] = df['Produtividade'].round().astype(int)

def box_plot(df, coluna, titulo, xlabel, cor='gray'):
    contagem = df[coluna].value_counts().sort_index()
    print(f"\n{titulo} (Tabela):")
    print(pd.DataFrame({
        coluna: [f"{i} {xlabel.lower() + ('s' if i != 1 else '')}" for i in contagem.index],
        'Pessoas': contagem.values
    }).to_string(index=False))

    plt.figure(figsize=(10, 4))
    box = plt.boxplot(df[coluna], vert=False, patch_artist=True)
    for pedaco in box['boxes']:
        pedaco.set_facecolor(cor)
    plt.title(f'Box Plot de {titulo}')
    plt.xlabel(xlabel)
    plt.tight_layout()
    plt.show()

def grafico_pessoas_por_categoria(df, coluna, titulo, xlabel, cor='gray'):
    contagem = df[coluna].value_counts().sort_index()
    print(f"\n{titulo} (Tabela):")
    print(pd.DataFrame({
        coluna: [f"{i} {xlabel.lower() + ('s' if i != 1 else '')}" for i in contagem.index],
        'Pessoas': contagem.values
    }).to_string(index=False))

    plt.figure(figsize=(10, 4))
    plt.bar(contagem.index, contagem.values, color=cor)
    plt.title(f'Pessoas por {titulo}')
    plt.xlabel(xlabel)
    plt.ylabel('Número de Pessoas')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# Gráficos de barras
grafico_pessoas_por_categoria(df, 'Erros_Reportados', 'Quantidade de Erros', 'Erro', 'red')
grafico_pessoas_por_categoria(df, 'Tempo_Conclusao', 'Tempo de Conclusão', 'Hora', 'orange')
grafico_pessoas_por_categoria(df, 'Produtividade', 'Produtividade (Linhas/Dia)', 'Linha', 'green')
grafico_pessoas_por_categoria(df, 'Experiencia', 'Experiência', 'Ano de Experiência', 'skyblue')

# Box plots
box_plot(df, 'Erros_Reportados', 'Quantidade de Erros', 'Erro', 'red')
box_plot(df, 'Tempo_Conclusao', 'Tempo de Conclusão', 'Hora', 'orange')
box_plot(df, 'Produtividade', 'Produtividade (Linhas/Dia)', 'Linha', 'green')
box_plot(df, 'Experiencia', 'Experiência', 'Ano de Experiência', 'skyblue')
