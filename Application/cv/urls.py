from django.urls import path

from cv import views

urlpatterns = [
    path('cv/', views.index, name='index')
    path('cv/', include('index.urls'))

]
