from django.urls import path
from . import views
from .views import CustomersListView, CustomersCreateView, CustomersDetailView, CustomersUpdateView

urlpatterns = [
    path('', CustomersListView.as_view(), name='customers-home-page'),
    path('create_customer/', CustomersCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>/', CustomersDetailView.as_view(), name='customer-detail'),
    path('create/', CustomersCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>/update/', CustomersUpdateView.as_view(), name='customer-update'),
]
