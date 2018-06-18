
'''
from . import views

urlpatterns = [
    url('', views.home, name='home'),
    url('github/', views.github, name='github'),
    url('github/client/', views.github_client, name='github_client'),
    url('oxford/', views.oxford, name='oxford'),
]
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^github', views.github, name='github'),
    url(r'^github/client', views.github_client, name='github_client'),
]