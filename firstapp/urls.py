
from . import views
from django.urls import path

urlpatterns = [
 path('home_page',views.home_page,name='home_page'),
 path('wayanad_page',views.wayanad_page,name='wayanad_page'),
 path('load_sample',views.load_sample,name='load_sample'),
 path('',views.load_add_page,name='load_add_page'),
 path('add_num',views.add_num,name='add_num'),
  path('add_product',views.add_product,name='add_product'),

]