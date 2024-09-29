from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('expense.urls')),
    path('api/v1/', include('earning.urls')),
    path('api/v1/', include('item.urls')),
    path('api/v1/', include('planner.urls')),
]
