import streamlit as st
import openai

# Obtener API key de OpenAI y conectarse a la API
openai.api_key = "your_api_key_here"

# Definir plantilla de texto para generar el plan personalizado
template = "Hola {nombre}, según tu edad ({edad}) y tu género ({genero}), te recomendamos los siguientes hábitos para llevar una vida más saludable:\n\n- Ejercicio: Realiza {ejercicio} minutos de ejercicio {dias_ejercicio} veces por semana.\n\n- Alimentación: Incluye en tu dieta {alimentos} para una nutrición balanceada.\n\n- Descanso: Asegúrate de dormir al menos {horas_sueno} horas por noche.\n\n- Meditación: Dedica {minutos_meditacion} minutos al día para meditar y reducir el estrés.\n\n¡Disfruta de una vida saludable!"

# Crear función para generar el plan personalizado utilizando GPT-3
def generar_plan(nombre, edad, genero, ejercicio, dias_ejercicio, alimentos, horas_sueno, minutos_meditacion):
    # Llenar la plantilla de texto con los datos del usuario utilizando GPT-3
    plan_generado = openai.Completion.create(
        engine="davinci", 
        prompt=template.format(nombre=nombre, edad=edad, genero=genero, ejercicio=ejercicio, dias_ejercicio=dias_ejercicio, alimentos=alimentos, horas_sueno=horas_sueno, minutos_meditacion=minutos_meditacion),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Devolver el plan generado por GPT-3
    return plan_generado.choices[0].text

# Crear la interfaz de usuario utilizando Streamlit
st.title("Generador de planes de vida saludable personalizados")
nombre = st.text_input("Ingresa tu nombre:")
edad = st.number_input("Ingresa tu edad:", min_value=1, max_value=120, value=30)
genero = st.selectbox("Selecciona tu género:", ("Masculino", "Femenino"))
ejercicio = st.slider("¿Cuántos minutos de ejercicio quieres realizar por día?", min_value=0, max_value=120, value=30, step=5)
dias_ejercicio = st.slider("¿Cuántos días a la semana quieres hacer ejercicio?", min_value=0, max_value=7, value=3, step=1)
alimentos = st.text_input("Ingresa los alimentos que quieres incluir en tu dieta:")
horas_sueno = st.slider("¿Cuántas horas de sueño quieres dormir por noche?", min_value=0, max_value=24, value=7, step=1)
minutos_meditacion = st.slider("¿Cuántos minutos quieres dedicar a la meditación diaria?", min_value=0, max_value=60, value=10, step=5)

if st.button("Generar plan"):
    # Generar el plan personalizado utilizando la función definida anteriormente
    plan = generar_plan(nombre, edad, genero, ejercicio, dias_ejercicio, alimentos, horas_sueno, minutos_meditacion)
# Mostrar el plan generado en la aplicación de Streamlit
st.write(plan)
