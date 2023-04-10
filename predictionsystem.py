import pickle
import streamlit as st
from PIL import Image


from streamlit_option_menu import option_menu

## loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

## navigate the sidebar

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)

## diabetes prediction page

if (selected == 'Diabetes Prediction'):
    st.title("Diabetes Prediction System: Harnessing the Power of Machine Learning")
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

    st.header("Diabetes and its Causes")

    image = Image.open('Images/diabetes1.jpg')

    st.image(image, caption='Diabetes Awareness: Know the Risks and Take Action')

    st.markdown("Diabetes is a chronic condition that affects how your body converts food into energy. "
                 "When you eat, your body breaks down carbohydrates into glucose, which is then transported to "
                 "your cells to be used as energy. However, in people with diabetes, the glucose is not "
                 "properly transported to the cells due to insufficient insulin production or insulin resistance. "
                 "This results in high levels of glucose in the blood, which can cause damage to the organs and tissues "
                 "over time.")
    st.markdown("Several factors can increase the risk of developing diabetes, including:")
    st.markdown("**Number of pregnancies**: Women who have had multiple pregnancies may be at an increased "
                "risk of developing gestational diabetes, a type of diabetes that occurs during pregnancy.")
    st.markdown("**Blood pressure**: High blood pressure can damage the blood vessels and increase the risk of "
                "developing diabetes.")
    st.markdown("**Glucose levels**: High levels of glucose in the blood can cause damage to the organs and "
                "tissues over time, leading to diabetes.")
    st.markdown("**Skin thickness**: Insulin resistance can cause thickening of the skin, which can contribute "
                "to the development of diabetes.")
    st.markdown("**Insulin levels**: Insulin is a hormone that regulates blood sugar levels. Insufficient insulin "
                "production or insulin resistance can lead to diabetes.")
    st.markdown("**BMI**: A high body mass index (BMI) is associated with an increased risk of developing diabetes.")
    st.markdown("**Diabetes Pedigree Function**: This is a measure of the genetic risk for diabetes based on "
                "family history.")
    st.markdown("**Age**: The risk of developing diabetes increases with age, particularly after the age of 45.")

    st.header("Prevention")
    image = Image.open('Images/diabetes2.jpg')

    st.image(image, caption='Preventing diabetes starts with making healthy choices every day.')
    st.markdown("Here are some steps for prevention of diabetes:")
    st.markdown("**Maintain a healthy weight**: Being overweight or obese can increase your risk of developing diabetes, "
                "especially type 2 diabetes. Losing even a small amount of weight, such as 5-7% of your body weight, "
                "can help reduce your risk.")
    st.markdown("**Make healthy food choices**: Eating a diet that's low in saturated and trans fats, cholesterol, and "
                "added sugars, while being rich in whole grains, fruits, vegetables, and lean protein sources "
                "can help you maintain a healthy weight and lower your risk of diabetes.")
    st.markdown("**Stay physically active**: Regular exercise can help you maintain a healthy weight, lower your blood "
                "sugar levels, and improve your body's ability to use insulin. Aim for at least 30 minutes of "
                "moderate-intensity exercise most days of the week.")
    st.markdown("**Monitor your blood sugar levels**: If you have a family history of diabetes or other risk factors, "
                "such as being overweight or having high blood pressure or cholesterol, it's important to monitor your "
                "blood sugar levels regularly. This can help you catch any changes early on and take steps to "
                "prevent diabetes.")
    st.markdown("**Manage stress**: Chronic stress can raise your blood sugar levels and increase your risk of developing "
                "diabetes. Finding healthy ways to manage stress, such as through exercise, meditation, or spending "
                "time with friends and family, can help.")
    st.markdown("**Quit smoking**: Smoking is a known risk factor for many health problems, including diabetes. "
                "If you smoke, talk to your doctor about quitting.")
    st.header("Get a Comprehensive Health Assessment from a Doctor")
    st.markdown("Although our machine learning model can provide an estimate of your risk for developing diabetes, "
                "it's important to remember that it can't always predict with 100% accuracy. "
                "That's why we strongly recommend that you speak with a healthcare professional "
                "if you're concerned about your risk for diabetes.")
    st.markdown("A doctor can perform additional tests and assessments to provide you with a more accurate "
                "diagnosis and personalized recommendations for prevention or management. "
                "No online tool or algorithm can replace the expertise and guidance of a trained healthcare professional.")
    st.markdown("**Remember, early detection and intervention are key to preventing and managing diabetes. "
                "Don't hesitate to speak with a doctor "
                "if you have any concerns about your health.**")
### heart disease prediction
if (selected == 'Heart Disease Prediction'):
    st.title("Your heart matters: predict your disease risk")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')


    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Test Result'):
        heart_prediction = heart_model.predict(
            [[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), float(thalach), int(exang),
              float(oldpeak), int(slope),
              int(ca), int(thal)]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The individual has been diagnosed with heart disease'
        else:
            heart_diagnosis = 'The individual has not been diagnosed with heart disease'

    st.success(heart_diagnosis)

    st.header("Cardiovascular Disease and its causes")

    image = Image.open('Images/heart1.jpg')

    st.image(image, caption='Understanding the causes of heart disease is the first step to prevention.')

    st.markdown("Heart disease, also known as cardiovascular disease, refers to a group of conditions that affect "
                "the heart and blood vessels. Some common types of heart disease include coronary artery disease, "
                "heart failure, and arrhythmias. Several factors can contribute to the development of heart disease, "
                "including age, sex, chest pain types, resting blood pressure, cholesterol levels, and fasting "
                "blood sugar.")
    st.markdown("**Age**: As people age, the risk of developing heart disease increases. This is because the arteries"
                " that supply blood to the heart can become narrower and less flexible over time, making it "
                "harder for the heart to pump blood effectively.")
    st.markdown("**Sex**: Men are more likely to develop heart disease at a younger age than women. "
                "However, women are more likely to develop heart disease after menopause, when their "
                "levels of estrogen decrease.")
    st.markdown("**Chest pain types**: Chest pain can be a symptom of several types of heart disease, "
                "including angina and heart attack. The type of chest pain can indicate the severity "
                "of the condition and the type of treatment that may be necessary.")
    st.markdown("**Resting blood pressure**: High blood pressure, also known as hypertension, "
                "can damage the arteries that supply blood to the heart and increase the risk of heart disease.")
    st.markdown("**Cholesterol levels**: High levels of LDL, or bad cholesterol, can lead to the buildup of plaque in "
                "the arteries, increasing the risk of heart disease.")
    st.markdown("**Fasting blood sugar**: High levels of fasting blood sugar, or hyperglycemia, can be a sign of diabetes. "
                "People with diabetes are at a higher risk of developing heart disease.")
    st.header("Prevention")
    image = Image.open('Images/heart2.jpg')

    st.image(image, caption='Your heart is worth the effort. Take steps to prevent heart disease today.')

    st.markdown("There are several measures that individuals can take to prevent heart disease, including:")
    st.markdown("**Healthy diet**: Eating a balanced diet that is rich in fruits, vegetables, whole grains, and "
                "lean proteins can help to lower the risk of heart disease. It is also important to limit the "
                "intake of saturated and trans fats, added sugars, and sodium.")
    st.markdown("**Regular exercise**: Engaging in regular physical activity, such as brisk walking, jogging, "
                "cycling, or swimming, can help to improve heart health and lower the risk of heart disease.")
    st.markdown("**Maintaining a healthy weight**: Being overweight or obese can increase the risk of heart disease, "
                "so it is important to maintain a healthy weight through a combination of healthy eating and "
                "regular exercise.")
    st.markdown("**Managing stress**: Chronic stress can contribute to the development of heart disease, "
                "so finding ways to manage stress, such as through meditation, yoga, or deep breathing exercises, "
                "can be beneficial.")
    st.markdown("**Avoiding smoking**: Smoking can damage the arteries that supply blood to the heart and increase "
                "the risk of heart disease, so avoiding smoking and exposure to secondhand smoke is important.")
    st.markdown("**Limiting alcohol intake**: Drinking too much alcohol can increase blood pressure and contribute "
                "to the development of heart disease, so it is important to limit alcohol intake to moderate levels.")
    st.markdown("**Regular check-ups**: Regular health check-ups can help to detect early signs of heart disease "
                "and enable early intervention to prevent or manage the condition.")
    st.header("Get a Comprehensive Health Assessment from a Doctor")
    st.markdown("Although our machine learning model can provide an estimate of your risk for developing heart disease, "
                "it's important to remember that it can't always predict with 100% accuracy. "
                "That's why we strongly recommend that you speak with a healthcare professional "
                "if you're concerned about your risk for diabetes.")
    st.markdown("A doctor can perform additional tests and assessments to provide you with a more accurate "
                "diagnosis and personalized recommendations for prevention or management. "
                "No online tool or algorithm can replace the expertise and guidance of a trained healthcare professional.")
    st.markdown("**Remember, early detection and intervention are key to preventing and managing diabetes. "
                "Don't hesitate to speak with a doctor "
                "if you have any concerns about your health.**")

## parkinsons prediction
if (selected == 'Parkinsons Prediction'):
    st.title("Advancing Parkinson's diagnosis through AI.")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

    st.header("Parkinsons's Disease and its causes")

    image = Image.open('Images/parkinson1.jpg')

    st.image(image, caption='Parkinson disease: A progressive neurological disorder that affects movement, balance, '
                            'and coordination.')
    st.markdown("Parkinson's disease is a progressive neurological disorder that affects movement. "
                "It occurs when there is a loss of dopamine-producing cells in the brain. "
                "Dopamine is a neurotransmitter that helps regulate movement, so a decrease in dopamine leads to "
                "symptoms such as tremors, stiffness, and difficulty with balance and coordination.")
    st.markdown("**Some of the factors that can influence the development of Parkinson's disease and their effects:**")
    st.markdown("**Age**: The risk of developing Parkinson's disease increases with age. "
                "The disease is rare in people under 50 and becomes more common as people get older.")
    st.markdown("**Genetics**: There are several genes that have been associated with an increased risk of "
                "Parkinson's disease. Mutations in the LRRK2, SNCA, and PARK2 genes, for example, have been "
                "linked to an increased risk.")
    st.markdown("**Environmental factors**: Exposure to certain environmental toxins, such as pesticides and herbicides, "
                "has been associated with an increased risk of Parkinson's disease. "
                "Head injuries and other forms of trauma to the brain have also been linked to an increased risk.")
    st.markdown("**Gender**: Parkinson's disease is slightly more common in men than women.")
    st.markdown("**Medications**: Certain medications, such as antipsychotic drugs, have been linked to an increased "
                "risk of Parkinson's disease.")
    st.markdown("**Lifestyle factors**: Some studies suggest that regular exercise may help reduce the risk of Parkinson's "
                "disease. In addition, smoking and caffeine consumption have been associated with a lower risk of "
                "developing the disease.")

    st.markdown("It's worth noting that not everyone who has these risk factors will develop Parkinson's disease, "
                "and not everyone who develops the disease has these risk factors. Parkinson's disease is a complex "
                "condition that can have many different contributing factors.")

    st.header("Parkinsons prediction and its causes.")

    image = Image.open('Images/parkinson2.jpg')

    st.image(image, caption='Prevention is key: Maintaining a healthy lifestyle may help reduce the risk of '
                            'Parkinsons disease.')

    st.markdown("There is no guaranteed way to prevent Parkinson's disease, but there are several measures "
                "that may reduce the risk of developing the condition or delay its onset. "
                "Here are some preventive measures that may help:")

    st.markdown("**Exercise regularly**: Exercise has been shown to be beneficial in reducing the risk of Parkinson's disease. "
                "Aim for at least 30 minutes of physical activity per day.")

    st.markdown("**Follow a healthy diet**: A diet rich in fruits, vegetables, whole grains, and lean proteins may "
                "reduce the risk of Parkinson's disease.")
    st.markdown("**Get enough sleep**: Aim for at least seven hours of sleep per night. Lack of sleep has been linked "
                "to a higher risk of developing Parkinson's disease.")
    st.markdown("**Protect your head**: Head injuries have been linked to an increased risk of Parkinson's disease. "
                "Wear a helmet when participating in activities that may result in head injury, such as "
                "cycling or skiing.")
    st.markdown("**Avoid exposure to toxins**: Exposure to certain toxins, such as pesticides and industrial chemicals, "
                "has been linked to an increased risk of Parkinson's disease. "
                "Take steps to avoid exposure to these toxins whenever possible.")
    st.markdown("**Stay mentally active**: Keeping your brain active with activities such as reading, playing games, "
                "and doing puzzles may help reduce the risk of Parkinson's disease.")
    st.markdown("**Manage stress**: Stress has been linked to an increased risk of Parkinson's disease. "
                "Take steps to manage your stress levels, such as practicing relaxation techniques, getting "
                "regular exercise, and seeking support from family and friends.")

    st.markdown("It's important to remember that while these measures may reduce the risk of Parkinson's disease, "
                "they cannot guarantee prevention. If you are concerned about your risk of developing Parkinson's disease, "
                "talk to your doctor.")

    st.header("Get a Comprehensive Health Assessment from a Doctor")
    st.markdown(
        "Although our machine learning model can provide an estimate of your risk for developing heart disease, "
        "it's important to remember that it can't always predict with 100% accuracy. "
        "That's why we strongly recommend that you speak with a healthcare professional "
        "if you're concerned about your risk for diabetes.")
    st.markdown("A doctor can perform additional tests and assessments to provide you with a more accurate "
                "diagnosis and personalized recommendations for prevention or management. "
                "No online tool or algorithm can replace the expertise and guidance of a trained healthcare professional.")
    st.markdown("**Remember, early detection and intervention are key to preventing and managing diabetes. "
                "Don't hesitate to speak with a doctor "
                "if you have any concerns about your health.**")









