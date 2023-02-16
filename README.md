# Momo Helper (Web Scraping API)

Este proyecto proporciona una API sencilla que rastrea un sitio web para obtener el valor mínimo "Compra" de divisas extranjeras. Los datos se obtienen de "https://cuantoestaeldolar.pe/".

## Prerrequisitos

Antes de poder ejecutar la API, asegúrese de tener instalado lo siguiente:

- Python 3.6 o superior
- Virtualenv (opcional)
- Node.js (si deseas ejecutar la API con PM2)

## Instalación

1. Clona este repositorio en tu ordenador local.
2. Navega hasta el directorio del proyecto.
3. Crea un entorno virtual: `python3 -m venv env`.
4. Activa el entorno virtual: `source env/bin/activate` (Linux/Mac) o `env\Scripts\activate` (Windows)
5. Instalar los paquetes necesarios: pip install -r requirements.txt.
6. Ejecuta la API: `flask --app api run`.
