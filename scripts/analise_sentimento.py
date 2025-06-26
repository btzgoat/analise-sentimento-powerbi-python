import pandas as pd
from leia.leia import SentimentIntensityAnalyzer

# Criacao de uma simulacao para que o codigo rode sem a ajuda do Power BI, facilitando a acao de testes, imitando a tabela que o Power BI daria
dados_exemplo = {
    'Texto_Avaliacao': [
        "Amei o celular! A bateria dura o dia todo e a camera e incrivel.",
        "O som e muito baixo e o material parece fragil. Decepcionado.",
        "E um bom aparelho, rapido e com design bonito. Recomendo.",
        "O relogio e funcional, mas a tela poderia ter mais brilho."
    ]
}
dataset = pd.DataFrame(dados_exemplo)


s = SentimentIntensityAnalyzer()

def classificar_sentimento_pt(texto):
    score = s.polarity_scores(texto)
    compound_score = score['compound']
    
    if compound_score >= 0.05:
        return 'Positivo'
    elif compound_score <= -0.05:
        return 'Negativo'
    else:
        return 'Neutro'

df = dataset.copy()
df['Sentimento'] = df['Texto_Avaliacao'].apply(classificar_sentimento_pt)

print(df)