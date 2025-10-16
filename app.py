import streamlit as st
import pandas as pd

st.set_page_config(page_title="Elecciones Generales Perú 2026", layout="wide")

st.title("🗳️ Elecciones Generales Perú 2026")
st.markdown("""
Estas elecciones definirán al próximo presidente, vicepresidentes, parlamentarios y representantes al Parlamento Andino.

---

### 📅 Fecha de elecciones
- **Primera vuelta:** Domingo **12 de abril de 2026**
- **Segunda vuelta (si aplica):** Domingo **7 de junio de 2026**

---

### 🧾 Autoridades a elegir
- Presidente de la República y dos vicepresidentes
- 130 Diputados (nueva cámara baja)
- 60 Senadores (nueva cámara alta)
- 5 Representantes al Parlamento Andino

---

### 🏛️ Convocatoria Legal
- Decreto Supremo **N.º 039-2025-PCM**
- Convocatoria oficial realizada el 12 de abril de 2025

---

### 🗳️ Proceso Electoral
- Se realizarán elecciones **primarias internas** en noviembre y diciembre de 2025
- Se utilizará el nuevo **Mapa de Alertas de Conflictos Electorales (MACE)** con apoyo internacional

---

### 👥 Padrón Electoral
- Aproximadamente **27 millones** de peruanos habilitados para votar
- **Lima** cuenta con más de **719,000** nuevos votantes (jóvenes)

---
""")

st.subheader("📌 Fechas clave del proceso electoral")
cronograma = pd.DataFrame({
    "Evento": [
        "Cierre del padrón electoral / Actualización de DNI",
        "Elecciones primarias internas",
        "Inscripción de listas y candidatos",
        "Presentación de objeciones a candidaturas",
        "Fecha máxima de inscripción oficial",
        "Primera vuelta electoral",
        "Segunda vuelta (si aplica)"
    ],
    "Fecha": [
        "12 de abril de 2025",
        "30 de noviembre y 7 de diciembre de 2025",
        "Hasta el 23 de diciembre de 2025",
        "13 de marzo de 2026",
        "14 de marzo de 2026",
        "12 de abril de 2026",
        "7 de junio de 2026"
    ]
})

st.table(cronograma)

st.markdown("""
---

### 🧑‍🤝‍🧑 Partidos y Candidatos
- **41 partidos políticos** con inscripción válida
- Se esperan **más de 40 candidatos presidenciales**
- Algunos partidos siguen en proceso de inscripción

---

### 🔗 Fuentes Oficiales
- [ONPE – Elecciones 2026](https://eg2026.onpe.gob.pe)
- [JNE – Jurado Nacional de Elecciones](https://www.jne.gob.pe)
- [Andina Noticias](https://andina.pe)
- [TV Perú](https://www.tvperu.gob.pe/noticias)
""")
