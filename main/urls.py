from django.contrib.auth.decorators import login_required
from django.urls import path
from main.views import *

urlpatterns = [
    path('index/', login_required(Index.as_view()), name='index'),
    path('', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('contact/', Contact.as_view(), name='contact'),
    path('post/', Post.as_view(), name='post'),
    path('about/', About.as_view(), name='about'),
    path('addproducto/', AddProducto.as_view(), name='add_product'),
    path('add_imagen/<int:pk>/', upload_images, name='add_imagen'),
    path('Logout/', LogoutUser.as_view(), name='logout'),
]
