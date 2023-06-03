from django.shortcuts import render


def index(request):
	return render(
		request, 'index.html'
	)

def about(request):
	return render(
		request, 'about.html'
	)

def contact(request):
	return render(
		request, 'contact.html'
	)

def courses(request):
	return render(
		request, 'courses.html'
	)

def events(request):
	return render(
		request, 'events.html'
	)

def pricing(request):
	return render(
		request, 'pricing.html'
	)

def trainers(request):
	return render(
		request, 'trainers.html'
	)

def course_detail(request):
	return render(
		request, 'course-detail.html'
	)
