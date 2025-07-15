# eda.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda(df):
    # 🎯 Confirm target column and encode
    TARGET_COL = 'Target'  # Change if your column is named differently
    if TARGET_COL not in df.columns:
        print(f"❌ Column '{TARGET_COL}' not found in dataset.")
        print("📋 Available columns:", df.columns.tolist())
        return

    label_mapping = {'Dropout': 0, 'Graduate': 1, 'Enrolled': 2}
    df['Target_Encoded'] = df[TARGET_COL].map(label_mapping)

    # 🟢 Class Distribution
    target_counts = df[TARGET_COL].value_counts(normalize=True).sort_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=target_counts.index, y=target_counts.values)
    plt.title("🎯 Target Class Distribution")
    plt.ylabel("Proportion")
    plt.xlabel("Class Label")
    plt.show()

    print("\n📈 Class Distribution:")
    print(df[TARGET_COL].value_counts())

    # Feature groups
    demographic_cols = ['Gender', 'Age at enrollment', 'Nationality', 'Marital status']
    socioeconomic_cols = ["Scholarship holder", "Father's occupation", "Mother's qualification"]
    academic_cols = [
        'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (approved)',
        'Curricular units 2nd sem (enrolled)', 'Curricular units 2nd sem (approved)'
    ]
    macroeconomic_cols = ['Unemployment rate', 'Inflation rate', 'GDP']

    def plot_feature_distributions(feature_list, title_prefix):
        for col in feature_list:
            if col in df.columns:
                plt.figure(figsize=(7, 4))
                if df[col].dtype in ['object', 'category']:
                    sns.countplot(data=df, x=col, hue=TARGET_COL)
                else:
                    sns.boxplot(data=df, x=TARGET_COL, y=col)
                plt.title(f"{title_prefix}: {col}")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

    plot_feature_distributions(demographic_cols, "🧬 Demographic")
    plot_feature_distributions(socioeconomic_cols, "💰 Socio-Economic")
    plot_feature_distributions(academic_cols, "🎓 Academic")
    plot_feature_distributions(macroeconomic_cols, "🌍 Macroeconomic")

    # Correlation matrix
    numerical_df = df.select_dtypes(include='number')
    if numerical_df.empty:
        print("⚠️ No numeric columns found.")
    else:
        plt.figure(figsize=(12, 10))
        sns.heatmap(numerical_df.corr(), annot=False, cmap='coolwarm', fmt=".2f", center=0)
        plt.title("🔍 Correlation Matrix")
        plt.show()
