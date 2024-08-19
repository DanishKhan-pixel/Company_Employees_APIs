
from django.contrib import admin
from django.urls import path, include
from .views import home_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1/',home_page ),
    path('api/v1',include('api.urls'))
]

#companies/{companyId}/employees