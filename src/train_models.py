"""
Model Training & Evaluation Pipeline
Trains:
1. Lifestyle/Health Model (RandomForestRegressor & GradientBoosting)
2. Workplace/Occupational Model (GradientBoostingRegressor & RandomForest)
3. Financial/Socio-Economic Model (RandomForestRegressor & Ridge)
4. Master Holistic Human Flourishing Stacking Ensemble
Exports trained artifacts and validation metrics for the interactive dashboard.
"""

import os
import json
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, classification_report

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODELS_DIR, exist_ok=True)


def train_lifestyle_models(data_path: str):
    print("\n--- Training Lifestyle & Biological Well-Being Models ---")
    df = pd.read_csv(data_path)
    
    feature_cols = [
        "sleep_duration", "sleep_quality", "daily_steps",
        "physical_activity_min", "resting_heart_rate",
        "sedentary_hours", "bmi_category"
    ]
    numeric_cols = [
        "sleep_duration", "sleep_quality", "daily_steps",
        "physical_activity_min", "resting_heart_rate", "sedentary_hours"
    ]
    categorical_cols = ["bmi_category"]
    
    X = df[feature_cols]
    y_vitality = df["vitality_score"]
    y_stress = df["stress_level"]
    
    X_train, X_test, y_v_train, y_v_test, y_s_train, y_s_test = train_test_split(
        X, y_vitality, y_stress, test_size=0.2, random_state=42
    )
    
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_cols),
            ("cat", OneHotEncoder(drop="first", sparse_output=False), categorical_cols)
        ]
    )
    
    # Vitality Regressor
    vitality_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=150, max_depth=12, random_state=42))
    ])
    vitality_pipeline.fit(X_train, y_v_train)
    y_v_pred = vitality_pipeline.predict(X_test)
    
    v_r2 = r2_score(y_v_test, y_v_pred)
    v_rmse = np.sqrt(mean_squared_error(y_v_test, y_v_pred))
    v_mae = mean_absolute_error(y_v_test, y_v_pred)
    print(f"Lifestyle Vitality Model: R²={v_r2:.4f}, RMSE={v_rmse:.2f}, MAE={v_mae:.2f}")

    # Stress Classifier
    stress_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42))
    ])
    stress_pipeline.fit(X_train, y_s_train)

    # Feature Importance
    rf_model = vitality_pipeline.named_steps["regressor"]
    ohe_cats = vitality_pipeline.named_steps["preprocessor"].named_transformers_["cat"].get_feature_names_out(categorical_cols)
    all_feature_names = numeric_cols + list(ohe_cats)
    importances = dict(zip(all_feature_names, rf_model.feature_importances_.round(4)))

    bundle = {
        "vitality_pipeline": vitality_pipeline,
        "stress_pipeline": stress_pipeline,
        "features": feature_cols,
        "metrics": {"r2": float(v_r2), "rmse": float(v_rmse), "mae": float(v_mae)},
        "feature_importances": importances
    }
    
    save_path = os.path.join(MODELS_DIR, "health_model.joblib")
    joblib.dump(bundle, save_path)
    print(f"Saved Lifestyle Model Artifacts: {save_path}")
    return bundle


def train_workplace_models(data_path: str):
    print("\n--- Training Workplace & Occupational Well-Being Models ---")
    df = pd.read_csv(data_path)
    
    feature_cols = [
        "weekly_work_hours", "overtime", "remote_work_pct",
        "job_autonomy", "work_life_balance_rating", "commute_minutes",
        "career_growth_satisfaction", "peer_manager_support"
    ]
    
    X = df[feature_cols]
    y_fulfillment = df["job_fulfillment_score"]
    y_burnout = df["burnout_risk"]
    
    X_train, X_test, y_f_train, y_f_test, y_b_train, y_b_test = train_test_split(
        X, y_fulfillment, y_burnout, test_size=0.2, random_state=42
    )
    
    pipeline_fulfillment = Pipeline([
        ("scaler", StandardScaler()),
        ("regressor", GradientBoostingRegressor(n_estimators=150, learning_rate=0.08, max_depth=5, random_state=42))
    ])
    pipeline_fulfillment.fit(X_train, y_f_train)
    y_f_pred = pipeline_fulfillment.predict(X_test)
    
    w_r2 = r2_score(y_f_test, y_f_pred)
    w_rmse = np.sqrt(mean_squared_error(y_f_test, y_f_pred))
    w_mae = mean_absolute_error(y_f_test, y_f_pred)
    print(f"Work Fulfillment Model: R²={w_r2:.4f}, RMSE={w_rmse:.2f}, MAE={w_mae:.2f}")

    # Burnout Classifier
    pipeline_burnout = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42))
    ])
    pipeline_burnout.fit(X_train, y_b_train)

    gb_model = pipeline_fulfillment.named_steps["regressor"]
    importances = dict(zip(feature_cols, gb_model.feature_importances_.round(4)))

    bundle = {
        "fulfillment_pipeline": pipeline_fulfillment,
        "burnout_pipeline": pipeline_burnout,
        "features": feature_cols,
        "metrics": {"r2": float(w_r2), "rmse": float(w_rmse), "mae": float(w_mae)},
        "feature_importances": importances
    }
    
    save_path = os.path.join(MODELS_DIR, "work_model.joblib")
    joblib.dump(bundle, save_path)
    print(f"Saved Workplace Model Artifacts: {save_path}")
    return bundle


def train_financial_models(data_path: str):
    print("\n--- Training Financial & Socio-Economic Well-Being Models ---")
    df = pd.read_csv(data_path)
    
    feature_cols = [
        "annual_income", "debt_to_income_ratio", "monthly_savings_rate_pct",
        "emergency_fund_months", "discretionary_spending_pct",
        "financial_literacy_score", "cost_of_living_index"
    ]
    
    X = df[feature_cols]
    y_security = df["financial_security_score"]
    y_anxiety = df["financial_anxiety_level"]
    
    X_train, X_test, y_s_train, y_s_test, y_a_train, y_a_test = train_test_split(
        X, y_security, y_anxiety, test_size=0.2, random_state=42
    )
    
    pipeline_security = Pipeline([
        ("scaler", StandardScaler()),
        ("regressor", RandomForestRegressor(n_estimators=160, max_depth=12, random_state=42))
    ])
    pipeline_security.fit(X_train, y_s_train)
    y_s_pred = pipeline_security.predict(X_test)
    
    f_r2 = r2_score(y_s_test, y_s_pred)
    f_rmse = np.sqrt(mean_squared_error(y_s_test, y_s_pred))
    f_mae = mean_absolute_error(y_s_test, y_s_pred)
    print(f"Financial Security Model: R²={f_r2:.4f}, RMSE={f_rmse:.2f}, MAE={f_mae:.2f}")

    # Anxiety Classifier
    pipeline_anxiety = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42))
    ])
    pipeline_anxiety.fit(X_train, y_a_train)

    rf_model = pipeline_security.named_steps["regressor"]
    importances = dict(zip(feature_cols, rf_model.feature_importances_.round(4)))

    bundle = {
        "security_pipeline": pipeline_security,
        "anxiety_pipeline": pipeline_anxiety,
        "features": feature_cols,
        "metrics": {"r2": float(f_r2), "rmse": float(f_rmse), "mae": float(f_mae)},
        "feature_importances": importances
    }
    
    save_path = os.path.join(MODELS_DIR, "finance_model.joblib")
    joblib.dump(bundle, save_path)
    print(f"Saved Financial Model Artifacts: {save_path}")
    return bundle


def train_master_ensemble(integrated_data_path: str, health_bundle, work_bundle, finance_bundle):
    print("\n--- Training Master Holistic Human Flourishing Stacking Ensemble ---")
    df = pd.read_csv(integrated_data_path)
    
    # Predict sub-domain scores using individual models
    pred_v = health_bundle["vitality_pipeline"].predict(df[health_bundle["features"]])
    pred_w = work_bundle["fulfillment_pipeline"].predict(df[work_bundle["features"]])
    pred_f = finance_bundle["security_pipeline"].predict(df[finance_bundle["features"]])
    
    # Construct Meta-Features for Master Ensemble
    meta_df = pd.DataFrame({
        "pred_vitality": pred_v,
        "pred_fulfillment": pred_w,
        "pred_financial_security": pred_f,
        "mean_domain_score": (pred_v + pred_w + pred_f) / 3.0,
        "min_domain_score": np.minimum(np.minimum(pred_v, pred_w), pred_f),
        "domain_spread": np.maximum(np.maximum(pred_v, pred_w), pred_f) - np.minimum(np.minimum(pred_v, pred_w), pred_f),
        "health_work_synergy": (pred_v * pred_w) / 100.0,
        "fin_health_resilience": (pred_f * pred_v) / 100.0
    })
    
    y_flourish = df["holistic_flourishing_index"]
    y_cantril = df["cantril_ladder"]
    
    X_train, X_test, y_m_train, y_m_test, y_c_train, y_c_test = train_test_split(
        meta_df, y_flourish, y_cantril, test_size=0.2, random_state=42
    )
    
    master_regressor = GradientBoostingRegressor(
        n_estimators=180, learning_rate=0.06, max_depth=5, subsample=0.85, random_state=42
    )
    master_regressor.fit(X_train, y_m_train)
    y_m_pred = master_regressor.predict(X_test)
    
    e_r2 = r2_score(y_m_test, y_m_pred)
    e_rmse = np.sqrt(mean_squared_error(y_m_test, y_m_pred))
    e_mae = mean_absolute_error(y_m_test, y_m_pred)
    print(f"Master Flourishing Ensemble: R²={e_r2:.4f}, RMSE={e_rmse:.2f}, MAE={e_mae:.2f}")

    # Cantril Ladder Regressor
    cantril_regressor = GradientBoostingRegressor(
        n_estimators=120, learning_rate=0.07, max_depth=4, random_state=42
    )
    cantril_regressor.fit(X_train, y_c_train)

    meta_feature_names = list(meta_df.columns)
    master_importances = dict(zip(meta_feature_names, master_regressor.feature_importances_.round(4)))

    bundle = {
        "master_regressor": master_regressor,
        "cantril_regressor": cantril_regressor,
        "meta_features": meta_feature_names,
        "metrics": {"r2": float(e_r2), "rmse": float(e_rmse), "mae": float(e_mae)},
        "feature_importances": master_importances
    }
    
    save_path = os.path.join(MODELS_DIR, "ensemble_flourishing_model.joblib")
    joblib.dump(bundle, save_path)
    print(f"Saved Master Ensemble Model Artifacts: {save_path}")

    # Compile Overall Metrics Report
    summary_report = {
        "project_title": "Predictive Modeling of Personal Well-being using Lifestyle, Occupational, and Financial Data",
        "health_model": {
            "name": "Biological Vitality & Stress Predictor",
            "algorithm": "RandomForestRegressor + Classifier",
            "metrics": health_bundle["metrics"],
            "top_features": health_bundle["feature_importances"]
        },
        "work_model": {
            "name": "Occupational Fulfillment & Burnout Predictor",
            "algorithm": "GradientBoostingRegressor + Classifier",
            "metrics": work_bundle["metrics"],
            "top_features": work_bundle["feature_importances"]
        },
        "finance_model": {
            "name": "CFPB-Calibrated Financial Security Predictor",
            "algorithm": "RandomForestRegressor + Classifier",
            "metrics": finance_bundle["metrics"],
            "top_features": finance_bundle["feature_importances"]
        },
        "master_ensemble": {
            "name": "Holistic Human Flourishing Stacking Ensemble",
            "algorithm": "GradientBoosting Non-Linear Meta-Learner",
            "metrics": bundle["metrics"],
            "top_features": bundle["feature_importances"]
        }
    }
    
    report_path = os.path.join(MODELS_DIR, "metrics_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(summary_report, f, indent=4)
    print(f"Saved System Validation Report: {report_path}")
    return bundle


def main():
    life_data = os.path.join(DATA_DIR, "raw", "sleep_health_lifestyle.csv")
    work_data = os.path.join(DATA_DIR, "raw", "workplace_wellbeing.csv")
    fin_data = os.path.join(DATA_DIR, "raw", "financial_wellbeing.csv")
    integrated_data = os.path.join(DATA_DIR, "processed", "integrated_flourishing_cohort.csv")

    health_bundle = train_lifestyle_models(life_data)
    work_bundle = train_workplace_models(work_data)
    finance_bundle = train_financial_models(fin_data)
    train_master_ensemble(integrated_data, health_bundle, work_bundle, finance_bundle)
    print("\nAll models trained, evaluated, and saved successfully!")


if __name__ == "__main__":
    main()
