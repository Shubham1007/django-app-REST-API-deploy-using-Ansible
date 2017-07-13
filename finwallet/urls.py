from django.conf.urls import include, url
from django.contrib import admin
from finwallet.utils import *


urlpatterns = [
    url(r'^$', homeView),
    url(r'^api', include('customers.urls')),
    url(r'^api', include('accounts.urls')),
    url(r'^api', include('transactions.urls')),
    url(r'^api', include('products.urls')),
    url(r'^api', include('orders.urls')),
    url(r'^', include('auths.urls')),
    url(r'^create-group/', create_finwallet_default_group),
    url(r'^admin/', include(admin.site.urls)),
]
