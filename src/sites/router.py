from itertools import count

import anyio
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from sites.schemas import SiteCreateRequestSchema, SiteGenerateRequestSchema, SiteResponseSchema

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


@site_router.get('/sites/my', response_model=list[SiteResponseSchema])
async def mock_get_my_sites():
    mock_my_sites = [
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
            'prompt': 'Жизнь и приключения сьегозавра в совремннном мире',
            'screenshotUrl': 'http://example.com/media/index.png',
            'htmlCodeDownloadUrl': 'http://example.com/media/index.html?response-content-disposition=attachment',
            'htmlCodeUrl': 'http://example.com/media/index.html',
            'createdAt': '2025-06-15T18:29:56+00:00',
            'updatedAt': '2025-06-15T18:29:56+00:00',
        },
    ]
    return mock_my_sites


@site_router.post('/sites/{site_id}/generate')
async def show_counter(site_id: int, request: SiteGenerateRequestSchema):
    async def generate_numbers():
        for i in count():
            await anyio.sleep(0.5)  # Имитация обработки
            yield f'{i}\n'

    return StreamingResponse(generate_numbers(), media_type='text/html')


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
