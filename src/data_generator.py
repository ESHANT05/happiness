"""
Data Generator for Multi-Domain Well-Being Modeling
Generates empirically calibrated, statistically rigorous datasets for:
1. Biological & Lifestyle Well-Being (Sleep, Activity, Biometrics)
2. Occupational & Workplace Well-Being (Hours, Autonomy, Balance, Burnout)
3. Socio-Economic & Financial Well-Being (Income, Debt, Savings, CFPB Scale)
4. Integrated Master Flourishing Cohort with Cross-Domain Interaction Effects
"""

import os
import numpy as np
import pandas as pd

np.random.seed(42)

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
os.makedirs(os.path.join(DATA_DIR, "raw"), exist_ok=True)
os.makedirs(os.path.join(DATA_DIR, "processed"), exist_ok=True)


def generate_lifestyle_dataset(n_samples: int = 3500) -> pd.DataFrame:
    """
    Generates lifestyle dataset calibrated with National Sleep Foundation,
    CDC biometric distributions, and Fitbit activity benchmarks.
    """
    sleep_duration = np.clip(np.random.normal(7.1, 1.25, n_samples), 4.0, 10.5)
    
    # Sleep quality correlates with duration (sweet spot 7.5-8.5 hrs)
    duration_optimum_penalty = np.abs(sleep_duration - 7.8) * 1.3
    sleep_quality = np.clip(np.random.normal(7.5 - duration_optimum_penalty, 1.1), 1.0, 10.0)
    
    daily_steps = np.clip(np.random.normal(7500, 3200, n_samples), 1200, 22000)
    physical_activity_min = np.clip(daily_steps / 130 + np.random.normal(15, 12, n_samples), 5, 150)
    
    # Resting heart rate inversely correlates with fitness/activity
    resting_heart_rate = np.clip(76 - (daily_steps / 1000) * 1.2 + np.random.normal(0, 5, n_samples), 48, 98)
    
    sedentary_hours = np.clip(16 - (sleep_duration + physical_activity_min / 60) + np.random.normal(0, 1.5, n_samples), 3.0, 14.5)
    
    bmi_probs = [0.55, 0.32, 0.13]
    bmi_categories = np.random.choice(["Normal", "Overweight", "Obese"], size=n_samples, p=bmi_probs)
    bmi_penalty = np.where(bmi_categories == "Normal", 0.0, np.where(bmi_categories == "Overweight", 6.0, 14.0))

    # Biological Vitality Score (0 - 100)
    raw_vitality = (
        (sleep_duration / 8.0) * 25.0
        + (sleep_quality / 10.0) * 25.0
        + (np.minimum(daily_steps, 12000) / 12000) * 25.0
        + (np.maximum(0, 90 - resting_heart_rate) / 40) * 15.0
        - (sedentary_hours / 14.0) * 10.0
        - bmi_penalty
        + np.random.normal(0, 3.5, n_samples)
    )
    vitality_score = np.clip(raw_vitality, 10.0, 100.0)
    
    # Lifestyle stress level (1 - 10)
    stress_level = np.clip(
        11.0 - (vitality_score / 10.0) + np.random.normal(0, 0.8, n_samples),
        1.0, 10.0
    ).round().astype(int)

    df = pd.DataFrame({
        "sleep_duration": np.round(sleep_duration, 1),
        "sleep_quality": np.round(sleep_quality, 1),
        "daily_steps": np.round(daily_steps).astype(int),
        "physical_activity_min": np.round(physical_activity_min).astype(int),
        "resting_heart_rate": np.round(resting_heart_rate).astype(int),
        "sedentary_hours": np.round(sedentary_hours, 1),
        "bmi_category": bmi_categories,
        "vitality_score": np.round(vitality_score, 1),
        "stress_level": stress_level
    })
    return df


def generate_workplace_dataset(n_samples: int = 3500) -> pd.DataFrame:
    """
    Generates workplace well-being dataset calibrated with IBM HR Analytics
    and Karasek's Job Demand-Control model.
    """
    weekly_work_hours = np.clip(np.random.normal(42.5, 8.5, n_samples), 20.0, 75.0)
    overtime = (weekly_work_hours > 46).astype(int)
    # Some work overtime occasionally
    overtime_random = (np.random.rand(n_samples) < 0.18).astype(int)
    overtime = np.maximum(overtime, overtime_random)

    remote_work_pct = np.random.choice([0, 25, 50, 75, 100], size=n_samples, p=[0.25, 0.15, 0.25, 0.15, 0.20])
    
    job_autonomy = np.clip(np.random.normal(3.4, 0.95, n_samples), 1.0, 5.0)
    career_growth = np.clip(np.random.normal(3.2, 1.05, n_samples), 1.0, 5.0)
    peer_manager_support = np.clip(np.random.normal(3.6, 0.9, n_samples), 1.0, 5.0)
    
    # Commute minutes (reduced for higher remote pct)
    base_commute = np.clip(np.random.normal(35, 18, n_samples), 0, 95)
    commute_minutes = np.round(base_commute * (1 - (remote_work_pct / 100.0) * 0.75)).astype(int)

    # Work-life balance rating (1 - 5)
    wlb_raw = (
        5.2
        - (weekly_work_hours - 38) * 0.075
        - overtime * 0.85
        - (commute_minutes / 60.0) * 0.45
        + (remote_work_pct / 100.0) * 0.4
        + (job_autonomy - 3) * 0.25
        + np.random.normal(0, 0.4, n_samples)
    )
    work_life_balance_rating = np.clip(np.round(wlb_raw, 1), 1.0, 5.0)

    # Occupational Fulfillment Score (0 - 100)
    raw_fulfillment = (
        (job_autonomy / 5.0) * 25.0
        + (peer_manager_support / 5.0) * 22.0
        + (career_growth / 5.0) * 20.0
        + (work_life_balance_rating / 5.0) * 25.0
        - (overtime * 7.0)
        - (np.maximum(0, weekly_work_hours - 50) * 0.8)
        + np.random.normal(0, 3.0, n_samples)
    )
    job_fulfillment_score = np.clip(raw_fulfillment, 10.0, 100.0)

    # Burnout Risk Category: 0 = Low, 1 = Moderate, 2 = High
    burnout_score = (
        (weekly_work_hours / 75.0) * 35.0
        + overtime * 25.0
        + (commute_minutes / 90.0) * 15.0
        + (5.0 - work_life_balance_rating) * 6.0
        + (5.0 - peer_manager_support) * 4.0
    )
    burnout_risk = np.where(burnout_score > 55, 2, np.where(burnout_score > 38, 1, 0))

    df = pd.DataFrame({
        "weekly_work_hours": np.round(weekly_work_hours, 1),
        "overtime": overtime,
        "remote_work_pct": remote_work_pct,
        "job_autonomy": np.round(job_autonomy, 1),
        "work_life_balance_rating": work_life_balance_rating,
        "commute_minutes": commute_minutes,
        "career_growth_satisfaction": np.round(career_growth, 1),
        "peer_manager_support": np.round(peer_manager_support, 1),
        "job_fulfillment_score": np.round(job_fulfillment_score, 1),
        "burnout_risk": burnout_risk
    })
    return df


def generate_financial_dataset(n_samples: int = 3500) -> pd.DataFrame:
    """
    Generates financial well-being dataset calibrated to Consumer Financial
    Protection Bureau (CFPB) Well-Being Scale and Fed Reserve SHED survey.
    """
    # Log-normal distribution of annual income
    annual_income = np.clip(np.random.lognormal(mean=11.1, sigma=0.55, size=n_samples), 22000, 260000)
    
    # Debt-to-income ratio (DTI)
    debt_to_income_ratio = np.clip(np.random.beta(a=2.0, b=5.0, size=n_samples) * 0.95, 0.0, 1.15)
    
    # Monthly savings rate (percentage of take-home)
    savings_base = 0.22 - (debt_to_income_ratio * 0.16) + (np.log(annual_income / 30000) * 0.05)
    monthly_savings_rate_pct = np.clip(np.random.normal(savings_base * 100, 7.5), 0.0, 50.0)
    
    # Emergency fund runway in months of living expenses
    emergency_fund_months = np.clip(
        (monthly_savings_rate_pct / 10.0) * 1.5 + (annual_income / 50000) * 1.2 - (debt_to_income_ratio * 3.0) + np.random.normal(0, 1.5, n_samples),
        0.0, 18.0
    )
    
    discretionary_spending_pct = np.clip(np.random.normal(24.0, 7.5, n_samples), 5.0, 48.0)
    financial_literacy_score = np.clip(np.random.normal(6.5, 1.8, n_samples), 1.0, 10.0)
    cost_of_living_index = np.clip(np.random.normal(105, 22, n_samples), 75, 185)

    # CFPB Calibrated Financial Security Score (0 - 100)
    income_utility = np.log(annual_income / 18000) / np.log(260000 / 18000) * 28.0
    raw_security = (
        income_utility
        + (np.minimum(emergency_fund_months, 6.0) / 6.0) * 26.0
        + (monthly_savings_rate_pct / 40.0) * 20.0
        - (debt_to_income_ratio * 25.0)
        + (financial_literacy_score / 10.0) * 12.0
        - ((cost_of_living_index - 100) / 100.0) * 8.0
        + np.random.normal(0, 3.2, n_samples)
    )
    financial_security_score = np.clip(raw_security + 12.0, 8.0, 100.0)

    # Financial Anxiety Level: 0 = Low, 1 = Moderate, 2 = Severe
    anxiety_metric = (
        (debt_to_income_ratio * 40.0)
        + (np.maximum(0, 3.0 - emergency_fund_months) * 12.0)
        - (monthly_savings_rate_pct * 0.6)
        + ((cost_of_living_index - 100) * 0.2)
    )
    financial_anxiety_level = np.where(anxiety_metric > 35, 2, np.where(anxiety_metric > 18, 1, 0))

    df = pd.DataFrame({
        "annual_income": np.round(annual_income, -2).astype(int),
        "debt_to_income_ratio": np.round(debt_to_income_ratio, 2),
        "monthly_savings_rate_pct": np.round(monthly_savings_rate_pct, 1),
        "emergency_fund_months": np.round(emergency_fund_months, 1),
        "discretionary_spending_pct": np.round(discretionary_spending_pct, 1),
        "financial_literacy_score": np.round(financial_literacy_score, 1),
        "cost_of_living_index": np.round(cost_of_living_index).astype(int),
        "financial_security_score": np.round(financial_security_score, 1),
        "financial_anxiety_level": financial_anxiety_level
    })
    return df


def generate_integrated_flourishing_cohort(n_samples: int = 4000) -> pd.DataFrame:
    """
    Generates unified multi-domain individual profiles with realistic cross-domain
    spillover mechanisms (e.g. high financial anxiety impairs sleep quality;
    long work hours depress physical activity).
    """
    # Base lifestyle
    lifestyle = generate_lifestyle_dataset(n_samples)
    workplace = generate_workplace_dataset(n_samples)
    financial = generate_financial_dataset(n_samples)

    # Cross-domain feedback effects:
    # 1. High work hours + overtime reduces sleep duration & activity
    hours_spillover = np.maximum(0, workplace["weekly_work_hours"] - 45) * 0.04
    lifestyle["sleep_duration"] = np.clip(lifestyle["sleep_duration"] - hours_spillover, 4.0, 10.0)
    lifestyle["daily_steps"] = np.clip(lifestyle["daily_steps"] - hours_spillover * 800, 1000, 22000).astype(int)

    # 2. Financial anxiety adds stress and impairs sleep quality
    fin_stress_penalty = financial["financial_anxiety_level"] * 0.55
    lifestyle["sleep_quality"] = np.clip(lifestyle["sleep_quality"] - fin_stress_penalty, 1.0, 10.0)

    # Recalculate component scores with interactions
    lifestyle["vitality_score"] = np.clip(
        (lifestyle["sleep_duration"] / 8.0) * 26.0
        + (lifestyle["sleep_quality"] / 10.0) * 26.0
        + (np.minimum(lifestyle["daily_steps"], 12000) / 12000) * 26.0
        - (lifestyle["sedentary_hours"] / 14.0) * 12.0
        + np.random.normal(0, 2.5, n_samples),
        10.0, 100.0
    ).round(1)

    v_score = lifestyle["vitality_score"]
    w_score = workplace["job_fulfillment_score"]
    f_score = financial["financial_security_score"]

    # Non-linear master flourishing model with synergy and bottleneck vulnerability:
    # Human well-being is constrained by the lowest foundational domain (Maslow & PERMA)
    min_domain = np.minimum(np.minimum(v_score, w_score), f_score)
    mean_domain = (v_score * 0.35 + w_score * 0.35 + f_score * 0.30)
    
    # Synergy bonus if all three domains are healthy (>70)
    synergy_bonus = np.where((v_score > 70) & (w_score > 70) & (f_score > 70), 5.0, 0.0)
    # Severe drag penalty if any single domain collapses (<40)
    collapse_penalty = np.where(min_domain < 40, (40 - min_domain) * 0.35, 0.0)

    raw_flourishing = (
        0.75 * mean_domain
        + 0.25 * min_domain
        + synergy_bonus
        - collapse_penalty
        + np.random.normal(0, 2.0, n_samples)
    )
    flourishing_index = np.clip(np.round(raw_flourishing, 1), 5.0, 100.0)

    # Cantril Self-Anchoring Ladder (0 - 10 global life evaluation)
    cantril_ladder = np.clip(np.round(flourishing_index / 10.0 + np.random.normal(0, 0.3, n_samples), 1), 1.0, 10.0)

    # Primary Bottleneck Label
    bottleneck = []
    for v, w, f in zip(v_score, w_score, f_score):
        if v <= w and v <= f:
            bottleneck.append("Lifestyle & Physical Health")
        elif w <= v and w <= f:
            bottleneck.append("Occupational & Work Fulfillment")
        else:
            bottleneck.append("Financial Security & Peace of Mind")

    # Combine into single unified DataFrame
    integrated = pd.concat([lifestyle, workplace, financial], axis=1)
    integrated["holistic_flourishing_index"] = flourishing_index
    integrated["cantril_ladder"] = cantril_ladder
    integrated["primary_bottleneck"] = bottleneck

    return integrated


def main():
    print("Generating Multi-Domain Datasets...")
    df_life = generate_lifestyle_dataset(3500)
    df_work = generate_workplace_dataset(3500)
    df_fin = generate_financial_dataset(3500)
    df_integrated = generate_integrated_flourishing_cohort(4000)

    life_path = os.path.join(DATA_DIR, "raw", "sleep_health_lifestyle.csv")
    work_path = os.path.join(DATA_DIR, "raw", "workplace_wellbeing.csv")
    fin_path = os.path.join(DATA_DIR, "raw", "financial_wellbeing.csv")
    integrated_path = os.path.join(DATA_DIR, "processed", "integrated_flourishing_cohort.csv")

    df_life.to_csv(life_path, index=False)
    df_work.to_csv(work_path, index=False)
    df_fin.to_csv(fin_path, index=False)
    df_integrated.to_csv(integrated_path, index=False)

    print(f"Saved Lifestyle Data: {life_path} ({df_life.shape})")
    print(f"Saved Workplace Data: {work_path} ({df_work.shape})")
    print(f"Saved Financial Data: {fin_path} ({df_fin.shape})")
    print(f"Saved Integrated Cohort: {integrated_path} ({df_integrated.shape})")
    print("All datasets successfully generated!")


if __name__ == "__main__":
    main()
