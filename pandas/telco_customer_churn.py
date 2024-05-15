import numpy as np
import pandas as pd
import os

from sklearn import metrics
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn.metrics import (
    accuracy_score, classification_report, recall_score, confusion_matrix,
    roc_auc_score, precision_score, f1_score, roc_curve, auc
)
from sklearn.preprocessing import OrdinalEncoder

from catboost import CatBoostClassifier, Pool
pd.set_option('display.max_columns', 40)


data_path = r"D:\data\ML\TelcoCustomerChurn\WA_Fn-UseC_-Telco-Customer-Churn.csv"
df_orig = pd.read_csv(data_path)
df = df_orig.copy()

bool_cols = ['Partner', 'Dependents', 'Churn', 'PhoneService', ]
df['SeniorCitizen'] = df['SeniorCitizen'].astype(int)
for column in bool_cols:
    df[column] = df[column].replace({'No': 0, 'Yes': 1})

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

columns_to_replace = ['MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
for column in columns_to_replace:
    df[column] = df[column].replace('No internet service', 'No')
