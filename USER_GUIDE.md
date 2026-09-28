# Comprehensive Website User & Functionality Guide

**Project:** Predictive Modeling of Personal Well-being using Lifestyle, Occupational, and Financial Data  
**Application URL:** `http://localhost:8501`  
**Launcher:** `run_dashboard.bat` or `streamlit run app.py`  

---

## 🧭 System Overview & Layout

The dashboard is structured into three main visual zones:
1. **Top Zone:** Header banner & One-Click Archetype Presets.
2. **Left Sidebar:** 22 Real-time multi-domain input controls (Biological, Occupational, Financial).
3. **Center Main Stage:** Four specialized interactive tabs containing real-time ML inferences, diagnostic charts, prescriptive simulations, and model research metrics.

---

## ⚡ 1. Top Section: Archetype Presets

Directly beneath the header banner are four **Quick Archetype Preset Buttons**:
- **Burnt-Out Tech Professional:** High income ($135,000), 58 hours/week with heavy overtime, short sleep (5.6h), low exercise, and high burnout risk.
- **Struggling Early-Career / Student:** Modest income ($34,000), high educational debt (DTI 0.85), low savings buffer (0.8 months), but healthy physical activity and restorative sleep.
- **Balanced Remote Creator:** 100% remote flexibility, balanced 39-hour workweek, strong liquidity runway (7.5 months), high decision autonomy, and high flourishing.
- **Stressed Middle-Manager in High-COL City:** Long commute (70 mins), high cost of living (165), high family financial drag, and low work-life boundary.

### What it does:
Clicking any preset button instantly overwrites all 22 sliders across all three domains with verified, realistic profiles. This allows an evaluator or presenter to demonstrate the system immediately without manual slider adjustments.

---

## 🎛️ 2. Left Sidebar: Multi-Domain Personal Levers

The sidebar contains 22 input features organized into three expandable categories:

### 🧬 Domain 1: Biological & Lifestyle Levers
- **Sleep Duration (Hours/Night):** Models circadian duration (4.0 to 10.0 hrs). Sweet spot calibrated around 7.5 - 8.5 hours.
- **Sleep Quality (1 - 10):** Self-reported sleep depth and restorative feeling.
- **Daily Steps:** Quantifies ambulatory physical activity (1,000 to 20,000 steps).
- **Active Exercise (Mins/Day):** Intentional moderate-to-vigorous physical exercise (5 to 120 mins).
- **Resting Heart Rate (BPM):** Cardiovascular baseline (48 to 95 BPM). Lower resting rates correlate with cardiovascular fitness.
- **Sedentary Hours/Day:** Prolonged physical inactivity (sitting at a desk, commuting, screen time).
- **BMI Category:** Normal, Overweight, or Obese (incorporates metabolic strain factors).

### 💼 Domain 2: Occupational & Workplace Levers
- **Weekly Work Hours:** Total weekly hours logged (20 to 75 hrs).
- **Overtime Required?:** Binary switch (Yes / No). Imposes psychological strain penalty based on Karasek's Demand model.
- **Remote Work Ratio (%):** Percentage of remote work (0%, 25%, 50%, 75%, 100%). Modulates commute friction and autonomy.
- **Job Autonomy / Decision Latitude (1 - 5):** Degree of control over schedule, tasks, and pacing.
- **Perceived Work-Life Balance (1 - 5):** Qualitative measure of personal-work boundary separation.
- **One-Way Commute (Minutes):** Travel duration (0 to 90 mins).
- **Career Growth Opportunities (1 - 5):** Forward-looking psychological trajectory within the organization.
- **Peer & Manager Support (1 - 5):** Social cohesion and psychological safety in the workplace.

### 💰 Domain 3: Financial & Socio-Economic Levers
- **Annual Income ($ USD):** Gross annual earnings ($15,000 to $280,000). Modeled with logarithmic diminishing marginal returns.
- **Debt-to-Income Ratio (DTI):** Monthly debt obligations divided by gross income (0.0 to 1.2). Values above 0.36 trigger financial anxiety flags.
- **Monthly Savings Rate (%):** Percentage of net take-home pay saved/invested (0% to 50%).
- **Emergency Fund Buffer (Months):** Liquid cash reserves covering living expenses (0 to 15 months).
- **Discretionary Spending (%):** Budget flexibility allocated to leisure, hobbies, and dining.
- **Financial Literacy Score (1 - 10):** Knowledge of compound interest, debt management, and budgeting.
- **Cost of Living Index:** Regional cost drag (100 = National Average; up to 185 for high-cost metros).

---

## 📊 3. Tab 1: Executive Flourishing Summary

This tab serves as the primary evaluation dashboard:

### A. Master Holistic Flourishing Index (Plotly Gauge)
- **Score (0 to 100):** The primary output of the Gradient Boosting Stacking Ensemble.
- **Classification Tier:**
  - 🟢 **Thriving** (Score $\ge 78$): High systemic flourishing, balanced domains.
  - 🔵 **Sustainable** ($60 \le \text{Score} < 78$): Healthy baseline, minor optimization room.
  - 🟡 **Vulnerable** ($42 \le \text{Score} < 60$): Moderate strain, one or more domains struggling.
  - 🔴 **Distressed** (Score $< 42$): Severe chronic deficits, high risk of burnout or health collapse.
- **Cantril Self-Anchoring Ladder:** Life satisfaction metric ($1.0$ to $10.0$) standard in global happiness studies (e.g. UN World Happiness Report).

### B. Tri-Domain Well-Being Equilibrium (Polar Radar Chart)
- Maps the individual's three scores (**Biological Vitality**, **Occupational Fulfillment**, and **Financial Security**) on a 3-axis radar chart.
- Overlays the **Thriving Benchmark (85+)** in dashed green, visually highlighting which life dimension is lagging behind.

### C. Three Multi-Domain Diagnostic Breakdown Cards
- **Biological Vitality Card:** Displays score out of 100, summary of sleep and steps, and a **Stress Level badge (1 to 10)**.
- **Occupational Fulfillment Card:** Displays score out of 100, workload summary, and a **Burnout Risk badge** (*Low Risk*, *Moderate Risk*, *High Burnout Risk*).
- **Financial Resilience Card:** Displays score out of 100, savings and debt summary, and a **Financial Anxiety badge** (*Low*, *Moderate*, *Severe Anxiety*).

### D. Identified Happiness Bottleneck Diagnosis Box
- Mathematically pinpoints the single weakest domain acting as the "binding constraint" on overall happiness.
- Evaluates **Liebig's Law of the Minimum**: an individual's happiness is limited not by their strongest domain, but by their weakest.
- Lists specific, bullet-pointed **Diagnostic Root Causes** extracted from the user's data (e.g., chronic sleep deficit, DTI above safe threshold, zero overtime boundaries).

---

## 💡 4. Tab 2: AI Prescriptions & Action Plan

Provides actionable, prescriptive intelligence based on sensitivity gradients:

### A. Prioritized Micro-Intervention Cards
The engine calculates four counterfactual behavioral interventions and sorts them by estimated point uplift:
1. **Sleep Architecture & Circadian Restoration:** Quantifies exact hours to add, sleep quality protocol, and references Matthew Walker / NSF clinical sleep neuroscience.
2. **Occupational Boundaries & Work-Life Recovery:** Calculates work hour caps, overtime elimination, autonomy re-negotiation, and references Karasek's Job Demand-Control model.
3. **Financial Security Buffer & Debt De-risking:** Reallocates discretionary income into emergency liquid reserves, targets safe DTI ratios, and references Consumer Financial Protection Bureau (CFPB) empirical findings.
4. **Synergistic Multi-Domain Transformation:** Combines all three interventions simultaneously, demonstrating non-linear compound multipliers.

### B. 📥 Download Comprehensive Well-Being Report Button
Generates a downloadable, clinical-grade assessment report in Markdown (`Personal_WellBeing_Flourishing_Report.md`) containing executive scores, domain metrics, diagnosed root causes, and recommended actions.

---

## 🔬 5. Tab 3: Counterfactual "What-If" Simulator

Allows users or researchers to simulate hypothetical interventions and observe the projected ML trajectory:

### Controls:
- **Modify Sleep Duration (Hours):** Test adding or subtracting up to 3 hours of sleep per night.
- **Simulate Overtime Policy:** Toggle between keeping current schedule, forcing zero overtime, or adding overtime.
- **Modify Weekly Workload (Hours):** Test reducing or increasing work hours by $\pm 15$ hrs.
- **Modify Monthly Savings Rate (%):** Test saving up to 20% more take-home pay.
- **Modify Emergency Buffer (Months):** Test saving an additional 2 to 6 months of emergency reserves.

### Outputs:
- **Projected Impact Metric Card:** Displays the simulated flourishing score, the point difference from baseline (e.g., $+14.9$ points), and the updated Cantril Ladder.
- **Comparative Grouped Bar Chart:** Side-by-side visualization comparing Baseline vs. Simulated scores across Biological Vitality, Workplace Fulfillment, Financial Security, and Overall Flourishing.

---

## 📑 6. Tab 4: Model Benchmarking & Research Metrics

Presents the scientific validation of the machine learning architecture:

### A. Model Performance Cards
Displays the exact evaluation statistics from 80/20 train/test splits:
- **Biological & Lifestyle Model:** Random Forest Regressor ($R^2 = 0.880$, $\text{RMSE} = 4.19$, $\text{MAE} = 3.37$).
- **Workplace & Occupational Model:** Gradient Boosting Regressor ($R^2 = 0.924$, $\text{RMSE} = 3.20$, $\text{MAE} = 2.59$).
- **Financial & Socio-Economic Model:** Random Forest Regressor ($R^2 = 0.943$, $\text{RMSE} = 4.06$, $\text{MAE} = 3.26$).
- **Master Stacking Ensemble:** Gradient Boosting Meta-Learner ($R^2 = 0.810$, $\text{RMSE} = 4.34$, $\text{MAE} = 3.42$).

### B. Feature Importance Analyses (4 Interactive Horizontal Bar Charts)
- **Biological Model:** Highlights `daily_steps` (43.4%), `sleep_duration` (28.5%), and `bmi_category` (12.4%).
- **Workplace Model:** Highlights `work_life_balance_rating` (45.2%), `job_autonomy` (15.9%), and `career_growth` (12.3%).
- **Financial Model:** Highlights `emergency_fund_months` (79.3%), `annual_income` (7.6%), and `debt_to_income_ratio` (4.9%).
- **Master Ensemble Meta-Features:** Highlights `mean_domain_score` (73.4%) and `min_domain_score` (16.0%), confirming that the lowest domain exerts heavy downward drag on holistic flourishing.
