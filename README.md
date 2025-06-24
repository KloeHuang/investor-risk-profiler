# 📊 Investor Risk Profiler & Strategy Recommender

This MVP is developed for the FinTech: Business Models and Applications course at RSM. It helps users understand their investment risk profile through a simple questionnaire and provides personalized ETF-based investment strategy recommendations.

---

## 🚀 Key Features

- **Risk Profiling Questionnaire**: Assesses user risk level via 10 intuitive questions.
- **Personalized Investment Strategy**: Recommends strategies and ETF portfolio compositions based on risk level.
- **Portfolio Performance Simulation**: Visualizes historical performance for selected ETFs using Yahoo Finance data.
- **User Feedback Collection**: Collects user satisfaction on profiling and strategy results.

---

## 📋 Questionnaire Design Rationale

The questionnaire design is grounded in academic frameworks:

- So, M. K. P. (2021). *Robo-Advising Risk Profiling through Content Analysis for Sustainable Development* ([Sustainability, 13(3), 1306](https://doi.org/10.3390/su13031306))  
- Lippi, A., & Poli, F. (2025). *ESG in Investor Profiling* ([IJBM, 43(1)](https://doi.org/10.1108/IJBM-11-2023-0609))

---

## 📊 Visualizations Explained

1. **ETF-Specific Portfolio Simulation**  
   After selecting an ETF (e.g., SPY, QQQ), the app simulates how a lump-sum investment would have grown over a chosen time frame, using 5-year historical price data.  
   - Purpose: Demonstrates real market volatility and long-term return potential for each fund.

2. **Recommended Portfolio Simulation**  
   Based on the user’s risk category, a weighted ETF combination (e.g., 60% QQQ + 40% EEM for aggressive profiles) is simulated.  
   - Purpose: Shows how a balanced portfolio might perform and educates users on asset allocation concepts.
---

## 🧠 Technology Stack

- **Programming Language**: Python
- **Framework**: Streamlit (for building the web app)
- **Data Source**: [Yahoo Finance](https://finance.yahoo.com/) via `yfinance` API
- **Visualization**: `matplotlib`
- **User Feedback Handling**: stored in local CSV file (`user_feedback.csv`)

---

## 🧭 How to Run It Locally

### 🧰 Requirements

Make sure you have Python 3.7+ installed. Then run:

```bash
pip install -r requirements.txt
```

### ▶️ Start the App

```bash
streamlit run main.py
```

This will launch the app in your default web browser.

---

## 📂 Project Structure

```text
investor-risk-profiler/
│
├── main.py                # Main application script
├── user_feedback.csv      # (Auto-created) feedback log
├── README.md              # Project documentation
└── requirements.txt       # List of Python packages needed
```

---

## 📌 Limitations

- Real-time ETF recommendation engine is rule-based and does not yet include AI optimization.
- Feedback data is stored locally and not connected to a cloud backend.
- Synthetic user profiling is basic; future iterations can include demographic segmentation.

---

## ⚖️ License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).

---

## 📫 Contact

This project was developed by **Kloe Huang** as part of the FinTech MVP assignment at Rotterdam School of Management.
