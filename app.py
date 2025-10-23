import streamlit as st
from PIL import Image

# 🌸 Configuración de la página
st.set_page_config(
    page_title="🌸 Introducción a Interfaces Multimodales",
    page_icon="🎨",
    layout="centered",
)

# 🌈 Estilo visual personalizado (más contraste y legibilidad)
page_style = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #f9f9ff 0%, #eaf2ff 100%);
    color: #1e2a44; /* azul oscuro para texto principal */
    font-family: 'Poppins', sans-serif;
}

/* Encabezados */
h1, h2, h3, h4, h5, h6 {
    text-align: center;
    color: #8b004f; /* rosado oscuro */
}

/* Botones */
.stButton>button {
    background-color: #ffd3e8; /* rosado pastel */
    color: #3a0055; /* texto oscuro */
    border-radius: 10px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #ffb6d9;
    transform: scale(1.05);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #f5ecff;
    color: #2a1d5c;
}

/* Cajas de texto, info y éxito */
.stSuccess, .stInfo, .stWarning, .stTextInput, .stSelectbox {
    color: #1e2a44 !important;
}

p, li {
    color: #1e2a44;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# 🌟 Título principal
st.title("🎨 Bienvenido a mi primera aplicación interactiva")

st.header("Explorando Interfaces Multimodales")
st.write("💡 Este es mi primer acercamiento al desarrollo de aplicaciones donde se combinan **diferentes modalidades de interacción** (visual, auditiva y táctil).")
st.write("Aquí podrás probar componentes básicos de **Streamlit**, que luego se expandirán en mis futuros proyectos.")

# 🖼️ Imagen principal
image = Image.open('cinna.jpeg')
st.image(image, caption='Experimentando con modalidades sensoriales 🎧👁️🤚')

# 🗣️ Entrada de texto
texto = st.text_input("✏️ Escribe una frase o palabra que te inspire", "Diseñar es pensar con los sentidos")
st.success(f"🪷 Has escrito: **{texto}**")

# 🧩 Columnas interactivas
st.subheader("Comparando modalidades")

col1, col2 = st.columns(2)

with col1:
    st.write("### 🌟 Columna A")
    st.info("Las **interfaces multimodales** integran varios sentidos para mejorar la experiencia de usuario.")
    acuerdo = st.checkbox("¿Estás de acuerdo?")
    if acuerdo:
        st.success("✅ ¡Totalmente cierto!")

with col2:
    st.write("### 🌟 Columna B")
    modalidad = st.radio("Selecciona la modalidad más importante para ti:", ("Visual", "Auditiva", "Táctil"))
    st.write(f"✨ Elegiste: **{modalidad}** como tu modalidad principal")

# 🖲️ Botón de acción
st.subheader("Probar botón interactivo")
if st.button("Haz clic aquí 💫"):
    st.balloons()
    st.write("🎉 ¡Gracias por participar en mi primera app!")
else:
    st.write("👆 Presiona el botón para activar una animación 🎈")

# 🔘 Selectbox dinámico
st.subheader("Simulación de acción multimodal")
mod = st.selectbox("Selecciona una modalidad para activar:", ("Audio", "Visual", "Háptico"))
if mod == "Audio":
    accion = "🔊 Reproduciendo sonido..."
elif mod == "Visual":
    accion = "🎞️ Mostrando video..."
else:
    accion = "🤚 Activando vibración..."
st.write(f"➡️ Acción seleccionada: {accion}")

# 🎛️ Sidebar interactivo
with st.sidebar:
    st.header("⚙️ Panel de configuración")
    st.write("Ajusta la modalidad activa:")
    opcion = st.radio("Modo preferido:", ("Visual", "Auditiva", "Háptica"))
    st.write(f"🔧 Modo seleccionado: **{opcion}**")
