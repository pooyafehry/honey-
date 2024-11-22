from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from user.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', home_page, name='home_page'),  # Map the home page
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path
from .views import register_view, test_view, category_list, category_detail, add_to_cart, remove_from_cart, cart_detail, continue_shopping

urlpatterns = [
    path('register/', register_view, name='register'),
    path('test/', test_view, name='test'),  # Define the `test` URL pattern
    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('continue-shopping/', continue_shopping, name='continue_shopping'),
]

