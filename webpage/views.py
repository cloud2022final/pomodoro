from django.shortcuts import render

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