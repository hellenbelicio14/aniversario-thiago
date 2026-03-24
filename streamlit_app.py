import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Homenagem ao Thiago", page_icon="🇵🇹", layout="centered")

# Estilos (Cores de Portugal)
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    h1 { color: #006600; text-align: center; }
    .stButton>button { 
        background-color: #cc0000; color: white; border-radius: 15px; border: none; padding: 10px; font-weight: bold; width: 100%;
    }
    .typing { color: #006600; font-weight: bold; font-size: 1.2rem; text-align: center; }
</style>
""", unsafe_allow_html=True)

if 'etapa' not in st.session_state:
    st.session_state.etapa = 1

# --- PERGUNTA 1 ---
if st.session_state.etapa == 1:
    st.title("⚽ Responda e ganhe uma surpresa!")
    st.subheader("Para começar: você é o Thiago de Azevedo?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sim"):
            st.session_state.etapa = 2
            st.rerun()
    with col2:
        if st.button("Não"):
            st.warning("Ops! Botão errado... tenta o 'Sim'!")

# --- PERGUNTA 2 ---
elif st.session_state.etapa == 2:
    st.title("⚽ Quase lá...")
    st.subheader("Você é o professor de matemática mais foda da região?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Old que sim"):
            st.session_state.etapa = 3
            st.rerun()
    with col2:
        if st.button("Talvez"):
            st.error("❌ Errado! Tenta de novo.")
    st.info("💡 *Old que sim = Óbvio que sim!*")

# --- MENSAGEM ---
elif st.session_state.etapa == 3:
    st.title("⚽ O motivo disso tudo...")
    st.write("Estou a atualizar os meus conhecimentos em programação e também gosto de te ver sorrir. Juntei o útil ao agradável!")
    if st.button("Clique para prosseguir ➡️"):
        st.session_state.etapa = 4
        st.rerun()

# --- DIGITAÇÃO ---
elif st.session_state.etapa == 4:
    st.title("⚽ Uma mensagem especial...")
    msg = "Feliz aniversário, Thiaguete! Tudo de bom na tua vida. O aniversário é teu, mas o presente de te conhecer é meu! ❤️"
    placeholder = st.empty()
    full_res = ""
    for char in msg:
        full_res += char
        placeholder.markdown(f"<p class='typing'>{full_res}</p>", unsafe_allow_html=True)
        time.sleep(0.05)
    if st.button("Continuar ➡️"):
        st.session_state.etapa = 5
        st.rerun()

# --- QUEM VEIO? ---
elif st.session_state.etapa == 5:
    st.subheader("E olha quem veio dar-te os parabéns...")
    if st.button("QUEM??"):
        st.session_state.etapa = 6
        st.rerun()

# --- CR7 FINAL ---
elif st.session_state.etapa == 6:
    st.balloons()
    st.image("https://i.imgur.com/8Qp2N4b.png", use_container_width=True)
    st.markdown("<h1 style='color: #cc0000;'>Feliz aniversário, campeão!</h1>", unsafe_allow_html=True)
    if st.button("Recomeçar"):
        st.session_state.etapa = 1
        st.rerun()
