from django.urls import path
from .views import (
    CrawlingView
)

urlpatterns = [
    path('/crawling', CrawlingView.as_view())
]
