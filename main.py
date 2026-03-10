from menu import menu
from input_module import collect_basic_info
from bmi_module import calculate_bmi
from bmr_module import calculate_bmr
from hydration_module import hydration_score
from cardiovascular_module import cardio_risk
from metabolic_module import diabetes_risk
from health_score_engine import overall_health_score
from history_manager import save_history,load_history
from report_generator import generate_report
from utils import ask_float


while True:

    choice = menu()

    if choice=="1":

        info = collect_basic_info()

        water = ask_float("Daily water intake (L): ")

        exercise = ask_float("Exercise hours per week: ")

        stress = ask_float("Stress level (1-10): ")

        sugar = ask_float("Daily sugar intake (g): ")

        bmi = calculate_bmi(info["weight"],info["height"])

        bmr = calculate_bmr(info["weight"],info["height"],info["age"],info["gender"])

        hydration = hydration_score(water,info["weight"])

        cardio = cardio_risk(info["age"],bmi,exercise,stress)

        diabetes = diabetes_risk(bmi,exercise,sugar)

        health = overall_health_score(bmi,hydration,cardio,diabetes)

        generate_report(info["name"],bmi,bmr,hydration,cardio,diabetes,health)

        save_history({
        "name":info["name"],
        "health_score":health
        })

    elif choice=="2":

        history=load_history()

        for h in history:
            print(h)

    elif choice=="3":

        break
