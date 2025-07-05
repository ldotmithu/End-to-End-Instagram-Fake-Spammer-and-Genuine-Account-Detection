# 📸End-to-End Instagram Fake, Spammer, and Genuine Account Detection


This project is an end-to-end Machine Learning pipeline that classifies Instagram accounts into **Fake** and **Genuine**. It automates the entire ML lifecycle — from data ingestion to model evaluation — and is designed to be modular, scalable, and production-ready.

## 🚀 Project Pipeline Overview

```
📦 artifacts/
│
├── data_ingestion/        ← Raw data collection and optional unzipping
├── data_validation/       ← Schema-based validation
├── data_transformation/   ← Feature engineering and preprocessing
├── trainer/               ← ML model training
└── evaluation/            ← Final model evaluation
```



> 🔍 Place raw data (`.zip` or `.csv`) in `artifacts/data_ingestion/`.
## ⚙️ Project Stages

### ✅ 1. Data Ingestion
- Unzips and loads the dataset.
- Saves as `data.csv` in `artifacts/data_ingestion/`.

### ✅ 2. Data Validation
- Validates using `schema.yaml`.
- Ensures correct column names, types, and no missing values.

### ✅ 3. Data Transformation
- Applies label encoding or one-hot encoding.
- Splits into train/test sets.
- Saves as `.npy` files.

### ✅ 4. Model Training
- Uses `RandomForestClassifier` (configurable in `params.yaml`).
- Saves as `model.pkl`.

### ✅ 5. Model Evaluation
- Reports accuracy, precision, recall, and F1-score.
- Saves metrics in `artifacts/evaluation/`.
- **Note**: Accuracy of 1.0 may indicate overfitting; consider cross-validation.

## 📁 Folder Structure

```
End-to-End-Instagram-Fake-Spammer-and-Genuine-Account-Detection/
├── app.py                       # Streamlit frontend
├── main.py                      # Pipeline runner
├── schema.yaml                  # Schema for validation & transformation
├── parems.yaml                  # Model hyperparameters
├── requirements.txt             # Python dependencies
├── setup.py                     # Setup script
├── artifacts/                   # All pipeline outputs
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transfomation/
│   ├── trainer/
│   └── evaluation/
└── src/
    ├── Config/
    │   └── config_entity.py     # All pipeline config dataclasses
    ├── Pipeline/
    │   └── Stages_of_Pipeline.py
    ├── Utility/
    │   └── common.py            # Utility functions
    └── components/
        ├── data_ingestion.py
        ├── data_validation.py
        ├── data_transfomation.py
        ├── model_trainer.py
        └── model_evaluation.py


```

## 🧪 Model

- **Model Used**: `RandomForestClassifier`
- **Evaluation Accuracy**: `1.0` (Investigate overfitting with cross-validation)
- **Saved As**: `artifacts/trainer/model.pkl`

## 📦 Installation & Running the Project

### ✅ Step 1: Clone the Repository
```bash
git clone https://github.com/ldotmithu/End-to-End-Instagram-Fake-Spammer-and-Genuine-Account-Detection.git
cd End-to-End-Instagram-Fake-Spammer-and-Genuine-Account-Detection
```

### ✅ Step 2: Create Virtual Environment
```bash
conda create -n insta-detector python=3.10 -y
conda activate insta-detector
```

### ✅ Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### ✅ Step 4: Run the Pipeline
```bash
python main.py
```

## 🛠️ Usage Example

To predict an account’s class using the trained model:

```python
import joblib
import pandas as pd

# Load model
model = joblib.load("artifacts/trainer/model.pkl")


# Predict
prediction = model.predict(data)
print(f"Predicted class: {prediction[0]}")  
```

## 💡 Author

**Mithurshan** – [LinkedIn](https://www.linkedin.com/in/mithurshan6) | [GitHub](https://github.com/ldotmithu/)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.