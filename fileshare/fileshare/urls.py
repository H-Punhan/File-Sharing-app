
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',loginuser),
    path('logout/',logoutuser),
    path('add/',add),
    path('add/comment/<id>',addcomment),
    path('add/comment/shared/<id>',addcommentshared),
    path('read/<id>',read),
    path('delete/<id>',deletefile),
    path('update/<id>',update),
    path('delete/<postid>/comment/<id>',deletecomment),
    path('share/<fileid>',share),
    path('read/<user>/<fileid>',readshared),
    path('',index),
 
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
