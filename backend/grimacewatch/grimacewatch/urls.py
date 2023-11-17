from django.urls import include, path
from rest_framework import routers
from main import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('get-data/', views.ListTokens.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]