from django.contrib import admin
from django.urls import path

from mysessions.views import cookie_delete, cookie_session, create_session, access_session, delete_session

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testcookie/', cookie_session),
    path('deletecookie/', cookie_delete),
    path('create/', create_session),
    path('access/', access_session),
    path('delete/', delete_session)
]
