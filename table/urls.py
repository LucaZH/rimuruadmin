
from django.contrib import admin
from django.urls import path
from table import views
urlpatterns = [
    path('user/', views.user_list),
    path('user/<int:pk>/', views.user_detail),
    path('cm/',views.centremedical_list),
    path('cm/<int:pk>',views.centremedical_detail),
    path('pharmacie/',views.pharmacie_list),
    path('pharmacie/<int:pk>',views.pharmacie_detail),
    path('conseil/',views.conseil_list),
    path('conseil/<int:pk>',views.conseil_detail),
]

