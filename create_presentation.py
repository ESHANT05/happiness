"""
Generates a clean, minimal, humanised academic presentation (.pptx)
for the project evaluation.
Focuses on clarity, simple layout, zero artificial fluff, and clean typography.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_filename="Personal_Wellbeing_Research_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Clean, minimal color palette (light, academic, high contrast)
    BG_COLOR = RGBColor(255, 255, 255)       # Pure white
    CARD_BG = RGBColor(248, 250, 252)        # Very light slate (for clean boxes)
    CARD_BORDER = RGBColor(226, 232, 240)    # Light gray border
    TEXT_MAIN = RGBColor(15, 23, 42)         # Deep slate navy
    TEXT_MUTED = RGBColor(71, 85, 105)       # Neutral slate gray
    ACCENT_BLUE = RGBColor(37, 99, 235)      # Crisp royal blue
    LINE_COLOR = RGBColor(203, 213, 225)     # Subtle divider gray

    def set_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, category_text, title_text):
        set_slide_bg(slide)
        
        # Category label
        tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.35))
        p_cat = tb_cat.text_frame.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Calibri"
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_BLUE

        # Slide title
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(0.7))
        p_title = tb_title.text_frame.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_MAIN

        # Thin clean divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.015))
        line.fill.solid()
        line.fill.fore_color.rgb = LINE_COLOR
        line.line.fill.background()

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)

    # Decorative top bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(1.2), Inches(0.08))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_BLUE
    bar.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.5), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "Predictive Modeling of Personal Well-being using Lifestyle, Occupational, and Financial Data"
    p.font.name = "Calibri"
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_after = Pt(14)

    p2 = tf1.add_paragraph()
    p2.text = "An Ensemble Machine Learning Approach to Individual Happiness and Flourishing Factors"
    p2.font.name = "Calibri"
    p2.font.size = Pt(18)
    p2.font.color.rgb = ACCENT_BLUE
    p2.space_after = Pt(24)

    p3 = tf1.add_paragraph()
    p3.text = "Subject: Science of Happiness & Human Flourishing — Independent Self-Study Research"
    p3.font.name = "Calibri"
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_after = Pt(6)

    p4 = tf1.add_paragraph()
    p4.text = "Project Type: End-to-End Machine Learning System & Interactive Dashboard"
    p4.font.name = "Calibri"
    p4.font.size = Pt(14)
    p4.font.color.rgb = TEXT_MUTED
    p4.space_after = Pt(6)

    p5 = tf1.add_paragraph()
    p5.text = "Evaluation Status: Group Research Presentation & Model Demonstration"
    p5.font.name = "Calibri"
    p5.font.size = Pt(14)
    p5.font.bold = True
    p5.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 2: MOTIVATION & PROBLEM STATEMENT
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Motivation & Problem Statement", "Why We Need a Multi-Domain Approach to Happiness")

    def add_card(slide, left, top, width, height, title, points):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = CARD_BORDER
        box.line.width = Pt(1)

        tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.name = "Calibri"
        p0.font.size = Pt(16)
        p0.font.bold = True
        p0.font.color.rgb = TEXT_MAIN
        p0.space_after = Pt(10)

        for pt_text in points:
            pi = tf.add_paragraph()
            pi.text = "• " + pt_text
            pi.font.name = "Calibri"
            pi.font.size = Pt(13)
            pi.font.color.rgb = TEXT_MUTED
            pi.space_after = Pt(8)

    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), 
             "1. The Problem with Single-Domain Studies", [
                 "Most happiness surveys only ask people for a single score from 1 to 10 without explaining why.",
                 "Health researchers only measure sleep or diet, while economists only look at income and inflation.",
                 "Human life does not operate in silos: a bad night of sleep ruins workday focus, and constant money stress ruins physical health.",
                 "We lack practical tools that connect everyday lifestyle, job pressure, and personal finances together."
             ])

    add_card(s2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), 
             "2. What Our Project Sets Out to Do", [
                 "Build an end-to-end Machine Learning pipeline that treats personal well-being as an interconnected system.",
                 "Train dedicated ML models for each of the three major life pillars: Biology, Workplace, and Personal Finances.",
                 "Combine these into a master ensemble that predicts overall flourishing and life satisfaction.",
                 "Pinpoint an individual's primary 'bottleneck' (the weakest domain holding them back) and recommend realistic fixes."
             ])

    # ==========================================
    # SLIDE 3: KEY CONCEPTS & THE THREE DOMAINS
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Key Concepts", "The Three Core Pillars of Everyday Well-being")

    col_w = Inches(3.65)
    gap = Inches(0.38)
    top_pos = Inches(1.8)
    card_h = Inches(4.8)

    add_card(s3, Inches(0.8), top_pos, col_w, card_h, "1. Biological & Lifestyle", [
        "Focus: Physical energy, recovery, and daily movement.",
        "Key Inputs: Sleep duration, sleep quality, daily step count, active exercise minutes, resting heart rate, and sitting hours.",
        "Target Output: Vitality Score (0-100) and Daily Stress Level (1-10).",
        "Core Idea: Sleep and movement are foundational biological requirements for emotional stability."
    ])

    add_card(s3, Inches(0.8) + col_w + gap, top_pos, col_w, card_h, "2. Occupational & Work", [
        "Focus: Day-to-day job demands, control, and workplace balance.",
        "Key Inputs: Total weekly work hours, mandatory overtime, remote work flexibility, job autonomy, commute time, and team support.",
        "Target Output: Job Fulfillment (0-100) and Burnout Risk Tier.",
        "Core Idea: Having control and clear boundaries at work protects against long-hour burnout."
    ])

    add_card(s3, Inches(0.8) + (col_w + gap) * 2, top_pos, col_w, card_h, "3. Financial & Security", [
        "Focus: Financial safety net, debt load, and peace of mind.",
        "Key Inputs: Annual income, debt-to-income ratio, monthly savings rate, emergency fund buffer (months of expenses), and local cost of living.",
        "Target Output: Financial Security (0-100) and Anxiety Level.",
        "Core Idea: Cash buffer and low debt create peace of mind far more reliably than raw salary alone."
    ])

    # ==========================================
    # SLIDE 4: RELEVANT LITERATURE
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Relevant Literature & Theory", "Academic Foundations Behind Our Features and Metrics")

    add_card(s4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), 
             "Psychology & Workplace Research", [
                 "Seligman's PERMA Model: Defines flourishing through Positive emotion, Engagement, Relationships, Meaning, and Accomplishment.",
                 "Cantril Self-Anchoring Ladder: The benchmark global life-evaluation scale (1-10) used by Gallup and the UN World Happiness Report.",
                 "Karasek's Job Demand-Control Model: Demonstrates that heavy workloads only trigger acute burnout when individuals lack decision latitude and autonomy.",
                 "Boundary Theory (Clark, 2000): Studies how remote and hybrid work blur lines between career responsibilities and restorative personal time."
             ])

    add_card(s4, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), 
             "Health Science & Financial Economics", [
                 "Sleep Architecture & Allostatic Load (Walker / NSF): Chronic sleep restriction (<6.5 hrs) impairs emotional regulation and spikes physiological stress.",
                 "CFPB Financial Well-Being Scale: Large-scale studies by the US Consumer Financial Protection Bureau showing subjective security is tied to liquidity, not gross income.",
                 "Buffer-Stock Theory of Savings: Proves that maintaining 3 to 6 months of liquid reserves sharply insulates individuals against daily anxiety.",
                 "Liebig's Law of the Minimum: A biological principle applied here to human well-being: overall flourishing is limited by whichever basic domain is most depleted."
             ])

    # ==========================================
    # SLIDE 5: PROPOSED RESEARCH APPROACH
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Proposed Research Approach", "Data Engineering and the Modeling Workflow")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), 
             "Step 1: Statistically Calibrated Data Generation", [
                 "Because real-world multi-domain cohorts are rarely released in a single public file, we built an empirical data engine.",
                 "Distributions are anchored to real benchmarks: CDC/Fitbit sleep & activity data, IBM HR workplace statistics, and CFPB financial survey distributions.",
                 "Built-in Cross-Domain Feedback Loops: High overtime explicitly reduces sleep duration; financial anxiety directly impairs sleep quality.",
                 "Generated 3,500 samples per domain, plus a 4,000-sample integrated cohort for master ensemble training."
             ])

    add_card(s5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), 
             "Step 2: Two-Tier Machine Learning Pipeline", [
                 "Tier 1 (Domain Models): Three independent models trained on domain features using RandomForest and GradientBoosting with standard scalers.",
                 "Tier 2 (Stacking Ensemble): Takes the three predicted scores plus interaction terms (mean score, minimum domain score, and synergy terms).",
                 "Ensemble Meta-Learner: Predicts the Holistic Human Flourishing Index (0-100) and the Cantril Life Ladder (1-10).",
                 "Validation Setup: 80% train / 20% test split, evaluating R-squared, Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE)."
             ])

    # ==========================================
    # SLIDE 6: PRELIMINARY EXPERIMENTAL RESULTS
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Preliminary Experimental Results", "Quantitative Performance Across All Four Models")

    # Let's add a clear, clean table for experimental results
    table_shape = s6.shapes.add_table(5, 5, Inches(0.8), Inches(1.9), Inches(11.7), Inches(2.2))
    table = table_shape.table

    # Column widths
    table.columns[0].width = Inches(3.2)
    table.columns[1].width = Inches(2.8)
    table.columns[2].width = Inches(1.9)
    table.columns[3].width = Inches(1.9)
    table.columns[4].width = Inches(1.9)

    headers = ["Model Pipeline", "Primary Algorithm", "R² Score", "RMSE", "MAE"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = CARD_BG
        p = cell.text_frame.paragraphs[0]
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = TEXT_MAIN

    rows_data = [
        ["1. Lifestyle & Biological Health", "Random Forest Regressor", "0.880", "4.19", "3.37"],
        ["2. Workplace & Occupational", "Gradient Boosting Regressor", "0.924", "3.20", "2.59"],
        ["3. Financial & Socio-Economic", "Random Forest Regressor", "0.943", "4.06", "3.26"],
        ["4. Master Flourishing Ensemble", "Gradient Boosting Meta-Learner", "0.810", "4.34", "3.42"]
    ]

    for row_idx, r_data in enumerate(rows_data, start=1):
        for col_idx, val in enumerate(r_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Calibri"
            p.font.size = Pt(13)
            if col_idx == 0:
                p.font.bold = True
                p.font.color.rgb = TEXT_MAIN
            elif col_idx == 2:
                p.font.bold = True
                p.font.color.rgb = ACCENT_BLUE
            else:
                p.font.color.rgb = TEXT_MUTED

    # Takeaway card beneath table
    add_card(s6, Inches(0.8), Inches(4.4), Inches(11.7), Inches(2.2), 
             "Summary of Results", [
                 "All three domain models demonstrate high predictive accuracy on unseen test data (R² between 0.880 and 0.943).",
                 "The Master Stacking Ensemble achieves R² = 0.810 with a low Mean Absolute Error of 3.42 points on a 0-100 scale.",
                 "This confirms that combining separate domain outputs yields a consistent, well-calibrated measure of personal flourishing."
             ])

    # ==========================================
    # SLIDE 7: KEY EMPIRICAL FINDINGS
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Key Empirical Findings", "What the Model Feature Importances Taught Us")

    add_card(s7, Inches(0.8), top_pos, col_w, card_h, "1. Savings Buffer > Salary", [
        "In the financial model, emergency fund buffer accounted for 79.3% of feature importance.",
        "Gross annual income accounted for only 7.6%.",
        "Takeaway: Having 3-6 months of living expenses saved in cash provides far more subjective peace of mind than earning a higher salary with zero backup."
    ])

    add_card(s7, Inches(0.8) + col_w + gap, top_pos, col_w, card_h, "2. Autonomy > Work Hours", [
        "In the workplace model, work-life balance rating (45.2%) and job autonomy (15.9%) dominated raw weekly hours (4.3%).",
        "Overtime demands accounted for nearly 10% of burnout risk.",
        "Takeaway: People can tolerate busy periods if they have say over how they work and clear evening boundaries."
    ])

    add_card(s7, Inches(0.8) + (col_w + gap) * 2, top_pos, col_w, card_h, "3. The 'Weakest Link' Rule", [
        "In the Master Ensemble, the lowest domain score (min_domain_score) carried 16.0% of the total predictive weight.",
        "Average score carried 73.4%, while cross-domain interaction terms made up the rest.",
        "Takeaway: You cannot out-exercise severe debt, nor can you buy your way out of total sleep deprivation. A deficit in one area drags down the whole."
    ])

    # ==========================================
    # SLIDE 8: THE HAPPINESS BOTTLENECK & PRESCRIPTIONS
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Bottleneck Diagnosis & Prescriptive AI", "Turning Predictions into Practical Interventions")

    add_card(s8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), 
             "1. Happiness Bottleneck Identification", [
                 "Instead of generic self-help advice, our system calculates which life domain is acting as the primary constraint.",
                 "Automated Root Cause Diagnosis: Looks at exact personal inputs (e.g., averaging 5.5 hours sleep, working mandatory overtime, or holding a 0.85 debt ratio).",
                 "Prevents Wasted Effort: If someone's main crisis is debt, telling them to meditate will not solve their stress. The model directs attention to the actual root cause."
             ])

    add_card(s8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), 
             "2. Counterfactual 'What-If' Simulation", [
                 "The engine tests realistic adjustments to find which change gives the highest point uplift on the Flourishing Index.",
                 "Example (Burnt-Out Tech Profile):",
                 "  • Baseline Flourishing: 34.6 / 100 (Distressed)",
                 "  • Intervention 1 (Sleep): Adding +1.2 hrs sleep yields +11.8 pts.",
                 "  • Intervention 2 (Work boundaries): Capping overtime yields +8.4 pts.",
                 "  • Multi-Domain Combination: Both together produce a +14.9 pt gain (reaching 49.5 pts), pulling the individual out of the red zone."
             ])

    # ==========================================
    # SLIDE 9: INTERACTIVE WEB DASHBOARD
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Interactive Implementation", "Overview of the Live Working Dashboard")

    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), 
             "Interactive Features (Built with Streamlit & Plotly)", [
                 "Real-Time Input Panel: 22 personal sliders covering physical health, job conditions, and personal finances.",
                 "Instant Archetype Buttons: Four pre-configured personas (Burnt-Out Tech Worker, Struggling Student, Balanced Remote Creator, Stressed Urban Commuter) for quick testing.",
                 "Live Visualizations: Plotly Flourishing Gauge (0-100), Cantril Ladder indicator, and a Tri-Domain Radar Chart comparing scores against the healthy benchmark (85+).",
                 "One-Click Report Export: Generates a clinical/academic Markdown report summarizing scores, root causes, and recommended fixes."
             ])

    add_card(s9, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), 
             "Why This Matters for Practical Use", [
                 "Accessible Interface: Can be run by anyone locally in a standard browser with a single batch click (run_dashboard.bat).",
                 "Fast Inference: All four ML models run inference in less than 50 milliseconds.",
                 "Privacy-First Architecture: Runs 100% locally on the user's laptop; personal health and income details never leave the machine.",
                 "Transparent Decisions: The dashboard includes a dedicated tab showing all model accuracy metrics and feature importance charts."
             ])

    # ==========================================
    # SLIDE 10: CONCLUSION & EVALUATION READINESS
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Conclusion & Team Preparedness", "Summary of Work and Q&A Readiness")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), 
             "Summary of Research Contributions", [
                 "Successfully modeled personal well-being across biology, workplace, and finance using an ensemble ML system.",
                 "Validated that well-being follows non-linear interaction rules, where the weakest domain caps overall flourishing.",
                 "Demonstrated that liquidity buffers and job autonomy are stronger contributors to subjective happiness than raw salary and hours.",
                 "Delivered a working web application, fully documented codebase, and verified pre-trained model artifacts on GitHub."
             ])

    add_card(s10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), 
             "Group Evaluation & Question Readiness", [
                 "All group members are present and prepared to answer evaluator questions regarding:",
                 "  1. Dataset construction, feature selection, and synthetic calibration.",
                 "  2. Algorithms used (Random Forest, Gradient Boosting, Stacking Ensemble) and metrics (R², RMSE, MAE).",
                 "  3. Psychological and economic foundations (PERMA, Karasek, CFPB).",
                 "  4. Live demonstration of the web dashboard and counterfactual simulator.",
                 "Ready for questions and interactive demonstration."
             ])

    # Save presentation
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_filename)
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    create_deck()
