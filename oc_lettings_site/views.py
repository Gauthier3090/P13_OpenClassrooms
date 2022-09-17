from django.shortcuts import render
from .models import Letting, Profile


def index(request):
    return render(request, 'index.html')


def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    letting_object = Letting.objects.get(id=letting_id)
    context = {
        'title': letting_object.title,
        'address': letting_object.address,
    }
    return render(request, 'letting.html', context)


def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


def profile(request, username):
    profile_object = Profile.objects.get(user__username=username)
    context = {'profile': profile_object}
    return render(request, 'profile.html', context)
