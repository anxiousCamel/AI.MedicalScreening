from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

"""
Treina um modelo de classificação usando os sintomas e rótulos de treinamento.

Parâmetros:
all_symptoms (list): Lista de listas contendo os sintomas de treinamento.
all_labels (list): Lista contendo os rótulos de doenças correspondentes.

Retorna:
MultinomialNB: O modelo treinado.
"""
def train_model(all_symptoms, all_labels):
    model = make_pipeline(
        TfidfVectorizer(analyzer=lambda x: x),
        MultinomialNB()
    )
    model.fit(all_symptoms, all_labels)
    return model
