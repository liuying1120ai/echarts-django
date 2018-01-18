from django.conf.urls import url
from echardemos import views

urlpatterns = [
    url(r'^linecharts/$', views.line_chars),
]