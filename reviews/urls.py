from django.urls import path
from . import views
# Feedback/urls.py
from reviews.views import signup_view
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("Home", views.Home, name='Home'),
    path('', signup_view, name='Home'),  # Default route = Home page add kiya hai
    path("SignUp", views.SignUp, name='signup'),
    path("Products", views.Products, name="Products"),
    path('Products/<slug:slug>', views.about_product, name="About Product"),
    path("Login", views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('history', views.history, name='history')
]

handler404 = 'reviews.views.custom_404_view'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)