from django.shortcuts import render, redirect
from .forms import RoomForm

from .models import Room
# Create your views here.




def home(request):
    rooms = Room.objects.all()
    context ={"rooms":rooms}
    return render(request, 'base/home.html',context )

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room":room}
    return render(request, 'base/room.html',context)


def create_room(request):
    forms = RoomForm()
    if request.method=='POST':
        forms = RoomForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    context={"forms":forms}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    pass