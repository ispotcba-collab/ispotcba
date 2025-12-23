import streamlit as st
import urllib.parse

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Tienda de iPhones", page_icon="??", layout="centered")

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

# NUEVA LISTA DE ALMACENAMIENTO AGREGADA
almacenamientos = ["128GB", "256GB", "512GB", "1TB"]

# --- INTERFAZ GRÁFICA ---
st.title("?? Venta de iPhones Exclusiva")
st.markdown("Selecciona tu modelo favorito y coordina el envío directamente por WhatsApp.")
st.divider()

# MODIFICACIÓN: AHORA HAY 3 COLUMNAS (Modelo, Color, Almacenamiento)
col1, col2, col3 = st.columns(3)

with col1:
    modelo_seleccionado = st.selectbox("Selecciona el Modelo:", modelos)

with col2:
    color_seleccionado = st.selectbox("Selecciona el Color:", colores)

with col3:
    # AQUÍ AGREGAMOS EL SELECTOR DE ALMACENAMIENTO
    almacenamiento_seleccionado = st.selectbox("Almacenamiento:", almacenamientos)

st.divider()

# Método de Pago
st.subheader("?? Forma de Pago")
metodo_pago = st.radio(
    "¿Cómo deseas abonar?",
    ["Contado (Efectivo)", "Transferencia Bancaria"]
)

# --- LÓGICA DE WHATSAPP ---
if st.button("?? CONFIRMAR PEDIDO Y COORDINAR ENVÍO", type="primary", use_container_width=True):
    if NUMERO_VENDEDOR == "PON_TU_NUMERO_AQUI":
        st.error("?? Error: El vendedor no ha configurado su número de teléfono en el código.")
    else:
        # AGREGAMOS EL ALMACENAMIENTO AL MENSAJE
        mensaje = (f"Hola! ?? Quiero comprar el *{modelo_seleccionado}*.\n"
                   f"?? Color: {color_seleccionado}\n"
                   f"?? Capacidad: {almacenamiento_seleccionado}\n"
                   f"?? Voy a abonar con: {metodo_pago}.\n"
                   f"?? Quisiera coordinar el envío.")
        
        # Codificar mensaje para URL
        mensaje_codificado = urllib.parse.quote(mensaje)
        
        # Crear link de WhatsApp
        link_whatsapp = f"https://wa.me/{NUMERO_VENDEDOR}?text={mensaje_codificado}"
        
        # Mostrar éxito y enlace
        st.success("¡Excelente elección! Haz clic abajo para finalizar en WhatsApp:")
        st.markdown(f'<a href="{link_whatsapp}" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: #25D366; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 5px; width: 100%;">?? Abrir WhatsApp</a>', unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("Los precios y disponibilidad se confirman por chat.")
