from django.urls import path
from .views import RefList, RefDetail, RefCreate, RefUpdate, RefDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
  path('register/', RegisterPage.as_view(), name='register'),

  path('', RefList.as_view(), name='refs'),  
  path('ref/<int:pk>', RefDetail.as_view(), name='ref'),
  path('ref-create/', RefCreate.as_view(), name='ref-create'),
  path('ref-update/<int:pk>', RefUpdate.as_view(), name='ref-update'),
  path('ref-delete/<int:pk>', RefDelete.as_view(), name='ref-delete'),
]

