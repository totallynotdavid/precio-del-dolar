import logging
import os
from datetime import time


class Settings:
    API_URL: str = "https://cuantoestaeldolar.pe/_next/data/ZZEdJMkcvJRPEYUmapmdz/cambio-de-dolar-online.json"
    DATABASE_URL: str = "sqlite+aiosqlite:///./perexchange.db"
    API_RATE_LIMIT: int = 6  # calls per hour
    BUSINESS_HOURS_START: time = time(9, 0)  # 9:00 AM
    BUSINESS_HOURS_END: time = time(17, 0)  # 5:00 PM
    BUSINESS_DAYS: list = [0, 1, 2, 3, 4, 5]  # Monday to Saturday

    # Logging configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


settings = Settings()

# Initialize logging
logging.basicConfig(level=settings.LOG_LEVEL, format=settings.LOG_FORMAT)
logger = logging.getLogger(__name__)
