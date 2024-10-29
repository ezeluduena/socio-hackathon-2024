# Análisis de la inversión en políticas laborales y su efecto durante el período 2012-2019 en Argentina

En este repositorio se comparten los datos y scripts utilizados en el trabajo presentado en el **[Socio-hackathon Investigar en Sociales 2024](https://sociales.unc.edu.ar/content/todav-est-s-tiempo-de-presentarte-en-el-i-socio-hackathon-investigar-en-sociales-2024-la)** por **Manuel Barragán, Micaela De Hernández, Ezequiel Ludueña y Marco Spalletti**.

La pregunta que guió el análisis y desarrollo de este trabajo fue:

**¿En qué medida el presupuesto anual ejecutado para la función "Trabajo" incide en las estadísticas laborales?**

Se pretendió analizar el impacto de los montos dedicados a políticas laborales, desagregando en distintas poblaciones, y comparando entre distintos períodos de gestión.

Para realizar este trabajo, las fuentes de datos utilizadas fueron los [datos abiertos disponibles del presupuesto nacional](https://www.presupuestoabierto.gob.ar/sici/datos-abiertos) y los resultados que se obtuvieron a partir del trabajo con la [Encuesta Permanente de Hogares (EPH)](https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos), realizada por el [INDEC](https://www.indec.gob.ar/), que releva de manera trimestral los datos sociodemográficos y socioeconómicos de la población.

En [`informe.pdf`](https://github.com/ezeluduena/socio-hackathon/blob/main/informe.pdf) se puede leer el informe del proyecto presentado en la competencia.

## Estructura del repositorio

- **Directorios:**

  - **[`data`](https://github.com/ezeluduena/socio-hackathon/tree/main/data):** Datos de entrada y generados.
  - **[`docs`](https://github.com/ezeluduena/socio-hackathon/tree/main/docs):** Documentación relacionada con las bases de datos utilizadas en el proyecto.
  - **[`plots`](https://github.com/ezeluduena/socio-hackathon/tree/main/plots):** Gráficos y visualizaciones generadas.
  - **[`utils`](https://github.com/ezeluduena/socio-hackathon/tree/main/utils):** Scripts utilizados para la descarga de datos de entrada.  

- **Scripts de R:**
  - **[`scripts_r`](https://github.com/ezeluduena/socio-hackathon/blob/main/scripts_r):** Directorio con los scripts utilizados para procesar los datos de la EPH año por año y generar valores para las distintas tasas analizadas.

- **Notebooks de Python:**
  - **[`presupuesto`](https://github.com/ezeluduena/socio-hackathon/blob/main/presupuesto.ipynb):** Scripts de procesamiento y visualización realizados sobre la base de datos de presupuesto abierto del gobierno nacional.
  - **[`ipim`](https://github.com/ezeluduena/socio-hackathon/blob/main/ipim.ipynb):** Scripts de procesamiento realizados sobre los datos del Índice de Precios al por Mayor (IPIM), utilizado para deflactar los valores monetarios.
  - **[`eph`](https://github.com/ezeluduena/socio-hackathon/blob/main/eph.ipynb):** Scripts de procesamiento y visualización sobre el trabajo realizado previamente utilizando los datos de la EPH.
  - **[`cruce_eph_presupuesto`](https://github.com/ezeluduena/socio-hackathon/blob/main/cruce_eph_presupuesto.ipynb):** Scripts de procesamiento y visualización realizados sobre los resultados generados sobre el presupuesto y la EPH.

- **Otros archivos:**
  - **[`informe.pdf`](https://github.com/ezeluduena/socio-hackathon/blob/main/informe.pdf):** informe sobre el trabajo realizado.
  - **[`requirements.txt`](https://github.com/ezeluduena/socio-hackathon/blob/main/requirements.txt):** listado de librerías de python utilizadas en los notebooks.
  - **[`.gitignore`](/.gitignore):** listado de archivos de los que no se requiere versionado en el repositorio.

## Instrucciones de uso

1. Clonar el repositorio.

```bash
git clone https://github.com/ezeluduena/socio-hackathon.git
cd socio-hackathon
```

### Notebooks de python

1. Crear entorno virtual de python.

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias de python.

```bash
pip install -r requirements.txt
```

3. Abrir cualquiera de los notebooks con un IDE que permita ejecutarlos utilizando el entorno virtual creado previamente.

### Scripts en R-markdown
<!-- TODO -->

## TODOs:
- Comentarios eph.ipynb
- Comentarios cruce_eph_presupuesto.ipynb
- Comentarios y mejor formateo del código en scripts_r
- Terminar el readme.md
  - revisar escritura sea acorde con el informe
  - terminar el cómo ejecutar los scritps de R
- Subir informe en formato pdf
- agregar algo sobre reproducibilidad en el repo
- cambiar nombre del repo a socio-hackathon-2024
- agregar tag de entrega
- hacer público el repositorio
- agregar tags de github