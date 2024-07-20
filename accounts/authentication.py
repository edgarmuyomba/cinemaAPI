from rest_framework.authentication import TokenAuthentication

class CinemaAuthentication(TokenAuthentication):
    keyword = "Bearer"