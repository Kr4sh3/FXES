from django.urls import path
from . import views
from .views import TweetViewSet, UserViewSet, SearchTermViewSet

urlpatterns = [
    path("", views.index, name="index"),
    path("api/tweets", TweetViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("api/tweets/<str:pk>", TweetViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path("api/users", UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("api/users/<str:pk>", UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path("api/searchterms", SearchTermViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("api/searchterms/<str:pk>", SearchTermViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]