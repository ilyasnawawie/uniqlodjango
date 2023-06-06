from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View
from django.db.models import Q, ManyToOneRel, ForeignKey

class ItemListView(View):
    model = None
    model_name = ""
    message = ""

    def get(self, request):
        page = request.GET.get("page", "1")
        page_size = request.GET.get("page_size", "10")
        query = request.GET.get("query", "")
        sort_column = request.GET.get("sortColumn", "")
        sort_order = request.GET.get("sortOrder", "asc")

        if not page:
            page = "1"
        if not page_size:
            page_size = "10"

        try:
            page = int(page)
            page_size = int(page_size)
        except ValueError:
            response_data = {"message": "Invalid page or page size", "status": "error"}
            return JsonResponse(response_data, status=400)

        fields = self.model._meta.get_fields()

        filter_conditions = Q()
        for field in fields:
            if not isinstance(field, (ManyToOneRel, ForeignKey)):
                filter_conditions |= Q(**{f"{field.name}__icontains": query})

        items = self.model.objects.filter(filter_conditions)

        # Get model's fields names
        model_field_names = [field.name for field in fields]

        # Apply sorting if a valid sort column is provided
        if sort_column and sort_column in model_field_names:
            if sort_order == 'desc':
                sort_column = f'-{sort_column}'
            items = items.order_by(sort_column)

        paginator = Paginator(items, page_size)

        try:
            item_page = paginator.page(page)
        except (PageNotAnInteger, EmptyPage):
            response_data = {"message": "Invalid page number", "status": "error"}
            return JsonResponse(response_data, status=400)

        item_list = [model_to_dict(item) for item in item_page]

        response_data = {
            "data": item_list,
            "meta": {
                "total": items.count(),
                "from": item_page.start_index(),
                "to": item_page.end_index(),
                "columns": [field.name for field in fields],
            },
            "message": self.message,
            "status": "ok",
        }

        return JsonResponse(response_data)