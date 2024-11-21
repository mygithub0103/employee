from django.urls import path
from . import views

urlpatterns = [
    path('add-employee/', views.add_employee, name='add_employee'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('add-employee/', views.add_employee, name='add_employee'),
    path('search-employee/', views.search_employee, name='search_employee'),  # مسار البحث
]
