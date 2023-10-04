from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('hello', views.showhello , name='hello'),
    path('detail/<id_p>/', views.detail, name='detail'),
    path('delete/<id_p>/', views.delete,name='delete'),
    path('create/', views.create, name='create'),
    path('create2/', views.create2, name='create2'),
    path('update/<int:id_p>', views.update, name='update'),
    path('person2', views.showperson2, name='showperson2'),
    path('dperson2/<int:id_p>', views.dperson2,name='dperson2'),
    path('p2delete/<int:id_p>', views.p2delete,name='p2delete'),
    path('p2update/<int:id_p>', views.p2update,name='p2update'),
]
