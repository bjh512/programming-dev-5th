"""programming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views
from pokemon import views as pokemon_views
from post import views as post_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list),
    url(r'^sum2/(?P<x>[\d/]+)/$',views.mysum2),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
	url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
	url(r'^sum/(?P<x>\d+)/$', views.mysum),
    url(r'^pokemon/$', pokemon_views.pokemon_list),
    url(r'^human/$', pokemon_views.human_list),
    url(r'^catch/$', pokemon_views.catch_list),
    url(r'^post/$',post_views.post_list)
]