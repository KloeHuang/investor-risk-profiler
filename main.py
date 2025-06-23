import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Investor Risk Profiler", layout="centered")
st.title("📊 Investor Risk Profiling Questionnaire")

st.markdown("""
Answer the questions below to understand your investment risk profile and receive a recommended strategy.
""")

# --- User ID Input ---
user_id = st.text_input("Please enter your user ID (or initials):",
    help="For testing, you can simply enter e.g. '0001', 'testA', or your initials.")

if not user_id:
    st.warning("⚠️ Please enter a user ID to continue.")
    st.stop()

# --- Section 1: Investment Questionnaire ---
q1 = st.radio("1. What is your intended investment horizon?",
              ["", "Less than 1 year", "1–3 years", "3–5 years", "More than 5 years"], key="q1")
q2 = st.radio("2. What is your expected annual return?",
              ["", "Less than 3%", "3%–6%", "6%–10%", "Above 10%"], key="q2")
q3 = st.radio("3. What would you do if your investment dropped 20% in the short term?",
              ["", "Sell all", "Sell part", "Do nothing", "Buy more"], key="q3")
q4 = st.radio("4. What is the maximum annual loss you could tolerate?",
              ["", "Less than 5%", "5%–10%", "10%–15%", "More than 15%"], key="q4")
q5 = st.multiselect("5. What have you invested in before?",
                    ["Deposits", "Bonds", "Stocks", "Derivatives, Mutual Funds, ETFs"], key="q5")
q6 = st.radio("6. How would you rate your investment knowledge?",
              ["", "Novice", "Moderate", "Knowledgeable", "Professional"], key="q6")
q7 = st.radio("7. When markets fluctuate sharply, you are more likely to:",
              ["", "Feel anxious and exit", "Monitor but worry", "Analyze and hold", "Rebalance or buy more"], key="q7")
q8 = st.radio("8. How much risk are you willing to take for higher returns?",
              ["", "Very little", "Some", "Moderate", "High risk"], key="q8")
q9 = st.radio("9. Is your income stable and predictable?",
              ["", "Very unstable", "Sometimes fluctuating", "Relatively stable", "Very stable"], key="q9")
q10 = st.radio("10. What percentage of your total assets do you plan to invest?",
               ["", "More than 75%", "50%–75%", "25%–50%", "Less than 25%"], key="q10")

# --- Save state and simulate below ---
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "profile" not in st.session_state:
    st.session_state.profile = None

if st.button("Submit Questionnaire"):
    required_responses = [q1, q2, q3, q4, q6, q7, q8, q9, q10]
    if "" in required_responses:
        st.error("❗ Please answer all required questions.")
    else:
        score_map = {
            "Less than 1 year": 1, "1–3 years": 2, "3–5 years": 3, "More than 5 years": 4,
            "Less than 3%": 1, "3%–6%": 2, "6%–10%": 3, "Above 10%": 4,
            "Sell all": 1, "Sell part": 2, "Do nothing": 3, "Buy more": 4,
            "Less than 5%": 1, "5%–10%": 2, "10%–15%": 3, "More than 15%": 4,
            "Novice": 1, "Moderate": 2, "Knowledgeable": 3, "Professional": 4,
            "Feel anxious and exit": 1, "Monitor but worry": 2, "Analyze and hold": 3, "Rebalance or buy more": 4,
            "Very little": 1, "Some": 2, "Moderate": 3, "High risk": 4,
            "Very unstable": 1, "Sometimes fluctuating": 2, "Relatively stable": 3, "Very stable": 4,
            "More than 75%": 1, "50%–75%": 2, "25%–50%": 3, "Less than 25%": 4
        }

        total_score = sum([
            score_map[q1], score_map[q2], score_map[q3], score_map[q4],
            score_map[q6], score_map[q7], score_map[q8], score_map[q9], score_map[q10]
        ])

        q5_score_map = {
            "Deposits": 0, "Bonds": 1, "Stocks": 2, "Derivatives, Mutual Funds, ETFs": 3
        }
        q5_score = max([q5_score_map[ans] for ans in q5]) if q5 else 0
        total_score += q5_score

        if total_score <= 17:
            profile = "🟦 Conservative"
            strategy = "Focus on capital preservation: 80% bonds, 15% large-cap stocks, 5% cash."
        elif total_score <= 24:
            profile = "🟩 Moderate"
            strategy = "Balanced approach: 50% stocks, 40% bonds, 10% alternatives."
        elif total_score <= 32:
            profile = "🟨 Growth"
            strategy = "Higher growth potential: 70% stocks, 25% bonds, 5% cash."
        else:
            profile = "🟥 Aggressive"
            strategy = "Maximize growth: 90% equities, including emerging markets."

        st.session_state.submitted = True
        st.session_state.profile = profile
        st.session_state.strategy = strategy

if st.session_state.submitted:
    st.subheader("📈 Your Risk Profile")
    st.success(f"You are classified as: {st.session_state.profile}")
    st.markdown(f"**Recommended Strategy:** {st.session_state.strategy}")

    st.markdown("---")
    st.subheader("💰 Simulate Your Investment Portfolio")
    initial_investment = st.number_input("Initial Investment Amount (EUR)", min_value=1000, value=10000, step=500)
    investment_years = st.slider("Investment Duration (Years)", 1, 30, 10)

    # Fix: Move dictionary definition to correct position
    profile_to_etfs = {
        "🟦 Conservative": ["VEA (Developed Markets ex-US)", "VTI (Total US Market)"],
        "🟩 Moderate": ["SPY (S&P 500)", "VTI (Total US Market)"],
        "🟨 Growth": ["QQQ (Nasdaq 100)", "SPY (S&P 500)"],
        "🟥 Aggressive": ["QQQ (Nasdaq 100)", "EEM (Emerging Markets)"]
    }

    etf_options = {
        "SPY (S&P 500)": "SPY",
        "QQQ (Nasdaq 100)": "QQQ",
        "VTI (Total US Market)": "VTI",
        "VEA (Developed Markets ex-US)": "VEA",
        "EEM (Emerging Markets)": "EEM"
    }

    # Fix: Get recommended ETF default value
    recommended_labels = profile_to_etfs.get(st.session_state.profile, ["SPY (S&P 500)"])
    recommended_default = recommended_labels[0]
    st.markdown(
        f"Based on your profile {st.session_state.profile}, we recommend starting with: **{recommended_default}**")

    etf_reasons = {
        "SPY (S&P 500)": "Broad market exposure to large-cap U.S. companies.",
        "QQQ (Nasdaq 100)": "Focused on technology and growth-oriented companies.",
        "VTI (Total US Market)": "Diversified U.S. equity exposure including small and mid caps.",
        "VEA (Developed Markets ex-US)": "Exposure to developed markets outside of the U.S.",
        "EEM (Emerging Markets)": "High-risk, high-return exposure to emerging economies."
    }

    # ETF explanation information
    with st.expander("ℹ️ ETF Explanations"):
        for name, reason in etf_reasons.items():
            st.markdown(f"**{name}**: {reason}")

    # Fix: Ensure default selection is in options list
    default_index = 0
    if recommended_default in etf_options:
        default_index = list(etf_options.keys()).index(recommended_default)

    selected_label = st.selectbox(
        "Choose an ETF to simulate portfolio performance:",
        options=list(etf_options.keys()),
        index=default_index
    )

    st.caption(f"📌 Why this ETF? {etf_reasons.get(selected_label, '')}")

    etf_symbol = etf_options[selected_label]

    try:
        ticker = yf.Ticker(etf_symbol)
        price_data = ticker.history(period="5y")["Close"]
        info = ticker.info

        # 添加数据验证
        if price_data.empty:
            st.warning(f"No price data available for {etf_symbol}")
        else:
            st.caption(
                f"Data source: {etf_symbol} historical prices from Yahoo Finance via yfinance API. Past performance does not guarantee future results.")

            # 安全地获取信息
            short_name = info.get('shortName', etf_symbol)
            long_summary = info.get('longBusinessSummary', 'No description available.')
            # 截断过长的描述
            if len(long_summary) > 300:
                long_summary = long_summary[:300] + "..."

            st.markdown(f"**{short_name}** — {long_summary}")

            price = info.get('currentPrice') or info.get('previousClose', 'N/A')
            category = info.get('category', 'N/A')
            st.markdown(f"**Current Price**: ${price} | **Category**: {category}")

            # Calculate annual returns
            annual_returns = price_data.resample("Y").last().pct_change().dropna().tolist()

            # If insufficient historical data, fill with average returns
            if len(annual_returns) > 0:
                avg_return = np.mean(annual_returns)
                while len(annual_returns) < investment_years:
                    annual_returns.append(avg_return)
            else:
                # If no historical data, use assumed return rate
                annual_returns = [0.07] * investment_years  # Assume 7% annual return

            # Simulate portfolio growth
            portfolio = [initial_investment]
            for r in annual_returns[:investment_years]:
                portfolio.append(portfolio[-1] * (1 + r))

            # Plot chart
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(range(investment_years + 1), portfolio, marker='o', linewidth=2)
            ax.set_title(f"Simulated Portfolio Growth ({etf_symbol})")
            ax.set_xlabel("Year")
            ax.set_ylabel("Portfolio Value (EUR)")
            ax.grid(True, alpha=0.3)

            # Format Y-axis as currency
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'€{x:,.0f}'))

            st.pyplot(fig)
            plt.close()  # Prevent memory leaks

            # Display final value and returns
            final_value = portfolio[-1]
            total_return = (final_value - initial_investment) / initial_investment * 100
            st.metric("Final Portfolio Value", f"€{final_value:,.2f}", f"{total_return:+.1f}%")

    except Exception as e:
        st.error(
            f"⚠️ Failed to retrieve data for {etf_symbol}. Please try another ETF or check your internet connection.")
        st.error(f"Error details: {str(e)}")

    # 🎯 Recommended Portfolio Simulation
    try:
        st.subheader("📊 Simulated Recommended Portfolio")

        weights_map = {
            "🟦 Conservative": {"VEA": 0.6, "VTI": 0.4},
            "🟩 Moderate": {"SPY": 0.5, "VTI": 0.5},
            "🟨 Growth": {"QQQ": 0.6, "SPY": 0.4},
            "🟥 Aggressive": {"QQQ": 0.6, "EEM": 0.4}
        }

        weights = weights_map.get(st.session_state.profile, {"SPY": 1.0})

        # Display portfolio allocation
        st.write("**Portfolio Allocation:**")
        for ticker_sym, weight in weights.items():
            st.write(f"- {ticker_sym}: {weight * 100:.0f}%")

        # Get price data for all ETFs
        combined_returns = []
        valid_tickers = []

        for ticker_sym in weights:
            try:
                ticker_data = yf.Ticker(ticker_sym)
                price_data = ticker_data.history(period="5y")["Close"]

                if not price_data.empty:
                    annual_returns = price_data.resample("Y").last().pct_change().dropna()
                    if len(annual_returns) > 0:
                        combined_returns.append(annual_returns.tolist())
                        valid_tickers.append(ticker_sym)

            except Exception as e:
                st.warning(f"Could not fetch data for {ticker_sym}: {str(e)}")
                continue

        if combined_returns and valid_tickers:
            # Ensure all data has consistent length
            min_length = min(len(returns) for returns in combined_returns)
            if min_length > 0:
                # Calculate weighted returns
                portfolio_returns = []
                for i in range(min(min_length, investment_years)):
                    weighted_return = 0
                    for j, ticker_sym in enumerate(valid_tickers):
                        if i < len(combined_returns[j]):
                            ticker_weight = weights.get(ticker_sym, 0)
                            weighted_return += ticker_weight * combined_returns[j][i]
                    portfolio_returns.append(weighted_return)

                # Fill with average if insufficient data
                if len(portfolio_returns) > 0:
                    avg_return = np.mean(portfolio_returns)
                    while len(portfolio_returns) < investment_years:
                        portfolio_returns.append(avg_return)

                # Calculate portfolio values
                portfolio_values = [initial_investment]
                for r in portfolio_returns[:investment_years]:
                    portfolio_values.append(portfolio_values[-1] * (1 + r))

                # Plot recommended portfolio chart
                fig2, ax2 = plt.subplots(figsize=(10, 6))
                ax2.plot(range(len(portfolio_values)), portfolio_values,
                         marker='s', linestyle='--', linewidth=2, color='green')
                ax2.set_title("Recommended Portfolio Growth")
                ax2.set_xlabel("Year")
                ax2.set_ylabel("Portfolio Value (EUR)")
                ax2.grid(True, alpha=0.3)
                ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'€{x:,.0f}'))

                st.pyplot(fig2)
                plt.close()

                # Display recommended portfolio final value
                final_portfolio_value = portfolio_values[-1]
                portfolio_total_return = (final_portfolio_value - initial_investment) / initial_investment * 100
                st.metric("Recommended Portfolio Final Value",
                          f"€{final_portfolio_value:,.2f}",
                          f"{portfolio_total_return:+.1f}%")
            else:
                st.warning("Insufficient historical data for portfolio simulation.")
        else:
            st.warning("Could not fetch sufficient data for recommended portfolio simulation.")

    except Exception as e:
        st.error(f"Error in recommended portfolio simulation: {str(e)}")

    # save users feedback
    st.markdown("---")
    st.subheader("📝 Feedback")

    agree_profile = st.radio("Do you agree with your risk profile classification?", ["Yes", "No", "Not sure"])
    agree_recommendation = st.radio("Do you agree with the ETF recommendation and strategy?", ["Yes", "No", "Somewhat"])

    if st.button("Submit Feedback"):
        feedback = {
            "user_id": user_id,
            "timestamp": datetime.datetime.now(),
            "Risk_Profile": st.session_state.profile,
            "Agree_Profile": agree_profile,
            "Agree_Recommendation": agree_recommendation
        }

        # save the feedback as csv, if no csv exists, then create a new one
        feedback_df = pd.DataFrame([feedback])
        try:
            existing_df = pd.read_csv("user_feedback.csv")
            combined_df = pd.concat([existing_df, feedback_df], ignore_index=True)
        except FileNotFoundError:
            combined_df = feedback_df

        combined_df.to_csv("user_feedback.csv", index=False)
        st.success("✅ Thank you! Your feedback has been saved.")

#Note: For MVP demo purposes, user feedback is currently saved as a local CSV file.
#In a full deployment scenario, this can be replaced with a Google Sheets API or database solution.

