from django.conf.urls import url
from echardemos import views

urlpatterns = [
    url(r'^$', views.line_chars),
]