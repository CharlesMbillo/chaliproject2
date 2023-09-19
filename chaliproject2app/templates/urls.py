from django.urls import path
from django.contrib import admin


from chaliproject2app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
]
