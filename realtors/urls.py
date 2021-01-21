from django.urls import path
from .views import RealtorsListView, RealtorsView, TopSellerView
urlpatterns = [
    path('', RealtorsListView.as_view()),
    path('TopSeller/', TopSellerView.as_view()),
    path('<pk>', RealtorsView.as_view()),
]