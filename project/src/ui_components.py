import streamlit as st
from datetime import datetime

def setup_sidebar():
    """
    Configura os elementos da barra lateral do Streamlit.
    """
    symbols = st.sidebar.text_input(
        "Digite os símbolos das ações separados por vírgula (ex: PETR4.SA, VALE3.SA, BBAS3.SA)",
        "PETR4.SA, VALE3.SA"
    )
    
    period_choice = st.sidebar.radio("Escolha o tipo de período", ("Período predefinido", "Intervalo de datas"))
    
    if period_choice == "Período predefinido":
        period = st.sidebar.selectbox("Escolha o período", ["1mo", "3mo", "6mo", "1y", "5y"])
        start_date = end_date = None
    else:
        period = None
        start_date = st.sidebar.date_input("Data inicial", datetime.now().replace(month=1, day=1))
        end_date = st.sidebar.date_input("Data final", datetime.now())
        
        if start_date > end_date:
            st.sidebar.error("A data final deve ser posterior à data inicial.")
    
    return symbols, period_choice, period, start_date, end_date

def display_metrics(ticker: str, metrics: dict):
    """
    Exibe as métricas de volatilidade na barra lateral.
    """
    st.sidebar.write(f"**{ticker}**")
    st.sidebar.write(f"Volatilidade anualizada: {round(metrics['volatility'] * 100, 2)}%")
    st.sidebar.write(f"Média da volatilidade anualizada: {round(metrics['avg_volatility'] * 100, 2)}%")
    st.sidebar.write(f"Preço máximo: R$ {round(metrics['max_price'], 2)}")
    st.sidebar.write(f"Preço mínimo: R$ {round(metrics['min_price'], 2)}")
    st.sidebar.write("---")