from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import recipe_create_list, recipe_retrieve_update_delete

urlpatterns = [
    path('recipes', recipe_create_list, name='recipe-create-list' ),
    path('recipes/<int:pk>', recipe_retrieve_update_delete, name='recipe-retrieve-update-delete'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_obtain_pair'),

]

