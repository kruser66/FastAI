from pydantic import BaseModel, ConfigDict

from .base import SiteResponse
from .router import site_router


class MySitesResponse(BaseModel):
    """My sites response schema."""
    sites: list[SiteResponse]

    model_config = ConfigDict(
        json_schema_extra={
            'examples': [
                {
                    'sites': [
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
            ],
        },
    )


@site_router.get('/sites/my', response_model=MySitesResponse)
async def mock_get_my_sites():
    mock_my_sites = {
        'sites': [
            {
                'id': 1,
                'title': 'Сайт Динозавры',
                'prompt': 'Последний день жизни динозавров',
                'screenshotUrl': 'http://example.com/media/index.png',
                'htmlCodeDownloadUrl': 'http://example.com/media/index.html?response-content-disposition=attachment',
                'htmlCodeUrl': 'http://example.com/media/index.html',
                'createdAt': '2025-06-15T18:29:56+00:00',
                'updatedAt': '2025-06-15T18:29:56+00:00',
            },
            {
                'id': 2,
                'title': 'Сайт Стегозавры',
                'prompt': 'Жизнь и приключения стегозавра в современном мире',
                'screenshotUrl': 'http://example.com/media/index.png',
                'htmlCodeDownloadUrl': 'http://example.com/media/index.html?response-content-disposition=attachment',
                'htmlCodeUrl': 'http://example.com/media/index.html',
                'createdAt': '2025-06-15T18:29:56+00:00',
                'updatedAt': '2025-06-15T18:29:56+00:00',
            },
        ],
    }
    return mock_my_sites
