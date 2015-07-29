import json
try:
    from django.http import JsonResponse
    JSON_RESPONSE_AVAILABLE = True
except ImportError:
    from django.http import HttpResponse
    JSON_RESPONSE_AVAILABLE = False
from .api import youtube_search

YOUTUBE_RES_TYPES = ('video', 'channel', 'playlist')
YOUTUBE_MAX_RESULTS = 50
DEFAULT_MAX_RESULTS = 25

def search(request):
    search_term = request.GET.get('search_term', '')
    restype = request.GET.get('restype', 'video')
    max_results = request.GET.get('max_results', DEFAULT_MAX_RESULTS)

    try:
        max_results = int(max_results)
    except ValueError, TypeError:
        max_results = DEFAULT_MAX_RESULTS

    max_results = min(max_results, YOUTUBE_MAX_RESULTS)
    max_results = max(max_results, 0)

    result = youtube_search(search_term=search_term,
                            max_results=max_results)

    if restype and restype in YOUTUBE_RES_TYPES:
        restype = 'youtube#{}'.format(restype)
        result['items'] = filter(lambda x: x["id"]["kind"] == restype,
                                 result.get("items", []))

    if JSON_RESPONSE_AVAILABLE:
        return JsonResponse(result)

    return HttpResponse(json.dumps(result), mimetype='application/json')
