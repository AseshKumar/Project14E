"""project14 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app14 import views
from project14 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ShowIndex,name="main"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('view_admin_login/',views.view_admin_login,name="view_admin_login"),
    path('view_product/',views.view_product,name="view_product"),
    path('save_product/',views.save_product,name="save_product"),
    path('user_register/',views.user_register,name="user_register"),
    path('new_register/',views.new_register,name="new_register"),
    path('user_login/',views.user_login,name="user_login"),
    path('save_login/',views.save_login,name="save_login"),
    path('view_use/',views.show_user,name="show_user"),
    path('forgot_user/',views.forgot_user,name="forgot_user"),
    path('Save_details/',views.Save_details,name="Save_details"),
    path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
    path('iteams_cart/',views.iteams_cart,name="iteams_cart"),
    path('del_cart/',views.del_cart,name="del_cart"),

    path('change_password/',views.change_password,name="change_password"),
    path('new_password/',views.new_password,name="new_password"),
    path('update_product/',views.update_product,name="update_product"),
    path('delete/',views.delete,name="delete"),
    path('update/',views.update,name="update"),
    path('in_cart/',views.in_cart,name="in_cart")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
