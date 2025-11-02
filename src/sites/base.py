from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from api_model import Site


class SiteResponse(Site):

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
