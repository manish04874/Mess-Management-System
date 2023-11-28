from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("feedback/", views.feedback, name="feedback"),
    path("myticket/", views.myticket, name="myticket"),
    path("profile/<str:pk>/", views.userProfile, name="user-profile"),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('mealss/', views.mealss, name='mealss'),
    path('<int:pk>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('buy_meal/<int:category_id>/', views.buy_meal, name='buy_meal'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
