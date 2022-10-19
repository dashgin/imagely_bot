from typing import Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Imagely"
    THREADS: Optional[int] = None
    PORT: int = 8000
    VERSION: str = "0.1.0"
    LOG_LEVEL: str = "info"

    SWAGGER_META: dict = {
        "contact": {
            "name": "Dashgin Khudiyev",
            "url": "https://github.com/dashgin",
            "email": "76277687+dashgin@users.noreply.github.com",
        },
        "license_info": {
            "name": "MIT License",
            "url": "https://github.com/<username>/<repo>/blob/main/LICENSE.txt",
        },
        "openapi_tags": [
            {
                "name": "Editing",
                "description": "Endpoints that perform background editing with different image sources like file, url, etc.",
                "externalDocs": {
                    "description": "GitHub Source",
                    "url": "https://github.com/danielgatis/rembg",
                },
            },
        ],
    }

    TG_BOT_TOKEN: str = Field(..., env="TG_BOT_TOKEN")
    TESSERACT_PATH: str = Field(..., env="TESSERACT_PATH")
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

if __name__ == "__main__":
    print(settings.TG_BOT_TOKEN)
    print(settings.TESSERACT_PATH)
