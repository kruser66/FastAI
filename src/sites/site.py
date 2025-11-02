from .base import SiteResponse
from .router import site_router


@site_router.get('/sites/{site_id}', response_model=SiteResponse)
async def mock_get_site_by_id(site_id: int):
    mock_get_site = {
        'id': site_id,
        'title': 'Сайт Динозавры',
        'prompt': 'Последний день жизни динозавров',
        'screenshotUrl': 'http://example.com/media/index.png',
        'htmlCodeDownloadUrl': 'http://example.com/media/index.html?response-content-disposition=attachment',
        'htmlCodeUrl': 'http://example.com/media/index.html',
        'createdAt': '2025-06-15T18:29:56+00:00',
        'updatedAt': '2025-06-15T18:29:56+00:00',
    }
    return mock_get_site
