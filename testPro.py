# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gestor de Tareas", layout="wide")
st.title("📋 Gestor de Tareas con Gantt")

# --- Panel lateral para añadir tareas ---
st.sidebar.header("Nueva Tarea")
name = st.sidebar.text_input("Nombre")
start = st.sidebar.date_input("Fecha de inicio")
end = st.sidebar.date_input("Fecha de fin")
if st.sidebar.button("Añadir tarea"):
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
    st.session_state.tasks.append({
        "Tarea": name,
        "Inicio": pd.to_datetime(start),
        "Fin": pd.to_datetime(end)
    })
    st.sidebar.success(f"Tarea «{name}» añadida")

# --- DataFrame de tareas ---
if "tasks" in st.session_state and st.session_state.tasks:
    df = pd.DataFrame(st.session_state.tasks)
else:
    # Tareas de ejemplo
    df = pd.DataFrame([
        {"Tarea": "Tarea A", "Inicio": "2025-05-01", "Fin": "2025-05-03"},
        {"Tarea": "Tarea B", "Inicio": "2025-05-02", "Fin": "2025-05-06"},
        {"Tarea": "Tarea C", "Inicio": "2025-05-04", "Fin": "2025-05-07"},
    ])
    df["Inicio"] = pd.to_datetime(df["Inicio"])
    df["Fin"] = pd.to_datetime(df["Fin"])

st.subheader("Lista de tareas")
st.dataframe(df)

# --- Gráfico Gantt ---
st.subheader("Diagrama de Gantt")
fig = px.timeline(
    df,
    x_start="Inicio",
    x_end="Fin",
    y="Tarea",
    color="Tarea",
    title="Cronograma de tareas"
)
fig.update_yaxes(autorange="reversed")  # para que la primera tarea quede arriba
st.plotly_chart(fig, use_container_width=True)
