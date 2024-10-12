# perexchange

perexchange es una aplicación escrita en Python pensada para obtener, almacenar y analizar los tipos de cambio de diversas casas de cambio (con presencia en línea) en Perú. ¡Todavía en desarrollo!

## Empezar

Sigue estos pasos para poner en marcha el proyecto rápidamente:

1. Clona el repo: `git clone https://github.com/tuusuario/precio-del-dolar.git`
2. Instala las dependencias: `poetry install`. Si no tienes Poetry instalado, puedes revisar [pyproject.toml](pyproject.toml) e instalar manualmente cada paquete con pip. Si tienes más tiempo, puedes consultar la [guía oficial de instalación](https://python-poetry.org/docs/#installation).
3. Activar el entorno virtual: `poetry shell`

### Uso

Después de la instalación, ejecuta la aplicación con: `poetry run start`

Este comando:

1. Inicializa la base de datos SQLite (`perexchange.db`).
2. Obtiene los últimos tipos de cambio de la API pública de [https://cuantoestaeldolar.pe/](https://cuantoestaeldolar.pe/)
3. Guarda los datos en la base de datos para futuro análisis ya que el sitio solo provee data para el último día.
4. Finalmente, el paquete te retornará:

- El mejor precio para comprar.
- Las 3 mejores casas para vender.
- Promedios de los últimos 30 días.

## Para desarrolladores

Este proyecto no está pensado para ser ejecutado en producción. Sino fue más bien un experimento para familiarizarme con Poetry + black + ruff en un pipeline. También para experimentar con algunos paquetes que puedan soportar altas cargas de llamadas utilizando paquetes como `SQLAlchemy`, `SQLite`, `Asyncio` y `Pydantic`.

Descripción de módulos:

- `main.py`: Punto de entrada principal de la aplicación.
- `core/config.py`: Configuraciones de la aplicación.
- `db/session.py`: Configuración de la sesión asíncrona con SQLAlchemy.
- `models/exchange_rate.py`: Modelo de datos para tipos de cambio.
- `schemas/exchange_rate.py`: Esquemas de Pydantic para validación de datos.
- `services/analysis.py`: Funciones para análisis de datos.
- `services/exchange.py`: Funciones para obtener y almacenar tipos de cambio.

### Contribuir

¡Las contribuciones son bienvenidas! Sigue estos pasos:

1. Clona el repo: `git clone https://github.com/tuusuario/precio-del-dolar.git`
2. Crea un branch: `git checkout -b feature/nueva-funcionalidad`
3. Instala las dependencias de desarrollo: `poetry install --with dev`
4. ¡Haz tus cambios! (pre-commit se encargará de que tus contribuciones tengan el formato y sigan reglas de linting)
5. Haz commit, push y crea el PR!

## Licencia

Este proyecto está bajo la **licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.
