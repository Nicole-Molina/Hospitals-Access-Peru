# Hospitals-Access-Peru

Este documento incluye las instrucciones mínimas para ejecutar el proyecto, además de explicar cómo se filtraron los hospitales por "estado de funcionamiento".

## Instrucciones de ejecución simples 
1. Crear y activar entorno virtual.
2. pip install -r requirements.txt.
3. Ejecutar el notebook con jupyter notebook geopandas.ipynb.

## ¿Cómo se filtraron los hospitales en funcionamiento?

Para las tareas de la parte 2, se consideraron como hospitales en funcionamiento las observaciones donde la columna Condición tomaba el valor EN FUNCIONAMIENTO.

En cambio, para la tarea 1 de la parte 3, se introdujo una precisión adicional: se filtraron las instituciones prestadoras de servicios de salud para quedarse solo con aquellas que correspondían a hospitales y centros médicos en funcionamiento, excluyendo establecimientos de menor nivel (postas médicas, entre otros). Específicamente, se mantuvieron los siguientes tipos de instituciones:

- "HOSPITALES O CLÍNICAS DE ATENCIÓN GENERAL"
- "HOSPITALES O CLÍNICAS DE ATENCIÓN ESPECIALIZADA"
- "CENTROS DE SALUD CON CAMAS DE INTERNAMIENTO"
- "CENTROS DE SALUD O CENTROS MÉDICOS"
- "CENTROS DE SALUD O CENTROS MÉDICOS, CENTROS DE SALUD O CENTROS MÉDICOS" (variación en los datos)

Esta diferenciación se realizó para visualizar la distribución de hospitales de mayor complejidad a nivel distrital en el Perú.

No fue necesario aplicar normalización compleja de texto, ya que la base de datos provee directamente el valor estándar EN FUNCIONAMIENTO.

De esta manera, se garantiza que el dataset resultante contenga únicamente los hospitales y centros médicos que realmente están en operación.
