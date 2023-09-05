from core.models import Tag
from django.db.models import Count
from django.utils import timezone


def get_tags_by_country(country: str) -> list[Tag]:
    end_date = timezone.now()
    start_date = timezone.now() - timezone.timedelta(days=1)
    tags = (
        Tag.objects.filter(
            tweet__author__country=country,
            tweet__created_at__gt=start_date,
            tweet__created_at__lt=end_date,
        )
        .annotate(tweets_count=Count("tweet"))
        .order_by("-tweets_count", "name")[:10]
    )
    return tags
