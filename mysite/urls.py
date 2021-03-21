
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from main.views import home,category_list,brand_list,product_list,category_product_list,brand_product_list,product_detail




urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', home),
    path( 'category-list', category_list,name='category-list' ),
    path( 'brand-list', brand_list,name='brand-list' ),
    path( 'product-list', product_list,name='product-list'),
    path( 'category-product-list/<int:cat_id>', category_product_list,name='category-product-list'),
    path( 'brand-product-list/<int:brand_id>', brand_product_list,name='brand-product-list'),
    path('product/<str:slug>/<int:id>',product_detail,name='product_detail'),

]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)