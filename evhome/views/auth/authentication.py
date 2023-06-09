from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from evhome.models import AuthTokens, Users
from django.contrib.auth.hashers import check_password
import uuid
import re


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

        if not email or not password:
            return JsonResponse({'message': 'The given data was invalid.',
                                 'errors': {'email': ['Email and password are required.']},
                                 'status': 400},
                                status=400)
        elif not re.search(email_regex, email):
            return JsonResponse({'message': 'The given data was invalid.',
                                 'errors': {'email': ['The email format is incorrect.']},
                                 'status': 400},
                                status=400)

        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                token = AuthTokens.objects.create(
                    id=str(uuid.uuid4()),
                    user=user
                )
                return JsonResponse({'token': token.id,
                                     'created_at': token.created_at.isoformat(),
                                     'status': 200})
            else:
                return JsonResponse({'message': 'The given data was invalid.',
                                     'errors': {'password': ['Please check your password.']},
                                     'status': 401},
                                    status=401)
        except Users.DoesNotExist:
            return JsonResponse({'message': 'The given data was invalid.',
                                 'errors': {'email': ['These credentials do not match our records.']},
                                 'status': 401},
                                status=401)
    else:
        return JsonResponse({'message': 'Invalid request method.',
                             'errors': {'detail': ['This endpoint only accepts POST requests.']},
                             'status': 400},
                            status=400)
