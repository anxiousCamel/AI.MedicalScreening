import json
import tkinter as tk
from tkinter import messagebox

def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data[0]  # Acessar o dicionário dentro da lista
    except FileNotFoundError:
        return None

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump([data], file, indent=2)

def add_symptom(symptom_data, new_symptoms, new_disease):
    symptom_dict = symptom_data['symptomDictionary']
    normalized_symptoms = [symptom.strip().lower() for symptom in new_symptoms]

    for symptom in normalized_symptoms:
        if symptom not in symptom_dict.values():
            new_number = max(map(int, symptom_dict.keys())) + 1
            symptom_dict[str(new_number)] = symptom

    disease_exists = False
    for entry in symptom_data['data']:
        if entry['disease'].lower() == new_disease.strip().lower():
            entry['symptoms'] += [int(key) for key in symptom_dict if symptom_dict[key] in normalized_symptoms]
            disease_exists = True
            break

    if not disease_exists:
        new_symptom_numbers = [int(key) for key in symptom_dict if symptom_dict[key] in normalized_symptoms]
        symptom_data['data'].append({
            'symptoms': new_symptom_numbers,
            'disease': new_disease
        })

    save_data(file_name, symptom_data)
    messagebox.showinfo("Sucesso", "Novos sintomas e doença adicionados com sucesso!")

def submit():
    new_symptoms_input = new_symptoms_entry.get()
    new_symptoms = [symptom.strip().lower() for symptom in new_symptoms_input.split(',')]
    new_disease = new_disease_entry.get()

    add_symptom(symptom_data, new_symptoms, new_disease)

file_name = 'data.json'
symptom_data = load_data(file_name)

if symptom_data is None:
    symptom_data = {
        'symptomDictionary': {},
        'data': []
    }

root = tk.Tk()
root.title("Adicionar Sintomas e Doença")

tk.Label(root, text="Novos Sintomas (separados por vírgula):").pack()
new_symptoms_entry = tk.Entry(root)
new_symptoms_entry.pack()

tk.Label(root, text="Nova Doença:").pack()
new_disease_entry = tk.Entry(root)
new_disease_entry.pack()

submit_button = tk.Button(root, text="Adicionar", command=submit)
submit_button.pack()

root.mainloop()
