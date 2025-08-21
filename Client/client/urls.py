from django.contrib import admin
from django.urls import path, re_path, include
from client.views.profile import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^accounts/profile$', ProfileView.as_view()),
]
