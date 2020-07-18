from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='main'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('<int:category_id>/products', 
views.products_by_cat, name='category'),
    path('<int:product_id>/product', views.product_single, name='product')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
