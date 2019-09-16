from django.urls import path
from people import views

urlpatterns = [
    path('people/', views.people_list),
]
