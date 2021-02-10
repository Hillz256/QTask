from django.urls import path

from quikTasks.views import *

urlpatterns = [

    path('', PoemListView.as_view(), name="task"),

    path('user/<str:username>/', UserPoemListView.as_view(), name="user-poems"),

    path('poem/add/', PoemCreateView.as_view(), name="create"),

    path('poem/detail/<int:pk>/', PoemDetailView.as_view(), name="detail"),

    path('poem/detail/<int:pk>/update/',
         PoemUpdateView.as_view(), name="poem-update"),

    path('poem/detail/<int:pk>/delete/',
         PoemDeleteView.as_view(), name="poem-delete"),

]
