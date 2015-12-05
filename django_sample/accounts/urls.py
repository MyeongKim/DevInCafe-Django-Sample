from django.conf.urls import url, patterns

urlpatterns = patterns(
    'accounts.views',
    url(r'^login/$', 'login', name='login'),
)