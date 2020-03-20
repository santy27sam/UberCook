from django.urls import path,include
from .views import UpdateUserView, CreateUserView

urlpatterns = [
    
    path('useracc/<int:pk>/updateuser/', UpdateUserView.as_view(),name = 'update'),
    path('useracc/<int:pk>/new/', CreateUserView.as_view(), name = 'create'),
]