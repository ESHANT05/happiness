@echo off
echo ======================================================================
echo Launching Personal Well-being & Human Flourishing ML Dashboard
echo Project: Predictive Modeling of Personal Well-being using Lifestyle,
echo          Occupational, and Financial Data
echo ======================================================================
cd /d "%~dp0"
streamlit run app.py
pause
