from api import views
from django.urls import path
from api import urls


urlpatterns = [
    
    path('accounts/<int:account_id>/', views.get_account_details),
    path('process/', views.process_event),
    #path('callback/', views.auth_callback, name='auth_callback'),
    

]