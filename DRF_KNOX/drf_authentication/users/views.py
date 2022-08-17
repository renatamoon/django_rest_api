# STANDARD IMPORTS
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken


# post a new user and generate a token
@api_view(['POST'])
def login_api(request) -> Response:
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']

    __, token = AuthToken.objects.create(user)

    response_login = Response(
        {
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
            'token': token
        }
    )
    return response_login


# check the user of a specific token
@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        auth_response = Response(
            {
                'user_info': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            }
        )
        return auth_response

    not_auth_response = Response(
            {
                'ERROR': 'USER NOT AUTHENTICATED'
            }, status=400
        )
    return not_auth_response


# Post new users and give them tokens as well

