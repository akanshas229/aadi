from rest_framework.routers import DefaultRouter
from aadi_app.views import UserViewSet, AuthTokenViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'auth-tokens', AuthTokenViewSet)

urlpatterns = router.urls



# from . import views
# from django.urls import path

# urlpatterns = [

#     path('user_list/', views.user_list, name='user-list'),
#     path('user_detail/<int:pk>/', views.user_detail, name='user-detail'),
#     path('user_create/', views.user_create, name='user-create'),
#     path('user_update/<int:pk>/', views.user_update, name='user-update'),
#     path('user_delete/<int:pk>/', views.user_delete, name='user-delete'),
    
# ]

