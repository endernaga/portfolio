from django.conf.urls.static import static
from django.urls import path

from portfolio import settings
from portfolio_project.views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('products/<str:slug>/', DetailPage.as_view(), name='detail'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('auth/', LoginUser.as_view(), name='auth'),
    path('logoutRequest/', userLogout, name='logout'),
    path('logout/', logoutRequest, name='userlogout'),
    path('categories/<str:slug>', PageByCategories.as_view(), name='categories'),
    path('tag/<str:slug>', PageByTags.as_view(), name='tags')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)