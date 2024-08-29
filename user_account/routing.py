from django.urls import path
from . import consumers


websocket_urlpatterns = [
<<<<<<< HEAD
    path("user/chat/", consumers.ChatConsumer.as_asgi()),
    path("user/chat/<int:thread_id>/", consumers.ChatConsumer.as_asgi()),
]
=======
    path('user/chat/', consumers.ChatConsumer.as_asgi()),
]
>>>>>>> 4f30a576e52fe87bdb08230faecc6802685494dd
