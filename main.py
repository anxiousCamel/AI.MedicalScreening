# main.py
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from joblib import dump, load
from data_preprocessing import preprocess_training_data
from data_loading import load_data
from interface import run_interface
from logger import logging

# Função para processar o texto individualmente
def analyze_text(x):
    return x

def train_model(all_symptoms, all_labels):
    logging.info("Treinando o modelo...")
    model = make_pipeline(
        TfidfVectorizer(analyzer=analyze_text),
        MultinomialNB()
    )
    model.fit(all_symptoms, all_labels)

    # Calcula a acurácia nos dados de treinamento
    train_accuracy = model.score(all_symptoms, all_labels)

    logging.info("Modelo treinado com sucesso. Acurácia: %.2f%%", train_accuracy * 100)
    return model

def save_model(model, filename):
    dump(model, filename)

def load_model(filename):
    return load(filename)

if __name__ == "__main__":
    logging.info("Iniciando o programa.")
    data = load_data('data.json')
    if not data:
        logging.error("Falha ao carregar os dados.")
        exit()

    symptom_mapping = data[0]['symptomDictionary']
    all_symptoms, all_labels = preprocess_training_data(data, symptom_mapping)

    model = train_model(all_symptoms, all_labels)
    save_model(model, 'trained_model.joblib')
    logging.info("Modelo treinado e salvo.")

    run_interface()
    logging.info("Interface encerrada.")
