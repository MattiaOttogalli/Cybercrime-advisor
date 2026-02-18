import streamlit as st

# Configurazione della pagina

st.set_page_config(page_title="Cybercrime Advisor", page_icon="⚖️")

# Titolo dell'applicazione
st.title("⚖️ Cybercrime Advisor")
st.markdown("---")

# 1. Selezione della Categoria Principale

categoria = st.selectbox(
    "Seleziona la Categoria:",
    options=[
        'Selezione', 
        'Accesso abusivo', 
        'Danneggiamento', 
        'Crimine commesso con IA (AI Act 2026)', 
        'Truffa', 
        'Ricilaggio', 
        'Falsità in un documento informatico'
    ]
)

# 2. Logica per la Sottocategoria (Menu dinamico)

sottocategoria_options = {"Scegli la prima categoria": None}
disabled_sub = True

if categoria == 'Danneggiamento':
    sottocategoria_options = {
        'Seleziona tipo di danno': None,
        'Danneggiamento di dati e programmi (Art. 635-bis)': '635-bis',
        'Danneggiamento di sistemi informatici (Art. 635-quater)': '635-quater',
        'Danneggiamento di sistemi di Pubblica Utilità (Art. 635-ter)': '635-ter'
    }
    disabled_sub = False

elif categoria == 'Accesso abusivo':
    sottocategoria_options = {
        'Seleziona circostanza': None,
        'Accesso abusivo standard (Art. 615-ter)': '615-ter',
        'Accesso abusivo da parte di Pubblico Ufficiale (Aggravante)': '615-aggravato'
    }
    disabled_sub = False

elif categoria == 'Crimine commesso con IA (AI Act 2026)':
    sottocategoria_options = {
        'Seleziona utilizzo IA': None,
        'IA come mezzo insidioso (L. 132/2025)': 'AI-insidioso'
    }
    disabled_sub = False

elif categoria == 'Truffa':
    sottocategoria_options = {
        'Seleziona il tipo di truffa': None,
        'Truffa (Art. 640)': '640',
        'Truffa aggravata per il conseguimento di erogazioni pubbliche (Art. 640-bis)': '640-bis',
        'Frode informatica (Art. 640-ter)': '640-ter'
    }
    disabled_sub = False

elif categoria == 'Ricilaggio':
    sottocategoria_options = {
        'Riciclaggio (Art. 648-bis)': '648-bis',
        'Autoriciclaggio (Art. 648-ter)': '648-ter'
    }
    disabled_sub = False

elif categoria == 'Falsità in un documento informatico':
    sottocategoria_options = {'Falsità in un documento (Art. 491-bis)': '491-bis'}
    disabled_sub = False

# Rendering del secondo menu
specifico_label = st.selectbox("Specifico:", options=list(sottocategoria_options.keys()), disabled=disabled_sub)
scelto = sottocategoria_options[specifico_label]

st.divider()

# 3. Visualizzazione Risultati

if scelto:
    if scelto == '615-ter':
        st.error("### Fattispecie: Accesso abusivo ad un sistema informatico protetto")
        st.warning("**Pena:** Reclusione fino a 3 anni")
        st.info("**Nota:** Il reato è commesso nel momento in cui si entra in un sistema informatico senza il consenso del proprietario")

    elif scelto == '615-aggravato':
        st.error("### Fattispecie: Accesso abusivo ad un sistema informatico protetto da parte di pubblico ufficiale")
        st.warning("**Nota:** Rappresenta un'aggravante specifica per il reato di accesso abusivo.")

    elif scelto == '635-bis':
        st.error("### Fattispecie: Danneggiamento di dati, informazioni o programmi informatici")
        st.warning("**Pena:** Reclusione da 2 a 6 anni")
        st.info("**Nota:** Il reato sussiste anche se i dati sono recuperabili.")

    elif scelto == 'AI-insidioso':
        st.error("### Fattispecie: Reato commesso tramite l'uso di un'intelligenza artificiale")
        st.warning("**Aggravante:** Art. 61 n. 11-undecies")
        st.info("**Esempio:** Cancellare dati utilizzando un malware creato da un IA.")

    elif scelto == '635-quater':
        st.error("### Fattispecie: Danneggiamento di sistemi informatici o telematici")
        st.warning("**Pena:** Reclusione da 2-6 a 3-8 anni")

    elif scelto == '635-ter':
        st.error("### Fattispecie: Danneggiamento di informazioni, dati e programmi pubblici")
        st.warning("**Pena:** Reclusione da 2-6 a 3-8 anni")

    elif scelto == '640':
        st.error("### Fattispecie: Truffa")
        st.warning("**Pena:** Reclusione da 0.5-3 a 1-5 anni con multa")

    elif scelto == '640-bis':
        st.error("### Fattispecie: Truffa aggravata per erogazioni pubbliche")
        st.info("Costituisce un'aggravante del reato di truffa.")

    elif scelto == '640-ter':
        st.error("### Fattispecie: Frode informatica")
        st.warning("**Pena:** Pene del 640 con aggravanti fino a 2-6 anni e multa.")

    elif scelto == '648-bis':
        st.error("### Fattispecie: Riciclaggio di beni")
        st.warning("**Pena:** Reclusione da 4 a 12 anni e multa pesante.")

    elif scelto == '648-ter':
        st.error("### Fattispecie: Autoriciclaggio di beni")
        st.warning("**Pena:** Reclusione da 2 a 8 anni e multa.")

    elif scelto == '491-bis':
        st.error("### Fattispecie: Falsità in un documento informatico")
        st.info("Pena equiparata a quella prevista per i documenti cartacei.")
else:
    st.info("Scegli una categoria e specifica il caso per visualizzare l'analisi")