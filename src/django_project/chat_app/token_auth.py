from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import AccessToken

from src.django_project.useraccount_app.models import User


@database_sync_to_async
def get_user(token_key):
    try:
        token = AccessToken(token_key)
        user_id = token.payload["user_id"]
        user = User.objects.get(pk=user_id)
    except Exception:
        return AnonymousUser
    return user


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        query = dict(x.split("=") for x in scope["query_string"].decode().split("&"))
        token_key = query.get("token", "")
        scope["user"] = await get_user(token_key)
        return await super().__call__(scope, receive, send)
