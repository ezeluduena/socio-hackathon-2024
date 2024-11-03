# Poniendo a trabajar a los números: Un análisis de la correlación entre el presupuesto nacional destinado a políticas de empleo y las tasas laborales en Argentina entre los períodos 2011-2015 y 2015-2019

En este repositorio se comparten los datos y scripts utilizados en el trabajo presentado en el **[Socio-hackathon Investigar en Sociales 2024](https://sociales.unc.edu.ar/content/todav-est-s-tiempo-de-presentarte-en-el-i-socio-hackathon-investigar-en-sociales-2024-la)** por **Manuel Barragán, Micaela de Hernández, Ezequiel Ludueña y Marco Spalletti**.

La pregunta que guió el análisis y desarrollo de este trabajo fue:

**¿En qué medida el presupuesto anual ejecutado para la función "Trabajo" incide en las estadísticas laborales?**

Se pretendió analizar el impacto de los montos dedicados a políticas laborales, desagregando en distintas poblaciones, y comparando entre distintos períodos de gestión.

Para realizar este trabajo, las fuentes de datos utilizadas fueron los [datos abiertos disponibles del presupuesto nacional](https://www.presupuestoabierto.gob.ar/sici/datos-abiertos) y los resultados que se obtuvieron a partir del trabajo con la [Encuesta Permanente de Hogares (EPH)](https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos), realizada por el [Instituto Nacional de Estadísticas y Censos (INDEC)](https://www.indec.gob.ar/), que releva de manera trimestral los datos sociodemográficos y socioeconómicos de la población.

En [`informe.pdf`](/informe.pdf) se puede leer el informe del proyecto presentado en la competencia.

## Estructura del repositorio

- **Directorios:**

  - **[`data`](/data):** Datos de entrada y generados.
  - **[`docs`](/docs):** Documentación relacionada con las bases de datos utilizadas en el proyecto.
  - **[`plots`](/plots):** Gráficos y visualizaciones generadas.
  - **[`utils`](/utils):** Scripts utilizados para la descarga de datos de entrada.  

  - **Scripts de *R*:**
  
    **[`scripts_r`](/scripts_r):** Directorio con los scripts utilizados para procesar los datos de la EPH año por año y generar valores para las distintas tasas analizadas.

  - **Notebooks de Python:**

    **[`notebooks`](/notebooks):** Directorio con los Jupyter Notebooks realizados, utilizando distintas librerias de *Python*.
    - **[`presupuesto`](/notebooks/presupuesto.ipynb):** Scripts de procesamiento y visualización realizados sobre la base de datos de presupuesto abierto del gobierno nacional.
    - **[`ipim`](/notebooks/ipim.ipynb):** Scripts de procesamiento realizados sobre los datos del Índice de Precios al por Mayor (IPIM), utilizado para deflactar los valores monetarios.
    - **[`eph`](/notebooks/eph.ipynb):** Scripts de procesamiento y visualización sobre el trabajo realizado previamente utilizando los datos de la EPH.
    - **[`cruce_eph_presupuesto`](/notebooks/cruce_eph_presupuesto.ipynb):** Scripts de procesamiento y visualización realizados sobre los resultados generados sobre el presupuesto y la EPH.

- **Otros archivos:**
  - **[`informe.pdf`](/informe.pdf):** informe sobre el trabajo realizado.
  - **[`requirements.txt`](/requirements.txt):** listado de librerías de *Python* utilizadas en los notebooks.
  - **[`.gitignore`](/.gitignore):** listado de archivos de los que no se requiere versionado en el repositorio.

## Instrucciones de uso para corrección y reproducción del trabajo

1. Clonar el repositorio.

```bash
git clone https://github.com/ezeluduena/socio-hackathon-2024.git
cd socio-hackathon-2024
```

### Notebooks de *Python*

1. Crear entorno virtual de *Python*.

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias de *Python*.

```bash
pip install -r requirements.txt
```

3. Abrir cualquiera de los notebooks con un IDE que permita ejecutarlos utilizando el entorno virtual creado previamente.

### Scripts en *R*

1. Instalar *R* desde [CRAN](https://cran.r-project.org/) y [RStudio](https://posit.co/download/rstudio-desktop/) o cualquier IDE donde ejecutar *R*.

2. Instalar las dependencias necesarias:

```r
install.packages("tidyverse")
install.packages("foreign")
install.packages("eph")
install.packages("dplyr")
install.packages("questionr")
install.packages("stringr")
install.packages("gmodels")
install.packages("rstatix")
install.packages("writexl")
```

3. Abrir el repositorio y ejecutar los scripts de *R* desde *RStudio* o el IDE de su preferencia.
