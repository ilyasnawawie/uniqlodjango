from django.shortcuts import render
from evhome.models import AdminAuthTokens  # Replace "evhome" with your app name
from django.http import JsonResponse

def admin_auth_tokens(request):
    tokens = AdminAuthTokens.objects.all()[:10]  # Fetch only 10 rows

    token_list = []
    for token in tokens:
        token_list.append({
            'id': token.id,
            'user_id': token.user_id,
            'created_at': token.created_at
        })

    response_data = {
        'data': {
            'tokens': token_list
        },
        'meta': {
            'total': AdminAuthTokens.objects.count(),
            'from': 0,
            'to': min(10, AdminAuthTokens.objects.count())
        },
        'message': 'Got admin authentication tokens.',
        'status': 'ok'
    }

    return JsonResponse(response_data)
