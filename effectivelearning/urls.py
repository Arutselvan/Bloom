"""effectivelearning URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from utils import views as util_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^qa/', include('qa.urls')),
    url(r'^accounts/login', util_views.LoginPageView.as_view(), name='login_view'),
    url(r'^accounts/signup', util_views.SignupPageView.as_view(), name='signup_view'),
    url(r'^accounts/logout', util_views.portal_logout, name='logout_view'),
    url(r'^my_uploads', util_views.FileUploadsView.as_view(), name='file_upload_view'),
    url(r'^extract_info', util_views.ExtractInfoView.as_view(), name='extract_info_view'),
    url(r'^chat/', include('django_private_chat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
