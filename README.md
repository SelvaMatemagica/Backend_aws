# Metodo de funcionalidad del backend en aws
---
 Proyecto basado unicamente en python, y usando la libreria pg800

## Desarrollo del backend en local para subirlo a AWS

1. Crea una carpeta donde guardar el entorno (directorio raiz del proyecto):
   ```bash
   mkdir lib
   ```
2. Instala dependencias en el entorno local:
   ```bash
   pip install --target=lib -r requirements.txt
   ```
3. Si va a instalar más dependencias, investigar si son compatibles con AWS (Version: Amazon Linux 2023 (AL2023))
   
5. Las dependencias instaladas tambien deben ser añadidas a la carpeta lib
   ```bash
   pip install --target=lib (nombre_dependencia)
   ```
7. El archivo Main.py es lambda_function.py (formato de reconocimiento de AWS).

9. Una vez realizados los cambios en local, convertir a un archivo .ZIP
   ```bash
   compress-archive lib/* nombre_del_archivo.zip
   compress-archive lambda_function.py -update nombre_del_archivo.zip
   ```
10. Subir el archivo .ZIP a AWS Lambda


## Desarrollo del backend en AWS

1. Solamente se debe ingresar a AWS Lambda y usar Visual Studio Code interno en lambda
2. De requerir más dependencias, debe realizar el proceso mostrado en (Desarrollo del backend en local para subirlo a AWS) con las dependencias ya instaladas en el archivo lib


