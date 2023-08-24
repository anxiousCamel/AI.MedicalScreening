"""
Pré-processa os sintomas do usuário.

Parâmetros:
user_symptoms (str): Sintomas informados pelo usuário, separados por vírgula.
symptom_mapping (dict): Dicionário que mapeia sintomas para seus números correspondentes.

Retorna:
list: Lista dos números correspondentes aos sintomas do usuário após o pré-processamento.
"""
def preprocess_user_symptoms(user_symptoms, symptom_mapping):
    try:
        return [symptom_mapping[str(symptom.strip())] for symptom in user_symptoms.split(',')]
    except KeyError as e:
        print(f"Sintoma não reconhecido: {e}")
        return []


"""
Pré-processa os dados de treinamento.

Parâmetros:
data (dict): Dados carregados do arquivo JSON.
symptom_mapping (dict): Dicionário que mapeia sintomas para seus números correspondentes.

Retorna:
tuple: Tupla contendo duas listas - uma com os sintomas de treinamento e outra com os rótulos de doenças correspondentes.
"""
def preprocess_training_data(data, symptom_mapping):
    all_symptoms = []
    all_labels = []
    for entry in data[0]['data']:
        symptoms = [symptom_mapping[str(symptom)]
                    for symptom in entry['symptoms']]
        all_symptoms.append(symptoms)
        all_labels.append(entry['disease'])
    return all_symptoms, all_labels
