from django.urls import path

from . import views

app_name = 'receitas'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/', views.category, name="categoria"),
    path('recipes/<int:id>/', views.recipe, name="receita"),
]
