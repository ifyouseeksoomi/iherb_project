from django.urls import path
from .views import (
    CrawlingView,
    OneCrawlingView
)

urlpatterns = [
    path('/crawling', CrawlingView.as_view()),
    path('/one_crawling', OneCrawlingView.as_view())
]
