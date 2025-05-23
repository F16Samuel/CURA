import google.generativeai as genai
import test
import ast

# Secure API Key (Store in Environment Variables Instead)
genai.configure(api_key="AIzaSyASjCwVvZUCK6WdC03nQm-1pM8aSAy5WCo")

model = genai.GenerativeModel('gemini-1.5-flash')

context = {' abdominal_pain': 0, ' abnormal_menstruation': 1, ' acidity': 2, ' acute_liver_failure': 3, ' altered_sensorium': 4, ' anxiety': 5, ' back_pain': 6, ' belly_pain': 7, ' blackheads': 8, ' bladder_discomfort': 9, ' blister': 10, ' blood_in_sputum': 11, ' bloody_stool': 12, ' blurred_and_distorted_vision': 13, ' breathlessness': 14, ' brittle_nails': 15, ' bruising': 16, ' burning_micturition': 17, ' chest_pain': 18, ' chills': 19, ' cold_hands_and_feets': 20, ' coma': 21, ' congestion': 22, ' constipation': 23, ' continuous_feel_of_urine': 24, ' continuous_sneezing': 25, ' cough': 26, ' cramps': 27, ' dark_urine': 28, ' dehydration': 29, ' depression': 30, ' diarrhoea': 31, ' dischromic _patches': 32, ' distention_of_abdomen': 33, ' dizziness': 34, ' drying_and_tingling_lips': 35, ' enlarged_thyroid': 36, ' excessive_hunger': 37, ' extra_marital_contacts': 38, ' family_history': 39, ' fast_heart_rate': 40, ' fatigue': 41, ' fluid_overload': 42, ' foul_smell_of urine': 43, ' headache': 44, ' high_fever': 45, ' hip_joint_pain': 46, ' history_of_alcohol_consumption': 47, ' increased_appetite': 48, ' indigestion': 49, ' inflammatory_nails': 50, ' internal_itching': 51, ' irregular_sugar_level': 52, ' irritability': 53, ' irritation_in_anus': 54, ' joint_pain': 55, ' knee_pain': 56, ' lack_of_concentration': 57, ' lethargy': 58, ' loss_of_appetite': 59, ' loss_of_balance': 60, ' loss_of_smell': 61, ' malaise': 62, ' mild_fever': 63, ' mood_swings': 64, ' movement_stiffness': 65, ' mucoid_sputum': 66, ' muscle_pain': 67, ' muscle_wasting': 68, ' muscle_weakness': 69, ' nausea': 70, ' neck_pain': 71, ' nodal_skin_eruptions': 72, ' obesity': 73, ' pain_behind_the_eyes': 74, ' pain_during_bowel_movements': 75, ' pain_in_anal_region': 76, ' painful_walking': 77, ' palpitations': 78, ' passage_of_gases': 79, ' patches_in_throat': 80, ' phlegm': 81, ' polyuria': 82, ' prominent_veins_on_calf': 83, ' puffy_face_and_eyes': 84, ' pus_filled_pimples': 85, ' receiving_blood_transfusion': 86, ' receiving_unsterile_injections': 87, ' red_sore_around_nose': 88, ' red_spots_over_body': 89, ' redness_of_eyes': 90, ' restlessness': 91, ' runny_nose': 92, ' rusty_sputum': 93, ' scurring': 94, ' shivering': 95, ' silver_like_dusting': 96, ' sinus_pressure': 97, ' skin_peeling': 98, ' skin_rash': 99, ' slurred_speech': 100, ' small_dents_in_nails': 101, ' spinning_movements': 102, ' spotting_ urination': 103, ' stiff_neck': 104, ' stomach_bleeding': 105, ' stomach_pain': 106, ' sunken_eyes': 107, ' sweating': 108, ' swelled_lymph_nodes': 109, ' swelling_joints': 110, ' swelling_of_stomach': 111, ' swollen_blood_vessels': 112, ' swollen_extremeties': 113, ' swollen_legs': 114, ' throat_irritation': 115, ' toxic_look_(typhos)': 116, ' ulcers_on_tongue': 117, ' unsteadiness': 118, ' visual_disturbances': 119, ' vomiting': 120, ' watering_from_eyes': 121, ' weakness_in_limbs': 122, ' weakness_of_one_body_side': 123, ' weight_gain': 124, ' weight_loss': 125, ' yellow_crust_ooze': 126, ' yellow_urine': 127, ' yellowing_of_eyes': 128, ' yellowish_skin': 129, '(vertigo) Paroymsal  Positional Vertigo': 130, 'AIDS': 131, 'Acne': 132, 'Alcoholic hepatitis': 133, 'Allergy': 134, 'Arthritis': 135, 'Bronchial Asthma': 136, 'Cervical spondylosis': 137, 'Chicken pox': 138, 'Chronic cholestasis': 139, 'Common Cold': 140, 'Dengue': 141, 'Diabetes ': 142, 'Dimorphic hemmorhoids(piles)': 143, 'Drug Reaction': 144, 'Fungal infection': 145, 'GERD': 146, 'Gastroenteritis': 147, 'Heart attack': 148, 'Hepatitis B': 149, 'Hepatitis C': 150, 'Hepatitis D': 151, 'Hepatitis E': 152, 'Hypertension ': 153, 'Hyperthyroidism': 154, 'Hypoglycemia': 155, 'Hypothyroidism': 156, 'Impetigo': 157, 'Jaundice': 158, 'Malaria': 159, 'Migraine': 160, 'Osteoarthristis': 161, 'Paralysis (brain hemorrhage)': 162, 'Peptic ulcer diseae': 163, 'Pneumonia': 164, 'Psoriasis': 165, 'Tuberculosis': 166, 'Typhoid': 167, 'Urinary tract infection': 168, 'Varicose veins': 169, 'hepatitis A': 170, 'itching': 171}
context_string = "\n".join([f"{key}: {value}" for key, value in context.items()])

def generate_symptoms(user_text):
    prompt = f"""
    You are given the following symptom dictionary:
    {context_string}
    
    The user will describe their symptoms. Your task is to return a Python list containing only the key numbers of the symptoms that match the user's input.
    
    Respond **ONLY** with a valid Python list of numbers and nothing else.

    User input: "{user_text}"
    """

    response = model.generate_content(prompt)

    try:
        key_numbers = ast.literal_eval(response.text.strip())
        if isinstance(key_numbers, list) and all(isinstance(i, int) for i in key_numbers):
            return key_numbers
    except (SyntaxError, ValueError):
        return []

# Example input
user_input = "eyes feel burning, headache, and fever"
symptom_keys = generate_symptoms(user_input)
final_output = test.predict_disease(symptom_keys)
print(final_output)


