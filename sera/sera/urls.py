from django.contrib import admin
from django.urls import path
from Myapp import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculate_churn_rate,name="calculate_churn_rate")
]
