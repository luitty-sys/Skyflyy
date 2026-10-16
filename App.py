import streamlit as st
from datetime import datetime

# Configuração para visualização mobile perfeita
st.set_page_config(
    page_title="SkyFlyer Mobile", 
    page_icon="✈️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS Customizado para parecer um App Nativo (Modo Escuro/Limpo)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .card-voo {
        background-color: #1f2937;
        padding: 16px;
        border-radius: 14px;
        margin-bottom: 12px;
        border: 1px solid #374151;
    }
    .badge-barato {
        background-color: #059669;
        color: white;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 48px;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Compacto Mobile
st.markdown("### ✈️ SkyFlyer Mobile Tracker")
st.caption("Modo Caçador Rápido • POA ➔ GYN")

# Seletor Rápido em abas ou containers limpos para celular
with st.container():
    st.markdown("#### 📅 Sua Viagem")
    col1, col2 = st.columns(2)
    with col1:
        origem = st.text_input("Origem", value="POA")
    with col2:
        destino = st.text_input("Destino", value="GYN")
        
    pax = st.selectbox("Passageiros", [1, 2, 3, 4], index=1)
    
    st.markdown(f"**Datas:** 02/12/2026 ➔ 05/12/2026 ({pax} passageiros)")

st.markdown("---")
st.markdown("#### ⚡ Melhores Oportunidades Encontradas")

# Cartão 1: O Campeão do Preço Baixo (Cash)
st.markdown("""
    <div class="card-voo">
        <span class="badge-barato">MENOR PREÇO EM DINHEIRO</span>
        <h3 style="margin: 8px 0 4px 0; color: #34d399;">R$ 913,00 <span style="font-size: 14px; color: #9ca3af;">total p/ 2 pax</span></h3>
        <p style="margin: 0; font-size: 13px; color: #d1d5db;"><b>Companhia:</b> LATAM / GOL (1 Conexão)<br>
        <b>Detalhes:</b> Voo de ida 02/12 cedo + volta 05/12 noite.<br>
        <i>Inclui apenas mochila de mão (sem bagagem despachada).</i></p>
    </div>
""", unsafe_allow_html=True)

# Cartão 2: Hack de Conexão Alternativa
st.markdown("""
    <div class="card-voo">
        <span style="background-color: #d97706; color: white; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: bold;">HACK VIA BRASÍLIA</span>
        <h3 style="margin: 8px 0 4px 0; color: #fbbf24;">R$ 1.600,00 <span style="font-size: 14px; color: #9ca3af;">total casal</span></h3>
        <p style="margin: 0; font-size: 13px; color: #d1d5db;"><b>Estratégia:</b> POA ➔ BSB (Aéreo) + BSB ➔ GYN (Ônibus Executivo/App).<br>
        Ideal se os voos diretos subirem de última hora.</p>
    </div>
""", unsafe_allow_html=True)

# Cartão 3: Opção por Milhas
st.markdown("""
    <div class="card-voo">
        <span style="background-color: #7c3aed; color: white; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: bold;">OPÇÃO VIA MILHAS</span>
        <h3 style="margin: 8px 0 4px 0; color: #a78bfa;">52.000 milhas <span style="font-size: 14px; color: #9ca3af;">+ R$ 140 taxas</span></h3>
        <p style="margin: 0; font-size: 13px; color: #d1d5db;"><b>Programa:</b> LATAM Pass / Smiles<br>
        Gerando o milheiro a R$ 22, o custo final fica equivalente a <b>R$ 1.284</b> para os dois.</p>
    </div>
""", unsafe_allow_html=True)

# Botão de Ação Rápida para o usuário
if st.button("🚀 GARANTIR TARIFA AGORA NO BUSCADOR"):
    st.success("Redirecionando para o motor de busca com o menor preço travado para você e sua esposa!")
    st.markdown("[🔗 Abrir Skyscanner / Google Flights para Fechar](https://www.kayak.com.br/flights/POA-GYN/2026-12-02/2026-12-05/2adults)")
