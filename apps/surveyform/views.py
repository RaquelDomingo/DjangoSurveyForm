from django.shortcuts import render, redirect

# Create your views here.

# Index
def index(request):
    location = ['Washington DC', 'Seattle', 'Houston', 'LA', 'Mountain View', 'New York']
    language = ['Python', 'Ruby On Rails', 'LAMP', 'MEAN', 'Javascript', 'HTML/CSS']
    context = {
        'locations': location,
        'languages': language
    }
    return render(request, 'surveyform/index.html', context)

# Results
def result(request):
    if 'count' in request.session:
        request.session['count'] += 0
    else:
        request.session['count'] = 1
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
        'count': request.session['count']
    }
    return render(request, 'surveyform/result.html', context)

# form process
def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

