from django.conf.urls import include, url
from django.contrib import admin
from .views import home,signIn,signUp,resetPassword,\
    createPassword,dashboard


urlpatterns = [
    url('admin/', include(admin.site.urls)),

    url(r'^signIn/$',signIn,name="signIn"),
    url(r'^signUp/$',signUp,name="signUp"),
    url(r'^resetPassword/$',resetPassword,name="resetPassword"),
    url(r'^createPassword/$',createPassword,name="createPassword"),
    url(r'^dashboard/$',dashboard,name="dashboard"),
    url(r'^',home,name="home")
]