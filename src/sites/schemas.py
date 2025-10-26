from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, PositiveInt
from pydantic.alias_generators import to_camel


class SiteSchema(BaseModel):

    id: PositiveInt = Field(..., description='Id сайта')
    prompt: str = Field(..., description='Промпт создания сайта')
    title: str = Field(..., description='Заголовок сайта')
    screenshot_url: str = Field(..., description='Ссылка на скриншот сайта')
    html_code_download_url: str = Field(..., description='Ссылка на загрузку сайта')
    html_code_url: str = Field(..., description='Ссылка на сайт')
    created_at: datetime = Field(..., description='Дата и время создания сайта')
    updated_at: datetime = Field(..., description='Дата и время создания сайта')


class SiteCreateRequestSchema(BaseModel):
    prompt: str = Field(..., description='Промпт создания сайта')
    title: str = Field(..., description='Заголовок сайта')

    model_config = ConfigDict(
        json_schema_extra={
            'examples': [
                {
                    'prompt': 'Портфолио профессионального спортсмена BMX-Freestyle',
                    'title': 'Kruglova Fun Club',
                },
            ],
        },
    )


class SiteGenerateRequestSchema(BaseModel):
    prompt: str = Field(..., description='Промпт создания сайта')

    model_config = ConfigDict(
        json_schema_extra={
            'examples': [
                {
                    'prompt': 'Портфолио профессионального спортсмена BMX-Freestyle',
                },
            ],
        },
    )


class SiteResponseSchema(SiteSchema):
    """Site response schema."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        json_schema_extra={
            'examples': [
                    {
                        'id': 1,
                        'title': 'Фан клуб Домино',
                        'prompt': 'Сайт любителей играть в домино',
                        'screenshotUrl': 'http://example.com/media/index.png',
                        'htmlCodeDownloadUrl': 'http://example.com/media/index.html?response-content-disposition=attachment',
                        'htmlCodeUrl': 'http://example.com/media/index.html',
                        'createdAt': '2025-06-15T18:29:56+00:00',
                        'updatedAt': '2025-06-15T18:29:56+00:00',
                    },
                ],
        },
    )
