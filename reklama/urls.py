from django.urls import path
from .import views
app_name = 'reklama'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('elektronika/',views.elekrtonika,name = 'elekrtonika'),
    path('basgalar/',views.basgalar,name = 'basgalar'),
    path('details/<slug:slug>',views.details,name = 'details'),
]
