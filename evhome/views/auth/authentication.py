from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from evhome.models import AuthTokens, Users
from django.contrib.auth.hashers import check_password
import uuid


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(email=email)
            print(f'Email: {email}')
            print(f'Hashed input password: {password}')
            print(f'Stored password: {user.password}')
            if check_password(password, user.password):
                print('Passwords match. Generating token...')
                token = AuthTokens.objects.create(
                    id=str(uuid.uuid4()),
                    user=user
                )
                return JsonResponse({'token': token.id})
            else:
                print('Passwords do not match.')
                return JsonResponse({'error': 'Invalid login credentials.'}, status=401)
        except Users.DoesNotExist:
            print(f'No user found with email {email}')
            return JsonResponse({'error': 'Invalid login credentials.'}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
