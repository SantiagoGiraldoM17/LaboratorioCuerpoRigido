# Laboratorio Cuerpo Rigido
# Análisis de Movimiento de un Brazo Robótico

Este repositorio contiene el proyecto de análisis de movimiento de un brazo robótico, incluyendo el cálculo de velocidades y aceleraciones utilizando dos métodos diferentes, la visualización de vectores de velocidad y aceleración para puntos específicos, y una animación que muestra el movimiento completo del brazo robótico.

## Contenidos del Repositorio

- `uaj_gms_LaboratorioCuerpoRigido.pdf`: Un informe completo que detalla los objetivos, metodología, resultados y conclusiones del análisis del movimiento del brazo robótico.
- `uaj_gms_LaboratorioCuerpoRigido.py`: El script de Python utilizado para realizar el análisis de movimiento, incluyendo cálculos y visualizaciones.
- `datos/`: Directorio que contiene los archivos de datos utilizados en el análisis. Esto incluye coordenadas (x, y, z) y datos de ángulo.
- `graficas/`: Directorio con las gráficas producidas por el código, incluyendo las trayectorias en 2D y 3D, así como las visualizaciones de vectores de velocidad y aceleración.

## Resumen del Proyecto

Este proyecto se centró en el análisis del movimiento de un brazo robótico utilizando datos experimentales. Se calcularon las velocidades y aceleraciones utilizando dos enfoques: un método directo basado en las diferencias de las coordenadas y un método corregido que toma en cuenta la naturaleza circular del movimiento para ciertas partes del brazo. Además, se crearon visualizaciones detalladas de los vectores de velocidad y aceleración en puntos específicos del movimiento y se desarrolló una animación que recorre todos los puntos de datos para ofrecer una comprensión dinámica del comportamiento del sistema.

## Uso del Código

Para ejecutar el script de análisis, asegúrate de tener instaladas las bibliotecas de Python `pandas`, `numpy` y `matplotlib`. El script puede ser ejecutado en un entorno de Python estándar
