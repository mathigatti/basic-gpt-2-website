# Basic GPT-2 website
Sitio web hecho en flask para generar periodicamente textos con el modelo de red neuronal GPT-2

El sitio web esta formado por dos scripts principales, `app.py` que ejecuta el sitio web y `gpt-2.py` que genera un texto nuevo periodicamente y lo guarda en `data/texto_generado.txt`

## Requerimientos

- Python 3
- Instalar librerias de python (Prueben algo asi como `pip install -r requirements.txt`)

## Para inicializar el modelo por primera vez

Esto generará una carpeta llamada aitextgen donde se alojara el modelo pre-entrenado.

```
python init_gpt-2.py
```

## Inicializar el sitio web

El script `gpt-2.py` lee el archivo `data/texto_inicial.txt` y utilizando eso como inicio genera un texto que luego guarda en `data/texto_generado.txt`

```
# Comando para ejecutar el script
python gpt-2.py
```

El script `app.py` genera un sitio web el cual cada vez que un usuario accede muestra en pantalla el contenido que haya en ese momento en `data/texto_generado.txt`

```
# Comando para ejecutar el script
python app.py
```