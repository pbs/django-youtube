from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^youtube-api/search/$',
        'youtube.views.search', name='search'),
)
