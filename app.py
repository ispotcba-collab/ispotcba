import streamlit as st
import urllib.parse

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Tienda de iPhones", page_icon="📱", layout="centered")

# --- VARIABLES ---
NUMERO_VENDEDOR = "5493517669886"

# --- DATOS DE LOS MODELOS ---
modelos = [
    "iPhone 13", "iPhone 13 Pro", "iPhone 13 Pro Max",
    "iPhone 14", "iPhone 14 Pro", "iPhone 14 Pro Max",
    "iPhone 15", "iPhone 15 Pro", "iPhone 15 Pro Max",
    "iPhone 16", "iPhone 16 Pro", "iPhone 16 Pro Max",
    "iPhone 17", "iPhone 17 Pro", "iPhone 17 Pro Max"
]

colores = [
    "Negro Espacial", "Plata", "Oro", "Titanio Natural", 
    "Titanio Azul", "Azul Sierra", "Verde Alpino", "Rosa", "Rojo (Product RED)"
]

almacenamientos = ["128GB", "256GB", "512GB", "1TB"]

# --- INTERFAZ GRÁFICA ---
st.title("📱 Venta de iPhones Exclusiva")
st.markdown("Selecciona tu modelo favorito y coordina el envío directamente por WhatsApp.")
st.divider()

# --- SELECTORES (3 COLUMNAS) ---
col1, col2, col3 = st.columns(3)

with col1:
    modelo_seleccionado = st.selectbox("📱 Modelo:", modelos)

with col2:
    color_seleccionado = st.selectbox("🎨 Color:", colores)

with col3:
    almacenamiento_seleccionado = st.selectbox("💾 Memoria:", almacenamientos)

st.divider()

# --- MÉTODO DE PAGO ---
st.subheader("💳 Forma de Pago")
metodo_pago = st.radio(
    "¿Cómo deseas abonar?",
    ["Contado (Efectivo)", "Transferencia Bancaria"],
    horizontal=True # Esto hace que las opciones se vean una al lado de la otra
)

st.divider()

# --- BOTÓN Y LÓGICA DE WHATSAPP ---
# Usamos un contenedor para centrar visualmente la acción
with st.container():
    if st.button("🛒 CONFIRMAR PEDIDO Y COORDINAR ENVÍO", type="primary", use_container_width=True):
        
        # Crear el mensaje limpio
        mensaje = (f"Hola! 👋 Quiero comprar el *{modelo_seleccionado}*.\n"
                   f"🎨 Color: {color_seleccionado}\n"
                   f"💾 Capacidad: {almacenamiento_seleccionado}\n"
                   f"💸 Voy a abonar con: {metodo_pago}.\n"
                   f"📍 Quisiera coordinar el envío.")
        
        # Codificar mensaje para URL (transforma espacios en %20, etc.)
        mensaje_codificado = urllib.parse.quote(mensaje)
        
        # Crear link de WhatsApp
        link_whatsapp = f"https://wa.me/{NUMERO_VENDEDOR}?text={mensaje_codificado}"
        
        # Mostrar mensaje de éxito y botón verde
        st.success("¡Excelente elección! Haz clic abajo para finalizar en WhatsApp:")
        
        # Botón HTML personalizado para abrir WhatsApp
        st.markdown(f'''
            <a href="{link_whatsapp}" target="_blank" style="
                display: inline-block; 
                padding: 15px 25px; 
                background-color: #25D366; 
                color: white; 
                text-align: center; 
                text-decoration: none; 
                font-size: 18px; 
                font-weight: bold;
                border-radius: 10px; 
                width: 100%;
                box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
                transition: transform 0.2s;
            ">
                📲 Abrir WhatsApp Ahora
            </a>
            ''', unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("🔒 Compra segura. Los precios y disponibilidad final se confirman por chat.")


