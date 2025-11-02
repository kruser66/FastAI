import anyio
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, ConfigDict, StrictStr

from .router import site_router


async def mock_generate_text_chunks(file_path):

    with open(file_path, encoding='utf-8') as file:
        for line in file:
            await anyio.sleep(0.1)
            yield line.encode('utf-8')


class SiteGenerateRequest(BaseModel):
    prompt: StrictStr
    """Промпт создания сайта"""

    model_config = ConfigDict(
        json_schema_extra={
            'examples': [
                {
                    'prompt': 'Портфолио профессионального спортсмена BMX-Freestyle',
                },
            ],
        },
    )


@site_router.post('/sites/{site_id}/generate')
async def generate_site(site_id: int, request: SiteGenerateRequest):

    file_path = '/home/kruser/python/test/FastAI/src/mock/mock.html'

    return StreamingResponse(
        content=mock_generate_text_chunks(file_path),
        media_type="text/plain; charset=utf-8",
    )
