# Image Moderation API

FastAPI-сервер, проверяющий изображения на NSFW-контент через DeepAI NSFW Detector.

## Установка и запуск

```bash
git clone https://github.com/Voppor41/image-moderation-api.git
cd image-moderation-api

# Создать и активировать виртуальное окружение (опционально)
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows

# Установка зависимостей
pip install -r requirements.txt

# Установить API-ключ
echo "DEEPAI_API_KEY=your_deepai_api_key_here" > .env

# Запуск сервера
uvicorn main:app --reload
