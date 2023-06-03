from django.urls import *
from .views import *


urlpatterns = [
	path('', index, name='index'),

	path('about/', about, name='about'),
	path('contact/', contact, name='contact'),
	path('course-detail/', course_detail, name='course-detail'),
	path('courses/', courses, name='courses'),
	path('events/', events, name='events'),
	path('pricing/', pricing, name='pricing'),
	path('trainers/', trainers, name='trainers'),
]
