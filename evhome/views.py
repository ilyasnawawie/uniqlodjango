from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from evhome.models import AdminAuthTokens, AuthTokens

def admin_auth_tokens(request):
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    if request.path == '/auth_tokens/':
        TokenModel = AuthTokens
    else:
        TokenModel = AdminAuthTokens

    tokens = TokenModel.objects.all()

    paginator = Paginator(tokens, page_size)

    try:
        token_page = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        response_data = {
            'message': 'Invalid page number',
            'status': 'error'
        }
        return JsonResponse(response_data, status=400)

    token_list = serializers.serialize('python', token_page, fields=('id', 'user_id', 'created_at'))

    response_data = {
        'data': {
            'tokens': token_list
        },
        'meta': {
            'total': tokens.count(),
            'from': token_page.start_index(),
            'to': token_page.end_index()
        },
        'message': 'Got authentication tokens.',
        'status': 'ok'
    }

    return JsonResponse(response_data)
