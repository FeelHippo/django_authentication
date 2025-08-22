from django.contrib import admin
from django.urls import path, include, re_path
from oauth2_provider import urls as oauth2_urls
from server.views.main import profile

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [

    # OAuth2 server URLs
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # Logged-in user profile endpoint
    re_path(r'^profile/$', profile),

    # Redirect route
    re_path(r'^accounts/', include('django.contrib.auth.urls')),

]
