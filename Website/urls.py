from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]