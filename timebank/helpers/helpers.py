from django.contrib.auth import get_user_model

CustomUser = get_user_model()


def get_user_full_name(user: CustomUser) -> str:
    return str(user)
