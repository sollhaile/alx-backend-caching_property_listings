from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = list(Property.objects.all().values(
        'id', 'title', 'description', 'price', 'location', 'created_at'
    ))
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()

    return JsonResponse({"data": properties})
