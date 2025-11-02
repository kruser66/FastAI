from pydantic import BaseModel, ConfigDict, StrictStr
from pydantic.alias_generators import to_camel

from api_model import Site

from .router import site_router


class SiteCreateRequest(BaseModel):
    prompt: StrictStr
    """Промпт создания сайта"""
    title: str | None = None
    """Заголовок сайта"""

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


class SiteCreateResponse(Site):

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


@site_router.post('/sites/create', response_model=SiteCreateResponse)
def mock_site_create(request: SiteCreateRequest):
    mock_site_created = {
        'id': 1,
        'title': request.title or '',
        'prompt': request.prompt,
        'screenshotUrl': 'http://example.com/media/index.png',
        'htmlCodeDownloadUrl': 'http://example.com/media/index.html?response-content-disposition=attachment',
        'htmlCodeUrl': 'http://example.com/media/index.html',
        'createdAt': '2025-06-15T18:29:56+00:00',
        'updatedAt': '2025-06-15T18:29:56+00:00',
    }
    return mock_site_created
