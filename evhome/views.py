from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from evhome.models import AdminAuthTokens, AuthTokens, ChargePointLocations, AuthGroup, AuthUser

def items_list(request):
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    if request.path == '/auth_tokens/':
        ItemModel = AuthTokens
        model_name = 'tokens'
        message = 'Got tokens.'
    elif request.path == '/charge_point_locations/':
        ItemModel = ChargePointLocations
        model_name = 'charge point locations'
        message = 'Got charge point locations.'
    elif request.path ==  '/admin_auth_tokens/':
        ItemModel = AdminAuthTokens
        model_name = 'admin tokens'
        message = 'Got admin tokens.'
    elif request.path ==  '/auth_groups/':
        ItemModel = AuthGroup
        model_name = 'auth groups'
        message = 'Got auth groups.'
    elif request.path == '/auth_user/':
        ItemModel = AuthUser
        model_name= 'auth user'
        message = "Got auth user"

    items = ItemModel.objects.all()

    paginator = Paginator(items, page_size)

    try:
        item_page = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        response_data = {
            'message': 'Invalid page number',
            'status': 'error'
        }
        return JsonResponse(response_data, status=400)

    item_list = serializers.serialize('python', item_page)

    response_data = {
        'data': {
            model_name: item_list
        },
        'meta': {
            'total': items.count(),
            'from': item_page.start_index(),
            'to': item_page.end_index()
        },
        'message': message,
        'status': 'ok'
    }

    return JsonResponse(response_data)
