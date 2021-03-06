# -*- coding: utf-8 -*-

### coellection(django) ###
### GNU/GPL v2
### Author: Cody Rocker
### Author_email: cody.rocker.83@gmail.com
### 2016
#-----------------------------------
#   Requires:                    """
#    - xlrd 0.9.4                """
#    - Django 1.9.3              """
#-----------------------------------
"""coellection URL Configuration

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
from django.conf.urls import *

from .views import HomeView, GameDetail, GameIndex, GameFilter, \
    PlatformDetail, PlatformIndex, AmiiboDetail, AmiiboIndex, search

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='coellection'),
    url(r'^games/$', GameIndex.as_view(), name='games'),
    url(r'^games/(?P<arg>[\D])/$', GameFilter.as_view(), name='filter_alpha'),
    url(r'^games/(?P<platform>[-\w]+)/$', GameFilter.as_view(), name='filter_games'),
    url(r'^game/(?P<slug>[-\w]+)/$', GameDetail.as_view(), name='game'),
    url(r'^platforms/$', PlatformIndex.as_view(), name='platforms'),
    url(r'^platform/(?P<slug>[-\w]+)/$', PlatformDetail.as_view(), name='platform'),
    url(r'^amiibos/$', AmiiboIndex.as_view(), name='amiibos'),
    url(r'^amiibo/(?P<slug>[-\w]+)/$', AmiiboDetail.as_view(), name='amiibo'),
    url(r'^search/$', search),
]