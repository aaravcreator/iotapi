from django.urls import path,include
from .views import index,TestView,get_token,loginPage,logoutPage,register_user,SensorReading,changeLedStatus,LedStatus
from rest_framework.routers import DefaultRouter


app_name = 'dashboard'
router = DefaultRouter()

router.register(r'sensor',SensorReading,basename="sensor")
urlpatterns = [
    path('',index,name='index'),
    path('api/',include(router.urls)),
    # path("users",UserView.as_view(),name="test"),
    path("api/public",TestView.as_view(),name='test_view'),
    path("account/get_token",get_token,name="get-token"),
    path("login",loginPage,name="user-login"),
    path("logout",logoutPage,name="user-logout"),
    path("register",register_user,name="user-registration"),
    path("change_led_status",changeLedStatus,name="change_led_status"),
    path("api/get_led_status",LedStatus.as_view(),name="get-led-status"),
    # path("api/sensor",SensorReading.as_view(),name="sensor_readings")

]