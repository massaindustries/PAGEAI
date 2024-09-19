import streamlit as st
import ollama
import time

# Funzione per restituire i dati gradualmente (simulando uno streaming di dati)
def stream_data(text):
    delay = 0.1  # Imposta un ritardo per il flusso dei dati
    for word in text.split():
        yield word + " "
        time.sleep(delay)

# Crea una tabella a 3 colonne senza contorni per centrare il logo
col1, col2, col3 = st.columns([1, 2, 1])  # Il logo sarà nella colonna centrale (col2)

with col2:
    # Carica il logo centrato
    logo_path = "logo.png"
    st.image(logo_path, width=350)

# Aggiungi i pulsanti con stile CSS personalizzato
st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .finance-button, .analyze-button, .law-button {
        padding: 20px 40px;
        font-size: 24px;
        font-weight: bold;
        color: white;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        width: 150px;
        height: 150px;
        text-align: center;
    }
    .finance-button {
        background-color: #FF930A;
    }
    .analyze-button {
        background-color: #F24B04;
    }
    .law-button {
        background-color: #BC00DD;
    }
    /* Riduci la distanza tra titolo e sottotitolo */
    .finance-button span, .analyze-button span, .law-button span {
        display: block;
        margin-top: -5px; /* Riduci la distanza tra titolo e sottotitolo */
        font-size: 12px;
        font-weight: normal;
    }
    </style>
""", unsafe_allow_html=True)

# Crea i pulsanti con il testo e i sottotitoli
st.markdown("""
    <div class="button-container">
        <button class="finance-button">Finance<br><span>Beat the market</span></button>
        <button class="analyze-button">Analyze<br><span>Study Countries</span></button>
        <button class="law-button">Law<br><span>Foreign Laws</span></button>
    </div>
""", unsafe_allow_html=True)

# Input per il prompt (istruzione)
instruction = st.chat_input("Chiedi a PAGE")

if instruction:
    # Visualizza l'input dell'utente
    with st.chat_message("user"):
        st.write(instruction)

    # Elaborazione del prompt
    with st.spinner("Thinking ..."):
        result = ollama.chat(model="francescomassa/page", messages=[{
            "role": "user",
            "input": "",  # Nessun input aggiuntivo
            "content": instruction,
        }])

    # Estrae la risposta e la mostra
    response = result["message"]["content"]  # 'content' è il campo che contiene la risposta
    st.write_stream(stream_data(response))  # Mostra la risposta del chatbot
