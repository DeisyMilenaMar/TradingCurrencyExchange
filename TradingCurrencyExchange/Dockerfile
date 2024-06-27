# Usar la imagen base de Python 3.10.12 basada en Debian Bullseye
FROM python:3.10.12-bullseye


# Establecer la variable de entorno para la salida de Python
ENV PYTHONUNBUFFERED 1

# Copiar todos los archivos y carpetas que se encuentran al mismo nivel (.) del Dockerfile a una carpeta llamada code
COPY . /code/

# Establecer el directorio de trabajo en el contenedor
WORKDIR /codeSETIC

# Copiar el archivo de requisitos y luego instalar las dependencias de Python
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Instalar psycopg2-binary para PostgreSQL
RUN pip install psycopg2-binary


# Comando para ejecutar la aplicación (ajustar según la configuración de tu proyecto)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]