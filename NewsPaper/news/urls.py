from django.urls import path
from .views import NewsDetail, NewsList

urlpatterns = [
    path('<int:pk>', NewsDetail.as_view()),
    path('', NewsList.as_view())
]
