import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="Cybercrime Help Desk", page_icon="🚨", layout="wide")

# Database esteso con i dati del file Cybercrime_advisor.ipynb
database_reati = {
    '615-ter': {
        'titolo': "Accesso abusivo ad un sistema informatico protetto",
        'identikit': "Qualcuno è entrato nel tuo account, PC o smartphone senza autorizzazione.",
        'soluzione': [
            "Cambia immediatamente la password da un dispositivo diverso.",
            "Attiva l'autenticazione a due fattori (2FA).",
            "Controlla i 'dispositivi connessi' nelle impostazioni dell'account e disconnetti quelli sospetti."
        ],
        'denuncia': "Art. 615-ter c.p.. Salva i log di accesso e le email di avviso di 'nuovo accesso'. Recati alla Polizia Postale.",
        'prevenzione': "Non usare la stessa password per più servizi e non comunicare mai codici OTP a terzi."
    },
    '615-aggravato': {
        'titolo': "Accesso abusivo da parte di Pubblico Ufficiale",
        'identikit': "Accesso illecito compiuto da un soggetto con poteri pubblici o incaricato di pubblico servizio.",
        'soluzione': ["Richiedi un audit interno se l'accesso è avvenuto in ambito lavorativo/istituzionale."],
        'denuncia': "Fattispecie aggravata dell'Art. 615-ter. Necessaria segnalazione formale all'ente di appartenenza e querela.",
        'prevenzione': "Monitoraggio rigoroso degli accessi ai database sensibili tramite log inalterabili."
    },
    '635-bis': {
        'titolo': "Danneggiamento di dati e programmi",
        'identikit': "I tuoi file sono stati cancellati, alterati o resi inutilizzabili (es. Ransomware).",
        'soluzione': [
            "Scollega il disco per evitare ulteriori sovrascritture.",
            "Tenta il ripristino da un backup precedente.",
            "Non pagare riscatti: contatta un esperto di data recovery."
        ],
        'denuncia': "Art. 635-bis c.p.. Il reato sussiste anche se i dati sono recuperabili. Fornisci i file log del sistema.",
        'prevenzione': "Mantieni backup regolari 'offline' (non collegati permanentemente al PC)."
    },
    '635-ter': {
        'titolo': "Danneggiamento di sistemi di Pubblica Utilità",
        'identikit': "Attacco che colpisce infrastrutture critiche (sanità, energia, trasporti).",
        'soluzione': ["Attivazione immediata del piano di Business Continuity e Disaster Recovery."],
        'denuncia': "Art. 635-ter c.p.. Reato di estrema gravità. Segnalazione obbligatoria al CNAIPIC.",
        'prevenzione': "Segregazione delle reti industriali (OT) da quelle amministrative (IT)."
    },
    '635-quater': {
        'titolo': "Danneggiamento di sistemi informatici",
        'identikit': "Interruzione o grave rallentamento del funzionamento di un intero sistema o rete.",
        'soluzione': ["Analisi del traffico di rete per identificare attacchi DoS/DDoS."],
        'denuncia': "Art. 635-quater c.p.. Raccogli prove del blocco del servizio (screenshot di errori, log server).",
        'prevenzione': "Uso di sistemi anti-DDoS e firewall di nuova generazione."
    },
    '640': {
        'titolo': "Truffa",
        'identikit': "Sei stato raggirato online per fornire beni o denaro (es. finto annuncio di vendita).",
        'soluzione': ["Interrompi ogni contatto con il soggetto. Non inviare altro denaro."],
        'denuncia': "Art. 640 c.p.. Conserva chat, numeri di telefono e ricevute di pagamento.",
        'prevenzione': "Diffida di offerte troppo vantaggiose e verifica l'attendibilità dei venditori."
    },
    '640-bis': {
        'titolo': "Truffa per erogazioni pubbliche",
        'identikit': "Uso di raggiri per ottenere indebitamente finanziamenti o bonus dallo Stato.",
        'soluzione': ["Autodenuncia o rettifica immediata presso l'ente erogatore per limitare le conseguenze penali."],
        'denuncia': "Aggravante dell'Art. 640. Spesso rilevata d'ufficio dalla Guardia di Finanza.",
        'prevenzione': "Verifica scrupolosa dei requisiti prima di inoltrare istanze telematiche."
    },
    '640-ter': {
        'titolo': "Frode informatica",
        'identikit': "Manipolazione del sistema per sottrarre denaro (es. bonifico partito a tua insaputa).",
        'soluzione': [
            "Blocca immediatamente carte e conti correnti tramite numero verde bancario.",
            "Disconosci le operazioni fraudolente.",
            "Controlla il PC alla ricerca di 'Keylogger' o malware bancari."
        ],
        'denuncia': "Art. 640-ter c.p.. Allega l'estratto conto e la lista dei dispositivi autorizzati dall'app bancaria.",
        'prevenzione': "Non cliccare su link in SMS/Email (Smishing/Phishing) e usa app bancarie con biometria."
    },
    '648-bis/ter': {
        'titolo': "Riciclaggio e Autoriciclaggio",
        'identikit': "Utilizzo di denaro proveniente da reati informatici per altre attività economiche.",
        'soluzione': ["Blocco dei flussi sospetti e segnalazione al Responsabile Antiriciclaggio."],
        'denuncia': "Art. 648-bis/ter c.p.. Sanzioni pesantissime che includono la confisca dei beni.",
        'prevenzione': "Procedure di KYC (Know Your Customer) rigorose e tracciamento dei pagamenti digitali."
    },
    '491-bis': {
        'titolo': "Falsità in un documento informatico",
        'identikit': "Firma digitale rubata o creazione di documenti informatici falsi con valore legale.",
        'soluzione': ["Revoca immediata del certificato di firma digitale presso il certificatore (es. Aruba, InfoCert)."],
        'denuncia': "Art. 491-bis c.p.. Le pene sono equiparate al falso in atto pubblico cartaceo.",
        'prevenzione': "Proteggi il token/smart card di firma con PIN complessi e non lasciarli mai incustoditi."
    },
    'AI-insidioso': {
        'titolo': "Reato commesso tramite IA",
        'identikit': "Uso di Deepfake, malware generati da IA o bot per compiere illeciti.",
        'soluzione': ["Uso di software di rilevamento 'Synthetic Media' per provare la falsità del contenuto."],
        'denuncia': "Aggravante specifica (Art. 61 n. 11-undecies) e normativa AI Act 2026.",
        'prevenzione': "Formazione del personale sul riconoscimento di audio/video generati da IA (Social Engineering)."
    }
}

# --- INTERFACCIA STREAMLIT ---
st.title("🚨 Cybercrime Incident Response Advisor")
st.markdown("Basato sul Codice Penale e sulle direttive di sicurezza informatica 2026.")

# Mappatura colloquiale per l'utente
problema_input = st.selectbox(
    "Quale problema hai riscontrato?",
    ["Seleziona...", 
     "Accesso non autorizzato ai miei account/dispositivi",
     "I miei dati/file sono stati cancellati o criptati",
     "Attacco a un sistema di pubblica utilità o infrastruttura",
     "Blocco o rallentamento della rete aziendale",
     "Truffa subita durante un acquisto online",
     "Furto di denaro tramite manipolazione bancaria/informatica",
     "Manipolazione di documenti informatici o firme digitali",
     "Uso illecito di denaro di dubbia provenienza",
     "Contenuto falso generato da Intelligenza Artificiale (Deepfake)"]
)

# Logica di associazione
mapping = {
    "Accesso non autorizzato ai miei account/dispositivi": "615-ter",
    "I miei dati/file sono stati cancellati o criptati": "635-bis",
    "Attacco a un sistema di pubblica utilità o infrastruttura": "635-ter",
    "Blocco o rallentamento della rete aziendale": "635-quater",
    "Truffa subita durante un acquisto online": "640",
    "Furto di denaro tramite manipolazione bancaria/informatica": "640-ter",
    "Manipolazione di documenti informatici o firme digitali": "491-bis",
    "Uso illecito di denaro di dubbia provenienza": "648-bis/ter",
    "Contenuto falso generato da Intelligenza Artificiale (Deepfake)": "AI-insidioso"
}

codice_scelto = mapping.get(problema_input)

if codice_scelto:
    dati = database_reati[codice_scelto]
    st.divider()
    
    st.error(f"### Reato Riconosciuto: {dati['titolo']}")
    st.write(f"**Identikit del caso:** {dati['identikit']}")
    
    t1, t2, t3 = st.tabs(["🛠️ Soluzione Tecnica", "👮 Procedura Legale", "🛡️ Prevenzione"])
    
    with t1:
        for s in dati['soluzione']:
            st.write(f"- {s}")
            
    with t2:
        st.info(dati['denuncia'])
        if st.button("Copia Bozza Denuncia"):
            st.code(f"Oggetto: Denuncia per {dati['titolo']}\nIl sottoscritto espone che...")
            
    with t3:
        st.success(dati['prevenzione'])
else:
    st.info("Benvenuto. Scegli un'opzione per analizzare il caso e ricevere istruzioni.")
