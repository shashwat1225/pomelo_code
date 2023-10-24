from api import views
from django.urls import path
from api import urls


urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/<int:account_id>/', views.get_account_details),
    path('process/', views.process_event)

]