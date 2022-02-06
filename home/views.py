from django.shortcuts import render
from django.views import View
# Create your views here.


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/home.html')


class Explore(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/explore.html')


class Contacts(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/contactshtml')


class Connector(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/connector.html')


class Forum(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'social/post_list.html')
