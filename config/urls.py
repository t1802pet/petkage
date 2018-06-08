"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from config.views import *

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

    url(r'^vaccine/', VaccineView.as_view(), name='vaccine'),
    url(r'^hospital/', HospitalView.as_view(), name='hospital'),

    url(r'^hospital_detail/', HospitalDetailView.as_view(), name='hospital_detail'),

    url(r'^hospital_notice/', HospitalNoticeView.as_view(), name='hospital_notice'),
    url(r'^hospital_reservation/', HospitalReservationView.as_view(), name='hospital_reservation'),

    url(r'^diary/', DiaryView.as_view(), name='diary'),

    url(r'^medical/', MedicalView.as_view(), name='medical'),

    # url(r'^accounts/', include('allauth.urls')),
]



urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)