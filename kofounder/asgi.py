import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import user_account.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kofounder.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            user_account.routing.websocket_urlpatterns
        )
    ),
})
