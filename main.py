import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import os
from data_loading import load_data
from data_preprocessing import preprocess_user_symptoms, preprocess_training_data
from model_training import train_model

def main():
    data = load_data('data.json')
    if not data:
        return

    symptom_mapping = data[0]['symptomDictionary']

    user_symptoms = input("Digite os sintomas que você está sentindo, separados por vírgula: ")
    user_symptoms = preprocess_user_symptoms(user_symptoms, symptom_mapping)
    if not user_symptoms:
        return

    all_symptoms, all_labels = preprocess_training_data(data, symptom_mapping)

    model = train_model(all_symptoms, all_labels)

    user_predictions = model.predict([user_symptoms])

    print("Doenças mais prováveis de acordo com os sintomas:")
    for disease in user_predictions:
        print(disease)

if __name__ == "__main__":
    main()
