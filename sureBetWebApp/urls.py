from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name="mainpage"),
    path('login/', views.custom_login, name="login"),
    path('signUp/', views.signUp, name="signUp"),
    path('logout/', views.custom_logout, name='logout'),
    path('make_payment/', views.make_payment, name='make_payment'),
] 
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
