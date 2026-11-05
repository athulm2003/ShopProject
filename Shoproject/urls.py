from django.contrib import admin
from django.urls import path
from Myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('category/', CategoryListCreateView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view()),

   
    path('product/', ProductListCreateView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view()),

    path('category/<int:pk>/products/', ProductByCategoryView.as_view()),
]