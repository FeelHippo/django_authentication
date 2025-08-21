from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from client.customprovider.provider import CustomProvider

urlpatters = default_urlpatterns(CustomProvider)