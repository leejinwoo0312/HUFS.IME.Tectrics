"""
URL configuration for Tectrics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from .views import Main
from Route.views import Road
from Load.views import BoxLoad, LoadData
from Box.views import BoxList
from Order.views import its
from Order.views import upload_file 
from Route.views import Map
from Login.views import Join
from Login.views import UserLogin
from Box.views import getbox
from django.conf.urls.static import static  
from django.conf import settings 
from Load.views import Index  
from Route.views import getmapbox
from Route.views import getaddress    #추가
from Box.views import BoxShow     # 추가




urlpatterns = [
    path("admin/", admin.site.urls),
    #path("",Main.as_view()),
    path("",UserLogin.as_view()),
    path("Route/road",Road.as_view()),
    path("Load/boxload",BoxLoad.as_view()),
    path("Box/boxlist",BoxList.as_view()),
    path('Route/map', Map.as_view()),
    path('upload/', upload_file, name='upload_file'),
    path("Order/itsdata",its.as_view()),
    path("Login/join",Join.as_view()),
    path("Login/userlogin",UserLogin.as_view()),
    path("getbox/",getbox,name='getbox'),
    path("Load/index",Index.as_view()),
    path('Load/loaddata',LoadData.as_view()),
    path("getmapbox/",getmapbox,name='getmapbox'),
    path("getaddress/",getaddress,name='getaddress'),   #추가
    path('Box/boxshow',BoxShow.as_view()),    # 추가
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 