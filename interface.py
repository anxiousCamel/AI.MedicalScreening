# interface.py

"""
Módulo de interface gráfica para diagnóstico de doenças.

Este módulo implementa uma interface gráfica utilizando a biblioteca Tkinter
para permitir aos usuários selecionar sintomas e fazer previsões de doenças
com base no modelo treinado.

Este módulo inclui as seguintes funções principais:
- run_interface: Função que inicia a interface gráfica e permite ao usuário interagir.
"""

import tkinter as tk
from tkinter import Checkbutton, IntVar, Button, Scrollbar, Listbox
from data_preprocessing import preprocess_user_symptoms
from model_training import load_model
from data_loading import load_data
from logger import logging

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

    # Cria um frame para a barra de rolagem e a lista de sintomas
    frame = tk.Frame(root)
    frame.pack()

    # Cria uma barra de rolagem
    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    # Cria uma lista de sintomas com a barra de rolagem
    symptom_listbox = Listbox(frame, yscrollcommand=scrollbar.set, selectmode="multiple")
    for symptom_id, symptom_name in symptom_mapping.items():
        symptom_listbox.insert(tk.END, symptom_name)
    symptom_listbox.pack(side="left", fill="both")

    scrollbar.config(command=symptom_listbox.yview)

    # Obtém os sintomas selecionados pelo usuário
    def get_selected_symptoms():
        selected_indices = symptom_listbox.curselection()
        selected_symptoms = [list(symptom_mapping.keys())[idx] for idx in selected_indices]
        return selected_symptoms


    def predict_diseases():
        selected_symptoms = get_selected_symptoms()
        user_symptoms = preprocess_user_symptoms(selected_symptoms, symptom_mapping)
        
        logging.info("Sintomas selecionados: %s", user_symptoms)
        
        user_predictions = model.predict([user_symptoms])
        logging.info("Doenças previstas: %s", user_predictions)

        result_label.config(text="Doenças mais prováveis:\n" + "\n".join(user_predictions))



    predict_button = Button(root, text="Fazer Previsão", command=predict_diseases)
    predict_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    run_interface()
    logging.info("Interface encerrada.")