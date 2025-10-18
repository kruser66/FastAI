# FastAI

## FastAPI & AI project.

Проект генерирует сайты по текстовому описанию.

## Как развернуть локально

В проекте используется проектный менеджер uv.

Сначала установите uv. Для macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Для Windows:
```shell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

или воспользуйтесь [документацией](https://docs.astral.sh/uv/getting-started/installation/), если у вас не Linux.


Склонируйте себе репозиторий.

```bash
git clone git@github.com:kruser66/FastAI.git
```

Перейдите в каталог проекта и запустите

```bash
uv venv
uv sync
```

Проектный менеджер установит все необходимые зависимости.


## Как запустить

Для локального запуска проекта используйте

```bash
fastapi run src/main.py
```

или, если установлен Make, то

```bash
make run
```

----

Инструкции и справочная информация по разворачиванию локальной инсталляции собраны
в документе [CONTRIBUTING.md](./CONTRIBUTING.md).
