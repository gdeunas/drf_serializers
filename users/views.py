from rest_framework import generics
from users.models import User
from users.serializers import UserProfileSerializer


class UserProfileUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Эндпоинт для просмотра и редактирования профиля пользователя.
    Принимает PUT и PATCH запросы для обновления по id.
    """

    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
