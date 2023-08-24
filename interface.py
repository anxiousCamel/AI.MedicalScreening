"""
Módulo de interface gráfica para diagnóstico de doenças.

Este módulo implementa uma interface gráfica utilizando a biblioteca Tkinter
para permitir aos usuários selecionar sintomas e fazer previsões de doenças
com base no modelo treinado.

Este módulo inclui as seguintes funções principais:
- run_interface: Função que inicia a interface gráfica e permite ao usuário interagir.
"""

import tkinter as tk
from tkinter import Checkbutton, IntVar, Button
from data_preprocessing import preprocess_user_symptoms
from model_training import load_model
from data_loading import load_data
import logging
import logger

"""
Inicia a interface gráfica para diagnóstico de doenças.
    
Carrega os dados de sintomas e o modelo treinado, exibe os sintomas como
checkboxes para seleção do usuário e permite fazer previsões de doenças
com base nos sintomas selecionados.
"""
def run_interface():
    logging.info("Iniciando a interface gráfica.")
    data = load_data('data.json')
    if not data:
        logging.error("Falha ao carregar os dados.")
        exit()

    model = load_model('trained_model.joblib')
    symptom_mapping = data[0]['symptomDictionary']

    root = tk.Tk()
    root.title("Diagnóstico de Doenças")

    checkbox_vars = []

    # Cria checkboxes para cada sintoma
    for symptom_id, symptom_name in symptom_mapping.items():
        var = IntVar()
        checkbox = Checkbutton(root, text=symptom_name, variable=var)
        checkbox_vars.append((var, symptom_id))
        checkbox.pack()

    # Obtém os sintomas selecionados pelo usuário
    def get_selected_symptoms():
        selected_symptoms = []
        for var, symptom_id in checkbox_vars:
            if var.get() == 1:
                selected_symptoms.append(symptom_id)
        return selected_symptoms

    # Realiza a previsão de doenças com base nos sintomas selecionados
    def predict_diseases():
        selected_symptoms = get_selected_symptoms()
        user_symptoms = preprocess_user_symptoms(selected_symptoms, symptom_mapping)
        user_predictions = model.predict([user_symptoms])

        result_label.config(text="Doenças mais prováveis:\n" + "\n".join(user_predictions))
        logging.info("Previsões feitas: %s", user_predictions)

    # Botão para fazer a previsão
    predict_button = Button(root, text="Fazer Previsão", command=predict_diseases)
    predict_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    run_interface()
    logging.info("Interface encerrada.")
