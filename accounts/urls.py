from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^login$', 'accounts.views.persona_login', name = 'persona_login'),
)
