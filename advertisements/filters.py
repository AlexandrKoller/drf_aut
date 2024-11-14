from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # TODO: задайте требуемые фильтры
    created_at = filters.DateFromToRangeFilter()
    status = filters.CharFilter(field_name='status', lookup_expr='icontains')
    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
