import os
from functools import lru_cache

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "CloudVPS Pro")
    ENV: str = os.getenv("ENV", "development")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change_me_secret")
    JWT_ACCESS_EXPIRES_MIN: int = int(os.getenv("JWT_ACCESS_EXPIRES_MIN", "30"))
    JWT_REFRESH_EXPIRES_DAYS: int = int(os.getenv("JWT_REFRESH_EXPIRES_DAYS", "30"))

    DB_ENGINE: str = os.getenv("DB_ENGINE", "postgresql")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "cloudvps")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "cloudvps")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "cloudvps")
    SQLITE_PATH: str = os.getenv("SQLITE_PATH", "/data/app.db")

    REDIS_HOST: str = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_DB: int = int(os.getenv("REDIS_DB", "0"))

    SMTP_HOST: str = os.getenv("SMTP_HOST", "")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    SMTP_FROM: str = os.getenv("SMTP_FROM", "noreply@example.com")

    HCAPTCHA_SITEKEY: str = os.getenv("HCAPTCHA_SITEKEY", "")
    HCAPTCHA_SECRET: str = os.getenv("HCAPTCHA_SECRET", "")

    STRIPE_SECRET: str = os.getenv("STRIPE_SECRET", "")
    STRIPE_WEBHOOK_SECRET: str = os.getenv("STRIPE_WEBHOOK_SECRET", "")
    PAYPAL_CLIENT_ID: str = os.getenv("PAYPAL_CLIENT_ID", "")
    PAYPAL_CLIENT_SECRET: str = os.getenv("PAYPAL_CLIENT_SECRET", "")
    ZARINPAL_MERCHANT_ID: str = os.getenv("ZARINPAL_MERCHANT_ID", "")
    NEXTPAY_API_KEY: str = os.getenv("NEXTPAY_API_KEY", "")
    BTCPAY_SERVER_URL: str = os.getenv("BTCPAY_SERVER_URL", "")
    BTCPAY_API_KEY: str = os.getenv("BTCPAY_API_KEY", "")

    PROMETHEUS_MULTIPROC_DIR: str = os.getenv("PROMETHEUS_MULTIPROC_DIR", "/tmp")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

@lru_cache
def get_settings():
    return Settings()
