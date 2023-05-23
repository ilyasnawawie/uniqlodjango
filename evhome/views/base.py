from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from django.views import View

class ItemListView(View):
    model = None
    model_name = ''
    message = ''

    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)

        items = self.model.objects.all()

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
                self.model_name: item_list
            },
            'meta': {
                'total': items.count(),
                'from': item_page.start_index(),
                'to': item_page.end_index()
            },
            'message': self.message,
            'status': 'ok'
        }

        return JsonResponse(response_data)
