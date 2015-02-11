from django.conf.urls import patterns, url

urlpatterns = patterns(
    'posts.views',
    url(r'^$', 'post_list_view', name='list'),
)
