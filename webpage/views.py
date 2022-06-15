from django.shortcuts import render
from webpage.models import RoomData

# Create your views here.

def index(request):
    return render(request, "index.html")

def test(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_visits': num_visits,
    }

    return render(request, "test.html", context=context)

def room(request):
	# get room's name from form in index.html
	roomstr = request.GET.get('room')
	if not RoomData.objects.filter(roomname__iexact=roomstr):
		# set default values of room
		roomdata = RoomData(roomname=roomstr, minutes=25, seconds=0, message="HI")
		roomdata.save()
	roomdata = RoomData.objects.filter(roomname__iexact=roomstr)
	test_text = "hello"

	return render(request, "room.html", locals())