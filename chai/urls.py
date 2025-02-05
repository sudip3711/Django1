
from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_chai,name='all_chai'),
    path('<int:chaiId>/',views.chai_desc, name='chai_desc'),
]