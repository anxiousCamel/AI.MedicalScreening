# model_training.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from joblib import load
from logger import logging

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


"""
Carrega um modelo treinado a partir de um arquivo usando a biblioteca joblib.

Parâmetros:
filename (str): O nome do arquivo contendo o modelo treinado.

Retorna:
object: O modelo treinado carregado a partir do arquivo, ou None em caso de erro.
"""


def load_model(filename):
    try:
        return load(filename)
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None
