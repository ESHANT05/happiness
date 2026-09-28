"""
Master Inference & Prescriptive AI Engine
Integrates the 3 Domain ML Models into the Holistic Human Flourishing Pipeline.
Features:
- Multi-domain inference
- Non-linear ensemble aggregation
- Happiness Bottleneck Diagnosis
- Counterfactual Optimization ("What-If" Sensitivity Simulator)
- Evidence-based Prescriptive Interventions (PERMA & Behavioral Science)
- Preset Archetypes for Instant Demonstration
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from typing import Dict, Any, Tuple, List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")


class FlourishingPredictor:
    def __init__(self):
        self.health_bundle = joblib.load(os.path.join(MODELS_DIR, "health_model.joblib"))
        self.work_bundle = joblib.load(os.path.join(MODELS_DIR, "work_model.joblib"))
        self.finance_bundle = joblib.load(os.path.join(MODELS_DIR, "finance_model.joblib"))
        self.ensemble_bundle = joblib.load(os.path.join(MODELS_DIR, "ensemble_flourishing_model.joblib"))
        
        with open(os.path.join(MODELS_DIR, "metrics_report.json"), "r", encoding="utf-8") as f:
            self.metrics_report = json.load(f)

    def predict_domains(self, lifestyle_input: Dict[str, Any], workplace_input: Dict[str, Any], financial_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Runs inference across all 3 domain pipelines.
        """
        # 1. Lifestyle Model
        df_life = pd.DataFrame([lifestyle_input])
        vitality_pred = float(self.health_bundle["vitality_pipeline"].predict(df_life)[0])
        vitality_score = float(np.clip(vitality_pred, 5.0, 100.0))
        stress_pred = int(self.health_bundle["stress_pipeline"].predict(df_life)[0])

        # 2. Workplace Model
        df_work = pd.DataFrame([workplace_input])
        fulfillment_pred = float(self.work_bundle["fulfillment_pipeline"].predict(df_work)[0])
        fulfillment_score = float(np.clip(fulfillment_pred, 5.0, 100.0))
        burnout_class = int(self.work_bundle["burnout_pipeline"].predict(df_work)[0])
        burnout_labels = {0: "Low Risk", 1: "Moderate Risk", 2: "High Burnout Risk"}
        burnout_label = burnout_labels.get(burnout_class, "Moderate Risk")

        # 3. Financial Model
        df_fin = pd.DataFrame([financial_input])
        security_pred = float(self.finance_bundle["security_pipeline"].predict(df_fin)[0])
        security_score = float(np.clip(security_pred, 5.0, 100.0))
        anxiety_class = int(self.finance_bundle["anxiety_pipeline"].predict(df_fin)[0])
        anxiety_labels = {0: "Low Anxiety", 1: "Moderate Anxiety", 2: "Severe Anxiety"}
        anxiety_label = anxiety_labels.get(anxiety_class, "Moderate Anxiety")

        # 4. Master Flourishing Meta-Features
        meta_features = pd.DataFrame([{
            "pred_vitality": vitality_score,
            "pred_fulfillment": fulfillment_score,
            "pred_financial_security": security_score,
            "mean_domain_score": (vitality_score + fulfillment_score + security_score) / 3.0,
            "min_domain_score": min(vitality_score, fulfillment_score, security_score),
            "domain_spread": max(vitality_score, fulfillment_score, security_score) - min(vitality_score, fulfillment_score, security_score),
            "health_work_synergy": (vitality_score * fulfillment_score) / 100.0,
            "fin_health_resilience": (security_score * vitality_score) / 100.0
        }])

        flourishing_pred = float(self.ensemble_bundle["master_regressor"].predict(meta_features)[0])
        flourishing_index = float(np.clip(flourishing_pred, 5.0, 100.0))

        cantril_pred = float(self.ensemble_bundle["cantril_regressor"].predict(meta_features)[0])
        cantril_score = float(np.clip(cantril_pred, 1.0, 10.0))

        # Well-being Tier
        if flourishing_index >= 78.0:
            tier = "Thriving (High Flourishing)"
            tier_color = "#10B981"  # Emerald
        elif flourishing_index >= 60.0:
            tier = "Sustainable (Moderate Well-Being)"
            tier_color = "#3B82F6"  # Blue
        elif flourishing_index >= 42.0:
            tier = "Vulnerable (At Risk)"
            tier_color = "#F59E0B"  # Amber
        else:
            tier = "Distressed (Critical Deficit)"
            tier_color = "#EF4444"  # Rose

        # Bottleneck Identification
        domain_scores = {
            "Biological & Lifestyle Health": vitality_score,
            "Occupational & Workplace Fulfillment": fulfillment_score,
            "Financial Resilience & Security": security_score
        }
        bottleneck_domain = min(domain_scores, key=domain_scores.get)
        bottleneck_score = domain_scores[bottleneck_domain]

        # Specific Root Cause Analysis
        root_causes = self._diagnose_root_causes(
            bottleneck_domain, lifestyle_input, workplace_input, financial_input
        )

        return {
            "vitality_score": round(vitality_score, 1),
            "stress_level": stress_pred,
            "fulfillment_score": round(fulfillment_score, 1),
            "burnout_label": burnout_label,
            "security_score": round(security_score, 1),
            "anxiety_label": anxiety_label,
            "flourishing_index": round(flourishing_index, 1),
            "cantril_ladder": round(cantril_score, 1),
            "tier": tier,
            "tier_color": tier_color,
            "domain_scores": domain_scores,
            "bottleneck_domain": bottleneck_domain,
            "bottleneck_score": round(bottleneck_score, 1),
            "root_causes": root_causes
        }

    def _diagnose_root_causes(self, bottleneck: str, life: Dict, work: Dict, fin: Dict) -> List[str]:
        causes = []
        if bottleneck == "Biological & Lifestyle Health":
            if life["sleep_duration"] < 6.5:
                causes.append(f"Chronic Sleep Deficit: Averaging only {life['sleep_duration']} hrs/night (Optimal: 7.5 - 8.5 hrs).")
            if life["daily_steps"] < 5000:
                causes.append(f"Physical Inactivity: Sedentary pattern with {life['daily_steps']:,} steps/day (Target: >8,000).")
            if life["sedentary_hours"] > 9.5:
                causes.append(f"Prolonged Sedentary Behavior: {life['sedentary_hours']} sedentary hours/day elevates cardiovascular strain.")
            if life["sleep_quality"] < 6:
                causes.append(f"Fragmented Sleep Architecture: Self-reported sleep quality of {life['sleep_quality']}/10.")
        elif bottleneck == "Occupational & Workplace Fulfillment":
            if work["weekly_work_hours"] > 48 or work["overtime"] == 1:
                causes.append(f"Excessive Workload & Overtime: Working {work['weekly_work_hours']} hrs/week with active overtime.")
            if work["job_autonomy"] <= 2.5:
                causes.append(f"Low Decision Latitude: Autonomy score of {work['job_autonomy']}/5 indicates micro-management friction.")
            if work["commute_minutes"] > 45:
                causes.append(f"Taxing Commute: {work['commute_minutes']} minutes one-way drains daily cognitive bandwidth.")
            if work["work_life_balance_rating"] <= 2.5:
                causes.append("Severe Work-Life Spillover: Boundary permeability preventing restorative personal downtime.")
        else: # Financial
            if fin["debt_to_income_ratio"] > 0.40:
                causes.append(f"Elevated Debt Burden: Debt-to-Income ratio at {fin['debt_to_income_ratio']:.2f} (Safe ceiling: <0.30).")
            if fin["emergency_fund_months"] < 3.0:
                causes.append(f"Fragile Liquidity Runway: Only {fin['emergency_fund_months']} months of reserve living expenses.")
            if fin["monthly_savings_rate_pct"] < 10.0:
                causes.append(f"Sub-optimal Savings Buffer: Saving {fin['monthly_savings_rate_pct']}% of income (Recommended: >15-20%).")
            if fin["cost_of_living_index"] > 125:
                causes.append(f"High Living Cost Drag: Region COL index of {fin['cost_of_living_index']} eroding discretionary surplus.")

        if not causes:
            causes.append("Domain is functioning at moderate capacity; incremental optimization will yield compound gains.")
        return causes

    def generate_prescriptive_optimizations(self, current_life: Dict, current_work: Dict, current_fin: Dict) -> List[Dict[str, Any]]:
        """
        Solves counterfactual simulations to find the highest-leverage behavioral micro-interventions.
        """
        baseline = self.predict_domains(current_life, current_work, current_fin)
        baseline_index = baseline["flourishing_index"]

        interventions = []

        # Intervention 1: Sleep & Recovery Protocol
        opt_life = dict(current_life)
        opt_life["sleep_duration"] = min(8.0, current_life["sleep_duration"] + 1.25)
        opt_life["sleep_quality"] = min(9.0, current_life["sleep_quality"] + 2.0)
        res1 = self.predict_domains(opt_life, current_work, current_fin)
        delta1 = round(res1["flourishing_index"] - baseline_index, 1)
        interventions.append({
            "title": "Sleep Architecture & Circadian Restoration",
            "category": "Biological Health",
            "action": f"Expand sleep from {current_life['sleep_duration']}h to {opt_life['sleep_duration']:.1f}h/night; implement digital sunset 60 mins before bed.",
            "predicted_flourishing": res1["flourishing_index"],
            "uplift": delta1,
            "evidence": "Walker (2017) & NSF clinical trials show sleep restoration directly modulates amygdala reactivity and subjective life evaluation."
        })

        # Intervention 2: Workload Boundary & Autonomy Re-contracting
        opt_work = dict(current_work)
        opt_work["weekly_work_hours"] = max(38.0, current_work["weekly_work_hours"] - 6.0)
        opt_work["overtime"] = 0
        opt_work["job_autonomy"] = min(5.0, current_work["job_autonomy"] + 1.0)
        res2 = self.predict_domains(current_life, opt_work, current_fin)
        delta2 = round(res2["flourishing_index"] - baseline_index, 1)
        interventions.append({
            "title": "Occupational Boundaries & Work-Life Recovery",
            "category": "Workplace Well-Being",
            "action": f"Cap weekly work at {opt_work['weekly_work_hours']} hrs (eliminate overtime) and negotiate asynchronous communication protocols.",
            "predicted_flourishing": res2["flourishing_index"],
            "uplift": delta2,
            "evidence": "Karasek's Demand-Control model proves that increasing task autonomy while capping extreme hours drops burnout odds by up to 62%."
        })

        # Intervention 3: Financial Emergency Runway & Debt Rationalization
        opt_fin = dict(current_fin)
        opt_fin["emergency_fund_months"] = min(6.0, current_fin["emergency_fund_months"] + 2.5)
        opt_fin["monthly_savings_rate_pct"] = min(30.0, current_fin["monthly_savings_rate_pct"] + 8.0)
        opt_fin["debt_to_income_ratio"] = max(0.15, current_fin["debt_to_income_ratio"] - 0.15)
        res3 = self.predict_domains(current_life, current_work, opt_fin)
        delta3 = round(res3["flourishing_index"] - baseline_index, 1)
        interventions.append({
            "title": "Financial Security Buffer & Debt De-risking",
            "category": "Socio-Economic Well-Being",
            "action": f"Target a {opt_fin['emergency_fund_months']:.1f}-month emergency liquidity cushion and reallocate 8% discretionary margin to high-interest debt paydown.",
            "predicted_flourishing": res3["flourishing_index"],
            "uplift": delta3,
            "evidence": "CFPB empirical research proves financial subjective well-being is more strongly correlated with emergency buffer months than absolute income level."
        })

        # Intervention 4: Holistic Multi-System Synergy (Combining all 3 interventions)
        res_synergy = self.predict_domains(opt_life, opt_work, opt_fin)
        delta_synergy = round(res_synergy["flourishing_index"] - baseline_index, 1)
        interventions.append({
            "title": "Synergistic Multi-Domain Transformation (All 3 Combined)",
            "category": "Holistic Master Intervention",
            "action": "Synchronized execution of sleep discipline, work boundaries, and liquidity buffering.",
            "predicted_flourishing": res_synergy["flourishing_index"],
            "uplift": delta_synergy,
            "evidence": "Cross-domain interaction modeling demonstrates a compounding non-linear multiplier when physiological, occupational, and economic strains are resolved simultaneously."
        })

        # Sort by uplift descending
        interventions.sort(key=lambda x: x["uplift"], reverse=True)
        return interventions


def get_preset_archetypes() -> Dict[str, Dict[str, Any]]:
    """
    Returns pre-configured demographic profiles for one-click demonstration.
    """
    return {
        "Burnt-Out Tech Professional": {
            "description": "High salary, but working 58 hours/week with heavy overtime, poor sleep, and rising burnout.",
            "lifestyle": {
                "sleep_duration": 5.6,
                "sleep_quality": 4.5,
                "daily_steps": 4200,
                "physical_activity_min": 15,
                "resting_heart_rate": 81,
                "sedentary_hours": 11.5,
                "bmi_category": "Overweight"
            },
            "workplace": {
                "weekly_work_hours": 58.0,
                "overtime": 1,
                "remote_work_pct": 25,
                "job_autonomy": 3.2,
                "work_life_balance_rating": 1.8,
                "commute_minutes": 55,
                "career_growth_satisfaction": 3.5,
                "peer_manager_support": 3.0
            },
            "financial": {
                "annual_income": 135000,
                "debt_to_income_ratio": 0.38,
                "monthly_savings_rate_pct": 22.0,
                "emergency_fund_months": 4.5,
                "discretionary_spending_pct": 28.0,
                "financial_literacy_score": 7.0,
                "cost_of_living_index": 140
            }
        },
        "Struggling Early-Career / Student": {
            "description": "Modest income, high educational debt, and financial stress, but good physical activity and sleep.",
            "lifestyle": {
                "sleep_duration": 7.4,
                "sleep_quality": 7.0,
                "daily_steps": 9500,
                "physical_activity_min": 45,
                "resting_heart_rate": 66,
                "sedentary_hours": 6.8,
                "bmi_category": "Normal"
            },
            "workplace": {
                "weekly_work_hours": 36.0,
                "overtime": 0,
                "remote_work_pct": 50,
                "job_autonomy": 3.8,
                "work_life_balance_rating": 3.8,
                "commute_minutes": 20,
                "career_growth_satisfaction": 3.9,
                "peer_manager_support": 4.2
            },
            "financial": {
                "annual_income": 34000,
                "debt_to_income_ratio": 0.85,
                "monthly_savings_rate_pct": 4.0,
                "emergency_fund_months": 0.8,
                "discretionary_spending_pct": 14.0,
                "financial_literacy_score": 5.5,
                "cost_of_living_index": 110
            }
        },
        "Balanced Remote Creator": {
            "description": "Harmonious balance across all 3 domains with 100% remote autonomy, solid savings, and restorative sleep.",
            "lifestyle": {
                "sleep_duration": 7.9,
                "sleep_quality": 8.5,
                "daily_steps": 8800,
                "physical_activity_min": 50,
                "resting_heart_rate": 62,
                "sedentary_hours": 7.0,
                "bmi_category": "Normal"
            },
            "workplace": {
                "weekly_work_hours": 39.0,
                "overtime": 0,
                "remote_work_pct": 100,
                "job_autonomy": 4.8,
                "work_life_balance_rating": 4.6,
                "commute_minutes": 0,
                "career_growth_satisfaction": 4.3,
                "peer_manager_support": 4.4
            },
            "financial": {
                "annual_income": 92000,
                "debt_to_income_ratio": 0.18,
                "monthly_savings_rate_pct": 28.0,
                "emergency_fund_months": 7.5,
                "discretionary_spending_pct": 26.0,
                "financial_literacy_score": 8.2,
                "cost_of_living_index": 98
            }
        },
        "Stressed Middle-Manager in High-COL City": {
            "description": "Extreme cost of living, severe commute, heavy family responsibilities, and zero savings runway.",
            "lifestyle": {
                "sleep_duration": 6.1,
                "sleep_quality": 5.2,
                "daily_steps": 5100,
                "physical_activity_min": 20,
                "resting_heart_rate": 78,
                "sedentary_hours": 10.2,
                "bmi_category": "Overweight"
            },
            "workplace": {
                "weekly_work_hours": 49.0,
                "overtime": 1,
                "remote_work_pct": 0,
                "job_autonomy": 2.8,
                "work_life_balance_rating": 2.2,
                "commute_minutes": 70,
                "career_growth_satisfaction": 2.9,
                "peer_manager_support": 2.7
            },
            "financial": {
                "annual_income": 88000,
                "debt_to_income_ratio": 0.62,
                "monthly_savings_rate_pct": 6.0,
                "emergency_fund_months": 1.2,
                "discretionary_spending_pct": 16.0,
                "financial_literacy_score": 6.0,
                "cost_of_living_index": 165
            }
        }
    }
