import streamlit as st
from src.data_loader import load_stock_data
from src.calculations import calculate_volatility_metrics
from src.ui_components import setup_sidebar, display_metrics

def main():
    st.title("Monitor de Volatilidade de Ações")
    
    # Configuração da barra lateral
    symbols, period_choice, period, start_date, end_date = setup_sidebar()
    
    # Período descriptions
    period_descriptions = {
        "1mo": "Último mês",
        "3mo": "Últimos 3 meses",
        "6mo": "Últimos 6 meses",
        "1y": "Último ano",
        "5y": "Últimos 5 anos"
    }
    
    # Processar cada ticker
    tickers = [symbol.strip() for symbol in symbols.split(",")]
    cols = st.columns(4)
    
    for i, ticker in enumerate(tickers):
        # Carregar dados
        data = load_stock_data(ticker, period_choice, period, start_date, end_date)
        
        # Calcular métricas
        metrics = calculate_volatility_metrics(data)
        
        # Exibir métricas na barra lateral
        display_metrics(ticker, metrics)
        
        # Exibir gráfico
        period_text = (f"de {start_date} a {end_date}" 
                      if period_choice == "Intervalo de datas" 
                      else f"({period_descriptions[period]})")
        
        with cols[i % 4]:
            st.write(f"Volatilidade de {ticker} {period_text}")
            st.line_chart(metrics['daily_returns'])

if __name__ == "__main__":
    main()