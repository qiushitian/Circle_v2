from django.urls import path
from home.views import Home, Explore, Contacts, Connector, Forum

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('home/explore', Explore.as_view(), name='explore'),
    path('home/contacts', Contacts.as_view(), name='contacts'),
    path('home/connector', Connector.as_view(), name='connector'),
    path('home/forum', Forum.as_view(), name='forum'),
]
