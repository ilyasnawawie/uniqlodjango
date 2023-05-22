from django.shortcuts import render
from evhome.models import AdminAuthTokens 
from django.http import JsonResponse

def admin_auth_tokens(request):
    tokens = AdminAuthTokens.objects.all()[:10]

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

'''
from django.shortcuts import render
from evhome.models import AdminAuthTokens 

def admin_auth_tokens(request):
    tokens = AdminAuthTokens.objects.all()
    return render(request, 'evhome/admin_auth_tokens.html', {'tokens': tokens})
'''
