# Django の urls.py では WSGI ベースのアプリケーションを扱うため、
# FastAPI のような ASGI アプリを正しく組み込む必要があるらしい

import os
import django # type: ignore
from django.core.asgi import get_asgi_application # type: ignore
from fastapi import FastAPI # type: ignore
from starlette.middleware.wsgi import WSGIMiddleware # type: ignore
from starlette.routing import Mount # type: ignore
from starlette.applications import Starlette # type: ignore


# Django 環境変数を設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio.settings')

# Django を初期化
django.setup()

# Django ASGI アプリケーションを取得
django_app = get_asgi_application()

# FastAPI アプリを作成
fastapi_app = FastAPI()

@fastapi_app.get("/")
async def get_hello():
    return {'message': 'Hello World'}

# FastAPI のエンドポイントを `/fastapi/` にマウント
app = Starlette(routes=[
    Mount("/fastapi", fastapi_app)  # "/fastapi" に FastAPI をマウント
])

# Django と FastAPI を共存させる ASGI アプリ
async def application(scope, receive, send):
    if scope["path"].startswith("/fastapi"):
        await app(scope, receive, send)  # FastAPI にルーティング
    else:
        await django_app(scope, receive, send)  # Django にルーティング