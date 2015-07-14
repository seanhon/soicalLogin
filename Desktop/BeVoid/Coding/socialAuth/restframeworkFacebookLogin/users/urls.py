from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    url(r'^register-by-token/(?P<backend>[^/]+)/$',
        views.register_by_access_token),
    url(r'^register-by-token/instagram/#$',
        views.register_by_access_token),

)
#292550279.d1bc49e.52ed986c4f6945ceabcb8d17bcb57d67