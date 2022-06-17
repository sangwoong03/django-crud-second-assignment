import jwt

from django.http import JsonResponse

from users.models import User
from assignment_2nd.settings import ALGORITHM, SECRET_KEY


def token_decorator(func) :
    def wrapper(self, request, *args, **kwargs) :
        try:
            access_token = request.headers.get("Authorization", None)
            payload      = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            user         = User.objects.get(id = payload["user_id"])
            request.user = user

            return func(self, request, *args, **kwargs)

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)

    return wrapper