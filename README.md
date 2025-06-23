
# 🚗 CO₂ Emission Predictor

This project is a web-based application built with **Streamlit** that predicts vehicle **CO₂ emissions (in g/km)** based on various user-inputted vehicle specifications. It uses a **machine learning model (Ridge Regression)** trained on real-world data from Canadian vehicle emissions.

## 📌 Overview

The app allows users to input vehicle details such as:

- Engine size
- Number of cylinders
- Transmission type
- Fuel type
- Fuel consumption (City, Highway, Combined)

It then uses a trained **linear regression model wrapped in a pipeline** to preprocess the inputs and output an accurate CO₂ emission prediction.


## 🧠 How It Works

1. A CSV dataset containing vehicle specs and emissions data is cleaned and preprocessed.
2. A `Pipeline` is created using:
   - `OneHotEncoder` for categorical features like Make, Vehicle Class, Fuel Type, etc.
   - `Ridge` regression as the prediction model.
3. The pipeline is trained and saved as `model.pkl` using `joblib`.
4. A **Streamlit app (`app.py`)** provides an interactive UI to enter vehicle details.
5. The app loads the trained pipeline and outputs CO₂ emission predictions in real time.


## 🛠 Technologies Used

- **Python**
- **scikit-learn**
- **pandas**
- **numpy**
- **joblib**
- **Streamlit**


## 🚀 How to Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/YOUR-USERNAME/co2-emission-predictor.git
   cd co2-emission-predictor
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

> You can deploy this app for free on [CO2_Emission_Predictor](https://co2-emission-predictor-dveuw46vonjd6z2x3rxfza.streamlit.app/)



## 📩 Contact

For questions or collaborations:

* GitHub: [GitNinja11](https://github.com/GitNinja)
* Email: [vaishnavinewalkar04l@gmail.com](vaishnavinewalkar04l@gmail.com)



