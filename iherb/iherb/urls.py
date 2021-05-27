from django.urls import (
    path,
    include
)

urlpatterns = [
    path('to_csv', include('to_csv.urls'))
]
