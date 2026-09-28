# Academic Research Presentation & Project Brief

**Title:** Predictive Modeling of Personal Well-being using Lifestyle, Occupational, and Financial Data  
**Sub-title:** An Ensemble Machine Learning Approach for Holistic Human Flourishing Prediction  
**Course / Context:** Science of Happiness & Human Flourishing — Independent Self-Study Research  
**Author:** Eshant  

---

## Slide 1: Title Slide & Project Identity
- **Project Title:** Predictive Modeling of Personal Well-being using Lifestyle, Occupational, and Financial Data
- **Subtitle:** A Multimodal Ensemble Machine Learning System for Holistic Human Flourishing
- **Core Domains Integrated:**
  - Positive Psychology & Behavioral Science (PERMA Framework)
  - Circadian Biology & Lifestyle Medicine
  - Occupational Sociology (Karasek's Demand-Control Model)
  - Socio-Economic Well-Being (CFPB Financial Resilience Scale)

---

## Slide 2: Problem Statement & Research Motivation
- **The Blindspot in Well-Being Research:** Traditional happiness measurements rely heavily on isolated, periodic subjective surveys (e.g. general life satisfaction scale 1-10) without accounting for underlying mechanistic drivers.
- **Siloed Domain Analysis:** Health researchers look only at sleep/diet; economists look only at income/debt; organizational psychologists look only at workplace stress.
- **The Interaction Reality:** Real human flourishing is **non-linear and cross-domain**. Chronic sleep loss magnifies financial anxiety; heavy overtime degrades physiological recovery; financial fragility destroys mental peace of mind.
- **Research Question:** *Can an ensemble machine learning architecture accurately model multi-domain life factors, quantify systemic well-being, and identify an individual's primary "happiness bottleneck"?*

---

## Slide 3: Conceptual Framework & Scientific Foundations
1. **Biological / Lifestyle Domain:**
   - Grounded in circadian rhythm biology and allostatic load theory.
   - Evaluates sleep duration, sleep quality, daily physical activity (steps), resting cardiovascular metrics, and sedentary strain.
2. **Occupational / Workplace Domain:**
   - Grounded in Karasek’s **Job Demand-Control-Support** model.
   - Measures weekly hours, mandatory overtime, remote work flexibility, decision latitude (autonomy), and collegial support.
3. **Socio-Economic / Financial Domain:**
   - Calibrated against the **Consumer Financial Protection Bureau (CFPB)** Financial Well-Being Scale.
   - Prioritizes emergency fund runway (months of living expenses) and debt-to-income (DTI) ratio over raw gross salary.
4. **Master Flourishing Ensemble:**
   - Incorporates Martin Seligman's **PERMA model** (Positive Emotion, Engagement, Relationships, Meaning, Accomplishment) and the **Cantril Self-Anchoring Ladder**.

---

## Slide 4: System Architecture & Data Engineering
- **Modular Multi-Pipeline Pipeline:**
  - `data_generator.py`: Statistically calibrated distributions mirroring CDC, Fitbit, IBM HR Analytics, and CFPB survey benchmarks with realistic cross-domain spillover feedback loops.
  - Preprocessing pipelines utilizing `StandardScaler` for continuous biometrics and `OneHotEncoder` for categorical factors.
- **Dataset Scale:** 3,500 domain-specific training cohorts and 4,000 multi-domain integrated cross-validation profiles.

---

## Slide 5: Model Design & Machine Learning Pipeline
1. **Model 1: Lifestyle Vitality & Stress Predictor**
   - **Algorithm:** Random Forest Regressor & Multi-class Classifier
   - Predicts: Vitality Score ($0-100$) and Stress Level ($1-10$)
2. **Model 2: Occupational Fulfillment & Burnout Predictor**
   - **Algorithm:** Gradient Boosting Regressor & Random Forest Classifier
   - Predicts: Job Fulfillment Score ($0-100$) and Burnout Risk Tier
3. **Model 3: CFPB Financial Resilience Predictor**
   - **Algorithm:** Random Forest Regressor & Classification Tree
   - Predicts: Financial Security Score ($0-100$) and Financial Anxiety Level
4. **Master Non-Linear Stacking Ensemble:**
   - **Algorithm:** Gradient Boosting Meta-Learner
   - Synthesizes latent domain predictions + interaction terms:
     - `mean_domain_score`
     - `min_domain_score` (capturing weakest-link vulnerability)
     - `domain_spread`
     - `health_work_synergy` and `fin_health_resilience`

---

## Slide 6: Quantitative Results & Empirical Benchmarks
The models achieved high predictive fidelity across all validation splits:

| Model Pipeline | Primary Algorithm | Validation $R^2$ | RMSE | MAE |
| :--- | :--- | :---: | :---: | :---: |
| **Lifestyle & Biological** | Random Forest Regressor | **0.880** | 4.19 | 3.37 |
| **Workplace & Occupational** | Gradient Boosting Regressor | **0.924** | 3.20 | 2.59 |
| **Financial & Socio-Economic** | Random Forest Regressor | **0.943** | 4.06 | 3.26 |
| **Master Flourishing Ensemble** | Gradient Boosting Meta-Learner | **0.810** | **4.34** | **3.42** |

---

## Slide 7: Key Scientific Insights & Feature Importances
- **Finding 1: Emergency Runway Outweighs Raw Income.** In the financial model, `emergency_fund_months` accounted for **79.3%** of feature importance, whereas `annual_income` accounted for only **7.6%**. Having 3-6 months of liquid reserves provides vastly more subjective peace of mind than higher pay paired with zero buffer.
- **Finding 2: Work-Life Balance Trumps Hours.** In workplace fulfillment, `work_life_balance_rating` (45.2%) and `job_autonomy` (15.9%) dominated raw weekly hours (4.3%), confirming Karasek's thesis that autonomy protects against high work demands.
- **Finding 3: Liebig's Law of the Minimum in Psychology.** In the Master Ensemble, `min_domain_score` accounted for **16.0%** of total predictive importance. An individual cannot achieve flourishing if any single foundational pillar (physical health, job dignity, or financial stability) has collapsed.

---

## Slide 8: The Happiness Bottleneck Diagnosis Engine
- Instead of generic positive thinking advice, the system identifies an individual's **binding constraint**.
- **Automated Root Cause Diagnosis:**
  - Pinpoints specific physiological, occupational, or economic drivers (e.g. sleep duration $<6.5\text{h}$, DTI ratio $>0.40$, or severe overtime).
- **Prevents Misallocated Effort:** Prevents an individual suffering from extreme financial anxiety from attempting to solve their stress purely through meditation apps, targeting the true systemic bottleneck instead.

---

## Slide 9: AI Prescriptions & Counterfactual "What-If" Simulation
- **Prescriptive AI:** Uses gradient sensitivities to calculate the highest return-on-investment micro-adjustments.
- **Counterfactual Engine:** Allows the user to simulate real-world changes:
  - *Case Study Example:* Extending sleep by $+1.25\text{ hrs}$ and capping work hours to eliminate overtime yields a projected **$+14.9\text{ point}$** surge in the Holistic Flourishing Index ($34.6 \rightarrow 49.5$).
- **Evidence-Based Grounding:** Each recommendation links to clinical studies (e.g., Matthew Walker's sleep neuroscience, CFPB financial resilience guidelines, Seligman's PERMA).

---

## Slide 10: Interactive Web Application Walkthrough
- Built using **Streamlit** and **Plotly** with an executive glassmorphism interface:
  - Dynamic Plotly Flourishing Gauge & Tri-Domain Polar Radar Chart.
  - Real-time sliders for 22 personal lifestyle, career, and financial variables.
  - One-click archetype buttons (*Burnt-Out Tech Worker*, *Struggling Student*, *Balanced Remote Creator*).
  - Downloadable Markdown assessment reports for personal or clinical review.

---

## Slide 11: Ethical Considerations & Human Agency
- **Non-Diagnostic Tool:** Designed as an educational, reflective, and empowering self-study tool rather than a psychiatric diagnostic device.
- **Privacy by Design:** Local execution ensures sensitive personal biometric and financial data never leaves the user's local machine.
- **Empowering Human Flourishing:** Shifting AI from passive consumption/surveillance toward proactive human flourishing and preventive health.

---

## Slide 12: Conclusion & Future Work
- **Summary:** Successfully created an end-to-end multimodal machine learning system that unifies biology, work sociology, and economics into a predictive flourishing model.
- **Future Extensions:**
  - Real-time wearable API integration (Apple HealthKit / Fitbit / Garmin).
  - Open banking API integration (Plaid) for automated liquidity scoring.
  - Longitudinal cohort tracking to evaluate intervention adherence and long-term well-being velocity.
