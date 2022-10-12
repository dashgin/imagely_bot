from typing import Optional

from pydantic import BaseSettings


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

    class Config:
        case_sensitive = True


settings = Settings()
