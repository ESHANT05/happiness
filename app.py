"""
Streamlit Web Application
Predictive Modeling of Personal Well-being using Lifestyle, Occupational, and Financial Data
An Ensemble Machine Learning Approach for Holistic Human Flourishing Prediction
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json
import os
import sys

# Add project root to system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ensemble_engine import FlourishingPredictor, get_preset_archetypes

# Page Configuration
st.set_page_config(
    page_title="Human Flourishing ML Predictor",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
    }
    
    /* Header Container */
    .hero-banner {
        background: linear-gradient(135deg, #1E1B4B 0%, #312E81 50%, #0F172A 100%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 28px 36px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    }
    
    .hero-title {
        color: #F8FAFC;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 6px;
        letter-spacing: -0.5px;
    }
    
    .hero-subtitle {
        color: #94A3B8;
        font-size: 1.05rem;
        line-height: 1.5;
        margin-bottom: 12px;
    }
    
    .hero-badges {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
    }
    
    .badge {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        color: #CBD5E1;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Metric & Domain Cards */
    .domain-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .domain-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }
    
    .domain-title {
        font-size: 0.95rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
        margin-bottom: 6px;
    }
    
    .domain-score {
        font-size: 2.3rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 8px;
    }
    
    .bottleneck-box {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.12) 0%, rgba(185, 28, 28, 0.05) 100%);
        border: 1px solid rgba(239, 68, 68, 0.35);
        border-radius: 14px;
        padding: 22px;
        margin-top: 15px;
        margin-bottom: 20px;
    }
    
    .intervention-card {
        background: #0F172A;
        border-left: 4px solid #10B981;
        border-radius: 8px 12px 12px 8px;
        padding: 16px 20px;
        margin-bottom: 12px;
        border-top: 1px solid #1E293B;
        border-right: 1px solid #1E293B;
        border-bottom: 1px solid #1E293B;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_engine():
    return FlourishingPredictor()


engine = load_engine()
archetypes = get_preset_archetypes()

# Session State Initialization for Inputs
if "lifestyle" not in st.session_state:
    st.session_state.lifestyle = archetypes["Burnt-Out Tech Professional"]["lifestyle"]
if "workplace" not in st.session_state:
    st.session_state.workplace = archetypes["Burnt-Out Tech Professional"]["workplace"]
if "financial" not in st.session_state:
    st.session_state.financial = archetypes["Burnt-Out Tech Professional"]["financial"]
if "active_preset" not in st.session_state:
    st.session_state.active_preset = "Burnt-Out Tech Professional"


def set_preset(preset_name: str):
    p = archetypes[preset_name]
    st.session_state.lifestyle = p["lifestyle"]
    st.session_state.workplace = p["workplace"]
    st.session_state.financial = p["financial"]
    st.session_state.active_preset = preset_name


# ==========================================
# HERO BANNER
# ==========================================
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">Predictive Modeling of Personal Well-being</div>
    <div class="hero-subtitle">
        An Ensemble Machine Learning Approach for Holistic Human Flourishing Prediction using Lifestyle, Occupational, and Financial Data.
    </div>
    <div class="hero-badges">
        <span class="badge">🧬 Biological & Lifestyle ML</span>
        <span class="badge">💼 Occupational & Burnout ML</span>
        <span class="badge">💰 CFPB Financial Resilience ML</span>
        <span class="badge">🌿 Master Stacking Ensemble</span>
        <span class="badge">🔍 Happiness Bottleneck AI</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Preset Archetype Quick Buttons
st.markdown("##### ⚡ Quick Archetype Presets (Click to test realistic archetypes):")
p_cols = st.columns(4)
for i, name in enumerate(archetypes.keys()):
    with p_cols[i]:
        if st.button(f"{name}", key=f"btn_{name}", use_container_width=True):
            set_preset(name)
            st.rerun()

st.caption(f"Currently inspecting: **{st.session_state.active_preset}** — *{archetypes[st.session_state.active_preset]['description']}*")
st.markdown("---")

# ==========================================
# SIDEBAR: MULTI-DOMAIN INPUT CONTROLS
# ==========================================
st.sidebar.title("🎛️ Multi-Domain Levers")
st.sidebar.caption("Adjust personal indicators to evaluate ML predictions in real-time.")

with st.sidebar.expander("🧬 Domain 1: Biological & Lifestyle", expanded=True):
    sleep_dur = st.slider("Sleep Duration (Hours/Night)", 4.0, 10.0, float(st.session_state.lifestyle["sleep_duration"]), 0.1)
    sleep_qual = st.slider("Sleep Quality (1 - 10)", 1.0, 10.0, float(st.session_state.lifestyle["sleep_quality"]), 0.5)
    steps = st.slider("Daily Steps", 1000, 20000, int(st.session_state.lifestyle["daily_steps"]), 500)
    act_min = st.slider("Active Exercise (Mins/Day)", 5, 120, int(st.session_state.lifestyle["physical_activity_min"]), 5)
    rhr = st.slider("Resting Heart Rate (BPM)", 48, 95, int(st.session_state.lifestyle["resting_heart_rate"]), 1)
    sed_hrs = st.slider("Sedentary Hours/Day", 3.0, 14.0, float(st.session_state.lifestyle["sedentary_hours"]), 0.5)
    bmi = st.selectbox("BMI Category", ["Normal", "Overweight", "Obese"], index=["Normal", "Overweight", "Obese"].index(st.session_state.lifestyle["bmi_category"]))

with st.sidebar.expander("💼 Domain 2: Occupational & Workplace", expanded=False):
    work_hrs = st.slider("Weekly Work Hours", 20.0, 75.0, float(st.session_state.workplace["weekly_work_hours"]), 1.0)
    overtime = st.radio("Overtime Required?", ["No", "Yes"], index=int(st.session_state.workplace["overtime"]))
    remote_pct = st.select_slider("Remote Work Ratio (%)", options=[0, 25, 50, 75, 100], value=int(st.session_state.workplace["remote_work_pct"]))
    autonomy = st.slider("Job Autonomy / Decision Latitude (1-5)", 1.0, 5.0, float(st.session_state.workplace["job_autonomy"]), 0.1)
    wlb = st.slider("Perceived Work-Life Balance (1-5)", 1.0, 5.0, float(st.session_state.workplace["work_life_balance_rating"]), 0.1)
    commute = st.slider("One-Way Commute (Minutes)", 0, 90, int(st.session_state.workplace["commute_minutes"]), 5)
    growth = st.slider("Career Growth Opportunities (1-5)", 1.0, 5.0, float(st.session_state.workplace["career_growth_satisfaction"]), 0.1)
    support = st.slider("Peer & Manager Support (1-5)", 1.0, 5.0, float(st.session_state.workplace["peer_manager_support"]), 0.1)

with st.sidebar.expander("💰 Domain 3: Financial & Socio-Economic", expanded=False):
    income = st.number_input("Annual Income ($ USD)", min_value=15000, max_value=280000, value=int(st.session_state.financial["annual_income"]), step=5000)
    dti = st.slider("Debt-to-Income Ratio (DTI)", 0.0, 1.2, float(st.session_state.financial["debt_to_income_ratio"]), 0.02)
    savings_pct = st.slider("Monthly Savings Rate (%)", 0.0, 50.0, float(st.session_state.financial["monthly_savings_rate_pct"]), 1.0)
    efund = st.slider("Emergency Fund Buffer (Months)", 0.0, 15.0, float(st.session_state.financial["emergency_fund_months"]), 0.5)
    discretionary = st.slider("Discretionary Spending (%)", 5.0, 50.0, float(st.session_state.financial["discretionary_spending_pct"]), 1.0)
    fin_lit = st.slider("Financial Literacy (1 - 10)", 1.0, 10.0, float(st.session_state.financial["financial_literacy_score"]), 0.5)
    col_idx = st.slider("Cost of Living Index (100 = Avg)", 75, 185, int(st.session_state.financial["cost_of_living_index"]), 5)

# Current inputs
current_life = {
    "sleep_duration": sleep_dur,
    "sleep_quality": sleep_qual,
    "daily_steps": steps,
    "physical_activity_min": act_min,
    "resting_heart_rate": rhr,
    "sedentary_hours": sed_hrs,
    "bmi_category": bmi
}

current_work = {
    "weekly_work_hours": work_hrs,
    "overtime": 1 if overtime == "Yes" else 0,
    "remote_work_pct": remote_pct,
    "job_autonomy": autonomy,
    "work_life_balance_rating": wlb,
    "commute_minutes": commute,
    "career_growth_satisfaction": growth,
    "peer_manager_support": support
}

current_fin = {
    "annual_income": income,
    "debt_to_income_ratio": dti,
    "monthly_savings_rate_pct": savings_pct,
    "emergency_fund_months": efund,
    "discretionary_spending_pct": discretionary,
    "financial_literacy_score": fin_lit,
    "cost_of_living_index": col_idx
}

# Run Inference
results = engine.predict_domains(current_life, current_work, current_fin)
optimizations = engine.generate_prescriptive_optimizations(current_life, current_work, current_fin)

# ==========================================
# MAIN TABS
# ==========================================
tab_summary, tab_prescriptions, tab_whatif, tab_validation = st.tabs([
    "📊 Executive Flourishing Summary",
    "💡 AI Prescriptions & Action Plan",
    "🔬 Counterfactual 'What-If' Simulator",
    "📑 Model Benchmarking & Research Metrics"
])

# -------------------------------------------------------------
# TAB 1: EXECUTIVE FLOURISHING SUMMARY
# -------------------------------------------------------------
with tab_summary:
    col_gauge, col_radar = st.columns([1.1, 1.0])

    with col_gauge:
        st.markdown("#### 🌟 Master Holistic Flourishing Index")
        
        # Plotly Gauge Chart
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=results["flourishing_index"],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': f"<b>{results['tier']}</b><br><span style='font-size:0.85em;color:#94A3B8'>Cantril Ladder: {results['cantril_ladder']} / 10.0</span>", 'font': {'size': 18, 'color': "#FFFFFF"}},
            number={'suffix': " / 100", 'font': {'size': 44, 'color': "#FFFFFF", 'family': "Outfit"}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#475569"},
                'bar': {'color': results["tier_color"], 'thickness': 0.28},
                'bgcolor': "rgba(15, 23, 42, 0.6)",
                'borderwidth': 1,
                'bordercolor': "#334155",
                'steps': [
                    {'range': [0, 42], 'color': "rgba(239, 68, 68, 0.2)"},
                    {'range': [42, 60], 'color': "rgba(245, 158, 11, 0.2)"},
                    {'range': [60, 78], 'color': "rgba(59, 130, 246, 0.2)"},
                    {'range': [78, 100], 'color': "rgba(16, 185, 129, 0.25)"}
                ],
                'threshold': {
                    'line': {'color': "#FFFFFF", 'width': 3},
                    'thickness': 0.8,
                    'value': 75.0
                }
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=50, b=20),
            height=300
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col_radar:
        st.markdown("#### 🎯 Tri-Domain Well-Being Equilibrium")
        categories = ['Biological Vitality', 'Occupational Fulfillment', 'Financial Security']
        user_values = [results["vitality_score"], results["fulfillment_score"], results["security_score"]]
        optimal_values = [85, 85, 85]

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=user_values + [user_values[0]],
            theta=categories + [categories[0]],
            fill='toself',
            fillcolor='rgba(99, 102, 241, 0.25)',
            line=dict(color='#818CF8', width=2.5),
            name='Current Profile'
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=optimal_values + [optimal_values[0]],
            theta=categories + [categories[0]],
            line=dict(color='rgba(16, 185, 129, 0.7)', width=1.5, dash='dash'),
            name='Thriving Benchmark (85+)'
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], color="#94A3B8", gridcolor="#334155"),
                angularaxis=dict(color="#E2E8F0", gridcolor="#334155")
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5, font=dict(color="#CBD5E1")),
            margin=dict(l=30, r=30, t=20, b=30),
            height=300
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    # 3 DOMAIN SCORE CARDS
    st.markdown("##### 🔍 Multi-Domain Diagnostic Breakdown")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="domain-card" style="border-top: 4px solid #06B6D4;">
            <div class="domain-title">🧬 Biological & Lifestyle</div>
            <div class="domain-score">{results['vitality_score']} <span style="font-size:1rem;color:#94A3B8">/ 100</span></div>
            <p style="color:#CBD5E1;font-size:0.9rem;margin-bottom:6px;">
                Sleep: <b>{sleep_dur} hrs</b> (Q: {sleep_qual}/10)<br>
                Activity: <b>{steps:,} steps</b> | Sedentary: <b>{sed_hrs}h</b>
            </p>
            <span class="badge" style="background:#0E7490;color:#E0F2FE;">Stress Level: {results['stress_level']} / 10</span>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="domain-card" style="border-top: 4px solid #8B5CF6;">
            <div class="domain-title">💼 Occupational Fulfillment</div>
            <div class="domain-score">{results['fulfillment_score']} <span style="font-size:1rem;color:#94A3B8">/ 100</span></div>
            <p style="color:#CBD5E1;font-size:0.9rem;margin-bottom:6px;">
                Workload: <b>{work_hrs} hrs/wk</b> ({'Overtime' if overtime=='Yes' else 'No OT'})<br>
                Autonomy: <b>{autonomy}/5</b> | Remote: <b>{remote_pct}%</b>
            </p>
            <span class="badge" style="background:#6D28D9;color:#EDE9FE;">Burnout: {results['burnout_label']}</span>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="domain-card" style="border-top: 4px solid #10B981;">
            <div class="domain-title">💰 Financial Resilience</div>
            <div class="domain-score">{results['security_score']} <span style="font-size:1rem;color:#94A3B8">/ 100</span></div>
            <p style="color:#CBD5E1;font-size:0.9rem;margin-bottom:6px;">
                DTI Ratio: <b>{dti:.2f}</b> | Buffer: <b>{efund} mos</b><br>
                Savings Rate: <b>{savings_pct}%</b> | Income: <b>${income:,}</b>
            </p>
            <span class="badge" style="background:#047857;color:#D1FAE5;">Anxiety: {results['anxiety_label']}</span>
        </div>
        """, unsafe_allow_html=True)

    # BOTTLENECK DIAGNOSIS BOX
    st.markdown(f"""
    <div class="bottleneck-box">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
            <span style="font-size:1.6rem;">⚠️</span>
            <span style="font-size:1.25rem;font-weight:700;color:#FCA5A5;">
                Identified Happiness Bottleneck: {results['bottleneck_domain']} ({results['bottleneck_score']}/100)
            </span>
        </div>
        <p style="color:#FEE2E2;margin-bottom:12px;font-size:0.95rem;">
            Empirical multi-domain modeling identifies this area as the critical binding constraint. Because human well-being follows non-linear multi-attribute dynamics, deficits in this domain create cross-system drag, suppressing gains made elsewhere.
        </p>
        <div style="background:rgba(0,0,0,0.25);border-radius:8px;padding:12px 18px;">
            <b style="color:#FFFFFF;font-size:0.9rem;">Diagnostic Root Causes:</b>
            <ul style="color:#FECACA;margin-top:6px;margin-bottom:0;padding-left:20px;font-size:0.9rem;">
                {''.join([f'<li>{cause}</li>' for cause in results['root_causes']])}
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)


# -------------------------------------------------------------
# TAB 2: AI PRESCRIPTIONS & ACTION PLAN
# -------------------------------------------------------------
with tab_prescriptions:
    st.markdown("### 💡 Evidence-Based Prescriptive Interventions")
    st.write(
        "Using sensitivity gradients from our ensemble ML models and principles from **Positive Psychology (Seligman's PERMA)** and **Behavioral Economics**, "
        "the AI calculates the highest-leverage micro-adjustments tailored to your bottleneck."
    )

    for item in optimizations:
        st.markdown(f"""
        <div class="intervention-card">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                <span style="font-weight:700;font-size:1.15rem;color:#F8FAFC;">{item['title']}</span>
                <span class="badge" style="background:rgba(16,185,129,0.2);color:#34D399;font-size:0.9rem;border-color:#10B981;">
                    +{item['uplift']} Flourishing Points (Target: {item['predicted_flourishing']}/100)
                </span>
            </div>
            <div style="color:#94A3B8;font-size:0.85rem;margin-bottom:8px;">Domain: <b>{item['category']}</b></div>
            <p style="color:#E2E8F0;font-size:0.95rem;margin-bottom:8px;">
                🎯 <b>Recommended Action:</b> {item['action']}
            </p>
            <p style="color:#64748B;font-size:0.8rem;margin-bottom:0;font-style:italic;">
                📚 Scientific Evidence: {item['evidence']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Downloadable Clinical / Academic Report
    st.markdown("---")
    report_text = f"""# Personal Well-Being & Flourishing Assessment Report
Generated by: Predictive Modeling of Personal Well-being using Lifestyle, Occupational, and Financial Data
Framework: Ensemble Multi-Domain Machine Learning Architecture

## Executive Metrics
- Master Holistic Human Flourishing Index: {results['flourishing_index']} / 100
- Well-Being Classification: {results['tier']}
- Cantril Self-Anchoring Ladder: {results['cantril_ladder']} / 10.0
- Primary Binding Constraint (Bottleneck): {results['bottleneck_domain']} ({results['bottleneck_score']}/100)

## Domain Diagnoses
1. Biological & Lifestyle Vitality: {results['vitality_score']}/100 | Stress Level: {results['stress_level']}/10
   - Sleep: {sleep_dur} hrs/night (Quality: {sleep_qual}/10)
   - Daily Steps: {steps:,} | Sedentary: {sed_hrs} hrs/day
2. Occupational & Workplace Fulfillment: {results['fulfillment_score']}/100 | Burnout Risk: {results['burnout_label']}
   - Weekly Hours: {work_hrs} hrs | Overtime: {'Yes' if overtime=='Yes' else 'No'}
   - Autonomy: {autonomy}/5.0 | Remote: {remote_pct}%
3. Financial Security & Resilience: {results['security_score']}/100 | Anxiety: {results['anxiety_label']}
   - Debt-to-Income: {dti:.2f} | Emergency Fund: {efund} months
   - Savings Rate: {savings_pct}% | Income: ${income:,}

## Top Prescriptive Interventions
{chr(10).join([f"- {opt['title']} (+{opt['uplift']} pts): {opt['action']}" for opt in optimizations])}
"""
    st.download_button(
        label="📥 Download Comprehensive Well-Being Report (.MD)",
        data=report_text,
        file_name="Personal_WellBeing_Flourishing_Report.md",
        mime="text/markdown"
    )


# -------------------------------------------------------------
# TAB 3: COUNTERFACTUAL "WHAT-IF" SIMULATOR
# -------------------------------------------------------------
with tab_whatif:
    st.markdown("### 🔬 Interactive Counterfactual Simulation")
    st.write(
        "Test hypothetical lifestyle and workplace interventions to see the exact non-linear trajectory change predicted by the stacking ensemble."
    )

    wcol1, wcol2 = st.columns([1, 1])

    with wcol1:
        st.markdown("##### 🔀 Adjust Simulation Levers")
        sim_sleep_delta = st.slider("Modify Sleep Duration (Hours)", -2.0, 3.0, 1.0, 0.25)
        sim_ot_toggle = st.selectbox("Simulate Overtime Policy", ["Keep Current", "Force Zero Overtime", "Add Overtime"])
        sim_work_hrs_delta = st.slider("Modify Weekly Workload (Hours)", -15.0, 15.0, -5.0, 1.0)
        sim_savings_delta = st.slider("Modify Monthly Savings Rate (%)", -10.0, 20.0, 5.0, 1.0)
        sim_efund_delta = st.slider("Modify Emergency Buffer (Months)", -2.0, 6.0, 2.0, 0.5)

    # Calculate Counterfactual State
    sim_life = dict(current_life)
    sim_life["sleep_duration"] = np.clip(current_life["sleep_duration"] + sim_sleep_delta, 4.0, 10.0)
    sim_life["sleep_quality"] = np.clip(current_life["sleep_quality"] + (sim_sleep_delta * 0.8), 1.0, 10.0)

    sim_work = dict(current_work)
    sim_work["weekly_work_hours"] = np.clip(current_work["weekly_work_hours"] + sim_work_hrs_delta, 20.0, 75.0)
    if sim_ot_toggle == "Force Zero Overtime":
        sim_work["overtime"] = 0
    elif sim_ot_toggle == "Add Overtime":
        sim_work["overtime"] = 1

    sim_fin = dict(current_fin)
    sim_fin["monthly_savings_rate_pct"] = np.clip(current_fin["monthly_savings_rate_pct"] + sim_savings_delta, 0.0, 50.0)
    sim_fin["emergency_fund_months"] = np.clip(current_fin["emergency_fund_months"] + sim_efund_delta, 0.0, 18.0)

    sim_res = engine.predict_domains(sim_life, sim_work, sim_fin)
    flourish_delta = round(sim_res["flourishing_index"] - results["flourishing_index"], 1)

    with wcol2:
        st.markdown("##### 📈 Projected Impact")
        
        # Delta Metric Card
        delta_color = "#10B981" if flourish_delta >= 0 else "#EF4444"
        delta_sign = "+" if flourish_delta >= 0 else ""
        
        st.markdown(f"""
        <div style="background:#1E293B;border:1px solid #334155;border-radius:14px;padding:24px;text-align:center;">
            <div style="color:#94A3B8;font-size:0.9rem;text-transform:uppercase;letter-spacing:1px;font-weight:600;">
                Simulated Flourishing Index
            </div>
            <div style="font-size:3.2rem;font-weight:700;color:#F8FAFC;margin:8px 0;">
                {sim_res['flourishing_index']} <span style="font-size:1.2rem;color:#94A3B8">/ 100</span>
            </div>
            <div style="font-size:1.3rem;font-weight:600;color:{delta_color};">
                {delta_sign}{flourish_delta} Points from Baseline ({results['flourishing_index']})
            </div>
            <div style="margin-top:10px;font-size:0.9rem;color:#CBD5E1;">
                Cantril Ladder: {results['cantril_ladder']} ➔ <b>{sim_res['cantril_ladder']} / 10</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Comparative Bar Chart
        compare_df = pd.DataFrame({
            "Domain": ["Biological Vitality", "Work Fulfillment", "Financial Security", "Overall Flourishing"],
            "Baseline": [results["vitality_score"], results["fulfillment_score"], results["security_score"], results["flourishing_index"]],
            "Simulated": [sim_res["vitality_score"], sim_res["fulfillment_score"], sim_res["security_score"], sim_res["flourishing_index"]]
        })

        fig_compare = go.Figure()
        fig_compare.add_trace(go.Bar(
            x=compare_df["Domain"], y=compare_df["Baseline"],
            name="Baseline", marker_color="#64748B"
        ))
        fig_compare.add_trace(go.Bar(
            x=compare_df["Domain"], y=compare_df["Simulated"],
            name="Simulated", marker_color="#10B981"
        ))
        fig_compare.update_layout(
            barmode="group",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#CBD5E1"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            yaxis=dict(range=[0, 100], gridcolor="#334155"),
            xaxis=dict(gridcolor="rgba(0,0,0,0)"),
            margin=dict(l=20, r=20, t=30, b=20),
            height=260
        )
        st.plotly_chart(fig_compare, use_container_width=True)


# -------------------------------------------------------------
# TAB 4: MODEL BENCHMARKING & RESEARCH METRICS
# -------------------------------------------------------------
with tab_validation:
    st.markdown("### 📑 Machine Learning Architecture & Validation Metrics")
    st.write(
        "Detailed performance evaluation across all 4 machine learning pipelines, cross-validation metrics, and feature importance rankings."
    )

    metrics = engine.metrics_report

    # Metrics Summary Table
    m_cols = st.columns(4)
    models_info = [
        ("health_model", "🧬 Lifestyle Vitality", m_cols[0]),
        ("work_model", "💼 Work Fulfillment", m_cols[1]),
        ("finance_model", "💰 Financial Security", m_cols[2]),
        ("master_ensemble", "🌿 Master Ensemble", m_cols[3])
    ]

    for key, label, col in models_info:
        m = metrics[key]
        with col:
            st.markdown(f"""
            <div style="background:#1E293B;border:1px solid #334155;border-radius:12px;padding:16px;">
                <div style="font-size:0.9rem;font-weight:600;color:#CBD5E1;margin-bottom:4px;">{label}</div>
                <div style="font-size:0.75rem;color:#94A3B8;margin-bottom:8px;">{m['algorithm']}</div>
                <div style="font-size:1.4rem;font-weight:700;color:#38BDF8;">R²: {m['metrics']['r2']:.3f}</div>
                <div style="font-size:0.85rem;color:#E2E8F0;">RMSE: {m['metrics']['rmse']:.2f} | MAE: {m['metrics']['mae']:.2f}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### 📊 Feature Importance Analyses Across Domains")

    fcol1, fcol2 = st.columns(2)

    with fcol1:
        # Lifestyle Top Features
        life_fi = pd.DataFrame(list(metrics["health_model"]["top_features"].items()), columns=["Feature", "Importance"]).sort_values("Importance", ascending=True)
        fig_lfi = px.bar(life_fi, x="Importance", y="Feature", orientation="h", title="Biological Model Feature Importances", color="Importance", color_continuous_scale="Purples")
        fig_lfi.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#CBD5E1"), coloraxis_showscale=False, height=280, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_lfi, use_container_width=True)

        # Financial Top Features
        fin_fi = pd.DataFrame(list(metrics["finance_model"]["top_features"].items()), columns=["Feature", "Importance"]).sort_values("Importance", ascending=True)
        fig_ffi = px.bar(fin_fi, x="Importance", y="Feature", orientation="h", title="Financial Model Feature Importances", color="Importance", color_continuous_scale="Teal")
        fig_ffi.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#CBD5E1"), coloraxis_showscale=False, height=280, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_ffi, use_container_width=True)

    with fcol2:
        # Workplace Top Features
        work_fi = pd.DataFrame(list(metrics["work_model"]["top_features"].items()), columns=["Feature", "Importance"]).sort_values("Importance", ascending=True)
        fig_wfi = px.bar(work_fi, x="Importance", y="Feature", orientation="h", title="Workplace Model Feature Importances", color="Importance", color_continuous_scale="Blues")
        fig_wfi.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#CBD5E1"), coloraxis_showscale=False, height=280, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_wfi, use_container_width=True)

        # Master Ensemble Top Meta-Features
        ens_fi = pd.DataFrame(list(metrics["master_ensemble"]["top_features"].items()), columns=["Feature", "Importance"]).sort_values("Importance", ascending=True)
        fig_efi = px.bar(ens_fi, x="Importance", y="Feature", orientation="h", title="Master Stacking Ensemble Meta-Features", color="Importance", color_continuous_scale="Viridis")
        fig_efi.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#CBD5E1"), coloraxis_showscale=False, height=280, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_efi, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #64748B; font-size: 0.85rem; padding: 10px;'>"
    "<b>Project:</b> Predictive Modeling of Personal Well-being using Lifestyle, Occupational, and Financial Data | "
    "<b>Architecture:</b> Multi-Domain Ensemble Machine Learning | "
    "Built for the Science of Happiness Independent Research Study"
    "</div>",
    unsafe_allow_html=True
)
