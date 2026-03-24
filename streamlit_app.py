import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Homenagem ao Thiago", page_icon="🇵🇹", layout="centered")

# Estilos (Cores de Portugal)
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .titulo { color: #006600; text-align: center; font-size: 2rem; font-weight: bold; margin-bottom: 20px; }
    .pergunta { color: #333; text-align: center; font-size: 1.5rem; margin-bottom: 30px; }
    .stButton>button { 
        background-color: #cc0000; color: white; border-radius: 15px; border: none; 
        padding: 15px; font-weight: bold; width: 100%; font-size: 1.1rem;
    }
    .stButton>button:hover { background-color: #990000; }
    .typing { color: #006600; font-weight: bold; font-size: 1.2rem; text-align: center; padding: 20px; }
</style>
""", unsafe_allow_html=True)

# Inicializa o estado se não existir
if 'passo' not in st.session_state:
    st.session_state.passo = 1

# --- ETAPA 1: THIAGO ---
if st.session_state.passo == 1:
    st.markdown("<div class='titulo'>⚽ Desafio de Aniversário!</div>", unsafe_allow_html=True)
    st.markdown("<div class='pergunta'>1. Para começarmos, você é o Thiago de Azevedo mesmo?</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sim, sou eu!"):
            st.session_state.passo = 2
            st.rerun()
    with col2:
        if st.button("Não..."):
            st.warning("Botão com defeito! Tente o outro.")

# --- ETAPA 2: PROFESSOR ---
elif st.session_state.passo == 2:
    st.markdown("<div class='titulo'>⚽ Quase lá...</div>", unsafe_allow_html=True)
    st.markdown("<div class='pergunta'>2. Você é o professor de matemática mais foda da região?</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Old que sim"):
            st.session_state.passo = 3
            st.rerun()
    with col2:
        if st.button("Talvez?"):
            st.error("Resposta errada! Tente de novo.")
    st.info("💡 *Old que sim = Óbvio que sim!*")

# --- ETAPA 3: O MOTIVO ---
elif st.session_state.passo == 3:
    st.markdown("<div class='titulo'>⚽ O motivo disso tudo...</div>", unsafe_allow_html=True)
    st.write("Estou atualizando meus conhecimentos em programação e também gosto de te ver sorrir. Juntei o útil ao agradável!")
    if st.button("Clique para continuar ➡️"):
        st.session_state.passo = 4
        st.rerun()

# --- ETAPA 4: MENSAGEM ---
elif st.session_state.passo == 4:
    st.markdown("<div class='titulo'>⚽ Uma mensagem para você</div>", unsafe_allow_html=True)
    placeholder = st.empty()
    msg = "Feliz aniversário, Thiaguete! Tudo de bom na sua vida. O aniversário é seu, mas o presente de te conhecer é meu! ❤️"
    
    # Efeito de digitação
    res = ""
    for char in msg:
        res += char
        placeholder.markdown(f"<div class='typing'>{res}</div>", unsafe_allow_html=True)
        time.sleep(0.04)
    
    if st.button("Continuar para a surpresa final ➡️"):
        st.session_state.passo = 5
        st.rerun()

# --- ETAPA 5: QUEM VEIO? ---
elif st.session_state.passo == 5:
    st.markdown("<div class='titulo'>⚽ Espera aí!</div>", unsafe_allow_html=True)
    st.markdown("<div class='pergunta'>Olha quem veio te dar parabéns...</div>", unsafe_allow_html=True)
    if st.button("QUEM??"):
        st.session_state.passo = 6
        st.rerun()

# --- ETAPA 6: CR7 ---
elif st.session_state.passo == 6:
    st.balloons()
    st.image("https://i.imgur.com/8Qp2N4b.png", use_container_width=True)
    st.markdown("<h1 style='color: #cc0000; text-align: center;'>Feliz aniversário, campeão!</h1>", unsafe_allow_html=True)
    if st.button("Ver de novo 🔄"):
        st.session_state.passo = 1
        st.rerun()
