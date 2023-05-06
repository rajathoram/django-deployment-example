from django.urls import path
from thirdapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('morning', views.good_morning_view),
    path('afternoon', views.good_afternoon_view),
    path('evening', views.good_evening_view),
    path('night', views.good_night_view),
]