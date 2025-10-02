# pip install folium

import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components

# -----------------------
# CONFIGURACIÓN DEL DASHBOARD
# -----------------------
st.set_page_config(
    page_title="Hospitals Access Peru",
    layout="wide"
)

# -----------------------
# FUNCIONES DE CARGA (placeholders)
# -----------------------
def load_hospitals():
    """Carga el dataset de hospitales filtrado (operativos)."""
    try:
        return pd.read_csv("bases/IPRESS.csv", encoding="latin-1")
    except Exception as e:
        st.error(f"Error cargando hospitales: {e}")
        return None

def load_centros_poblados():
    """Carga el dataset de centros poblados."""
    try:
        # Si está en CSV o shapefile, usar la función adecuada
        return pd.read_csv("bases/CCPP_0/CCPP_0.csv", encoding="latin-1")
    except Exception as e:
        st.warning(f"No se pudo cargar centros poblados: {e}")
        return None

def load_distritos():
    """Carga el límite distrital shapefile / GeoDataFrame."""
    try:
        return gpd.read_file("bases/Distritos/Distritos.shp")
    except Exception as e:
        st.warning(f"No se pudo cargar distritos: {e}")
        return None

# -----------------------
# CARGA DE DATOS
# -----------------------
hospitals = load_hospitals()
centros = load_centros_poblados()
distritos = load_distritos()

data_ok = (hospitals is not None) and (distritos is not None)

# -----------------------
# DEFINICIÓN DE TABS
# -----------------------
tab1, tab2, tab3 = st.tabs([
    "📊 Data Description",
    "🗺 Static Maps & Dept Analysis",
    "🌍 Dynamic Maps"
])

# -----------------------
# TAB 1: Data Description
# -----------------------
with tab1:
    st.header("📊 Data Description")
    st.markdown("""
    - Unidad de análisis: hospitales públicos operativos  
    - Fuentes: MINSA – IPRESS, centros poblados, límites distritales  
    - Filtrado: solo se consideran hospitales con coordenadas válidas  
    - Objetivo: el dashboard muestra mapas estáticos y dinámicos con información georreferenciada de hospitales en funcionamiento en el país
    """)
    if hospitals is not None:
        st.success(f"Hospitales cargados: {len(hospitals)}")
        st.dataframe(hospitals.head())
    else:
        st.warning("Datos de hospitales no disponibles aún.")

# -----------------------
# TAB 2: Mapas estáticos & análisis departamental
# -----------------------
with tab2:
    st.header("🗺 Static Maps & Department Analysis")

    if not data_ok:
        st.warning("⚠️ No hay datos suficientes para mostrar mapas estáticos.")
    else:
        # --- Parte 2: Static Maps (GeoPandas) ---
        st.subheader("Static Maps — Task 1")
        st.write("Aquí se insertan los mapas estáticos que tu compañera genere (hospitales por distrito, distritos vacíos, top-10).")
        # Ejemplo de placeholder:
        # fig = your_function_to_plot_map(...)
        # st.pyplot(fig)

        st.write("---")

        # --- Parte 2: Department-level analysis ---
        st.subheader("Department-level Analysis — Task 2")
        st.write("Aquí irá la tabla resumen por departamento, gráfico de barras, mapa coroplético departamental.")
        # placeholder de ejemplo:
        # df_dept = hospitals.groupby("DEPARTAMENTO")... 
        # st.dataframe(df_dept)
        # fig2 = your_function_to_plot_dept_map(...)
        # st.plotly_chart(fig2)  # o st.pyplot(fig2)

# -----------------------
# TAB 3: Mapas dinámicos (Folium)
# -----------------------
with tab3:
    st.header("🌍 Dynamic Maps with Folium")

    if not data_ok:
        st.warning("⚠️ No hay datos suficientes para mostrar mapas dinámicos.")
    else:
        # --- Parte 3 Task 1: Coropleta + Marker Cluster ---
        st.subheader("National Choropleth + Hospital Markers")
        st.write("Aquí va el mapa Folium interativo con coropleta distrital + cluster de hospitales.")
        # placeholder:
        # m = your_function_to_create_choropleth(...)
        # st_folium(m, width=700, height=500)

        st.write("---")

        # --- Parte 3 Task 2: Proximity for Lima & Loreto ---
        st.subheader("Proximity Visualization — Lima y Loreto")
        st.write("Aquí irán los mapas de proximidad para Lima y Loreto (círculos 10 km, etc.).")
        # placeholder:
        # m_lima = ...
        # st_folium(m_lima, width=400, height=400)
        # m_loreto = ...
        # st_folium(m_loreto, width=400, height=400)

        # Mostrar mapa de Loreto desde archivo HTML
        html_path = "assets/Loreto_hospitales_buffer.html"
        with open(html_path, "r", encoding="utf-8") as f:
            map_html = f.read()

        components.html(map_html, height=600, scrolling=True)

        st.write("---")
        st.markdown("""
        **Análisis esperado según rúbrica**  
        - Lima: concentración urbana y accesibilidad hospitalaria.  
        - Loreto: dispersión y retos geográficos en la Amazonía.  
        """)

