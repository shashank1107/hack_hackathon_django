from django.urls import path

from demo import views

app_name = "demo"

urlpatterns = [
    # views
    path('', views.home_page_view, name='home-page'),

    # apis
    path('api/v1/configure-demo-app', views.configure_demo_app, name='api-v1-configure-demo-app'),
]
