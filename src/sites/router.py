
import anyio
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from sites.schemas import MySitesResponseSchema, SiteCreateRequestSchema, SiteGenerateRequestSchema, SiteResponseSchema

# Продумать импорты роутеров
site_router = APIRouter(prefix='/api/v1')


@site_router.post('/sites/create', response_model=SiteResponseSchema)
def mock_site_create(request: SiteCreateRequestSchema):
    mock_site_created = {
        'id': 1,
        'title': request.title,
        'prompt': request.prompt,
        'screenshotUrl': 'http://example.com/media/index.png',
        'htmlCodeDownloadUrl': 'http://example.com/media/index.html?response-content-disposition=attachment',
        'htmlCodeUrl': 'http://example.com/media/index.html',
        'createdAt': '2025-06-15T18:29:56+00:00',
        'updatedAt': '2025-06-15T18:29:56+00:00',
    }
    return mock_site_created


@site_router.get('/sites/my', response_model=MySitesResponseSchema)
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


async def mock_generate_text_chunks(file_path):

    with open(file_path, encoding='utf-8') as file:
        for line in file:
            await anyio.sleep(0.1)
            yield line.encode('utf-8')


@site_router.post('/sites/{site_id}/generate')
async def generate_site(site_id: int, request: SiteGenerateRequestSchema):

    file_path = '/home/kruser/python/test/FastAI/src/mock/mock.html'

    return StreamingResponse(
        content=mock_generate_text_chunks(file_path),
        media_type="text/plain; charset=utf-8",
    )


@site_router.get('/sites/{site_id}', response_model=SiteResponseSchema)
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
