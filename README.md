# 📊 Investor Risk Profiler & Strategy Recommender

This MVP is developed for the FinTech: Business Models and Applications course at RSM. It helps users understand their investment risk profile through a simple questionnaire and provides personalized ETF-based investment strategy recommendations.

---

## 🚀 Key Features

- **Risk Profiling Questionnaire**: Assesses user risk level via 10 intuitive questions.
- **Personalized Investment Strategy**: Recommends strategies and ETF portfolio compositions based on risk level.
- **Portfolio Performance Simulation**: Visualizes historical performance for selected ETFs using Yahoo Finance data.
- **User Feedback Collection**: Collects user satisfaction on profiling and strategy results.

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
