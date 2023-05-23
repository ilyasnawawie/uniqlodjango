from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from evhome.models import AdminAuthTokens

def admin_auth_tokens(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('pagesize', 10))

    tokens = AdminAuthTokens.objects.all()

    paginator = Paginator(tokens, page_size)

    try:
        token_page = paginator.page(page)
    except EmptyPage:
        response_data = {
            'message': 'Invalid page number',
            'status': 'error'
        }
        return JsonResponse(response_data, status=400)

    token_list = []
    for token in token_page:
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
            'total': tokens.count(),
            'from': token_page.start_index(),
            'to': token_page.end_index()
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
