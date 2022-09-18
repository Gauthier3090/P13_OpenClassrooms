from django.shortcuts import render
from lettings.models import Letting


def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    letting_object = Letting.objects.get(id=letting_id)
    context = {
        'title': letting_object.title,
        'address': letting_object.address,
    }
    return render(request, 'lettings/letting.html', context)
