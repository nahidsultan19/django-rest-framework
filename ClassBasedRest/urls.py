from django.urls import path
# from .views import BookApiView, BookApiDetail
# # from . import views
# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('', BookApiView.as_view()),
#     path('detail/<str:pk>/', BookApiDetail.as_view())
#     # path('', views.BookApiView)
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

from .views import BookViewSet

urlpatterns = [
    path('', BookViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('books/<str:pk>', BookViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
