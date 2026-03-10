from utils import ask_yes_no

def collect_symptoms():

    symptoms = {

    "fever":ask_yes_no("Fever"),
    "cough":ask_yes_no("Cough"),
    "fatigue":ask_yes_no("Fatigue"),
    "headache":ask_yes_no("Headache"),
    "dizziness":ask_yes_no("Dizziness"),
    "nausea":ask_yes_no("Nausea")

    }

    return symptoms
