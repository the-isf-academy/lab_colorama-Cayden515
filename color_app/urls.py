from django.urls import path
from color_app import views


app_name = "color_app"
urlpatterns = [
    path('', views.home_view, name="index"),
    path('random/', views.random_color_view, name="random_color")
    path('color_app/'), views.ColorListView, name="color_list"
]

