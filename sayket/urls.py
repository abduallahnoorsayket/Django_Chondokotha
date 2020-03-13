


from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from  .views  import search
from  .views import data,district



urlpatterns = [
    # path('admin/', admin.site.urls),
    path ("sayket/", search,name='index.html'),
    path('data/',data ),
    path('district/',district ),


]
