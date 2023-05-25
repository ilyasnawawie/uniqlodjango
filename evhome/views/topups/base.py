from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import FieldError
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View


class ItemListView(View):
    model = None
    model_name = ""
    message = ""

    def get(self, request):
        page = request.GET.get("page", "1")
        page_size = request.GET.get("page_size", "10")

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

        order = request.GET.get("order", "asc")
        order_by = request.GET.get("order_by", "id")

        if order == "desc":
            order_by = "-" + order_by

        try:
            items = self.model.objects.all().order_by(order_by)
        except FieldError:
            response_data = {"message": f"Invalid field: {order_by}", "status": "error"}
            return JsonResponse(response_data, status=400)

        paginator = Paginator(items, page_size)

        try:
            item_page = paginator.page(page)
        except (PageNotAnInteger, EmptyPage):
            response_data = {"message": "Invalid page number", "status": "error"}
            return JsonResponse(response_data, status=400)

        item_list = [model_to_dict(item) for item in item_page]

        response_data = {
            "data": {self.model_name: item_list},
            "meta": {
                "total": items.count(),
                "from": item_page.start_index(),
                "to": item_page.end_index(),
            },
            "message": self.message,
            "status": "ok",
        }

        return JsonResponse(response_data)
