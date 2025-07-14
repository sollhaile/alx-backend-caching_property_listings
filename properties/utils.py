from django.core.cache import cache
from .models import Property

def get_all_properties():
    all_properties = cache.get('all_properties')
    if all_properties is None:
        all_properties = list(Property.objects.all().values(
            'id', 'title', 'description', 'price', 'location', 'created_at'
        ))
        cache.set('all_properties', all_properties, 3600)  # cache 1 hour
    return all_properties
import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    try:
        conn = get_redis_connection("default")
        info = conn.info()
        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses

        hit_ratio = (hits / total_requests) if total_requests > 0 else 0

        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": round(hit_ratio, 2)
        }

        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics

    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "hit_ratio": 0
        }
