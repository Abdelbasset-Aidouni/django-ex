from django.urls import path,re_path
from . import views

urlpatterns = [
	path('contact/',views.message_handler,name='contact'),
	path('newsletter/',views.newsletter_subscribe,name='newsletter'),
	path('requirements/<int:pk>/',views.get_requirements,name='requirements'),
	path('test/',views.test, name="test"),
    
]