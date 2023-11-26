from . import views
from django.urls import path
app_name='college'

urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.allDepartments,name="allDepartments"),
    path('placeorder/',views.placeorder,name='placeorder'),
    path('get_courses/<str:department_name>/',views.get_courses,name='get_courses'),

    ]
