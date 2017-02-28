from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from Website.models import EmailAddress, HeartRate
from django.template import RequestContext
from django.http import HttpResponseRedirect


def index(request):
#	latest_question_list = EmailAddress.objects.all()
	context = {}
	if request.user.is_authenticated():
		query = EmailAddress.objects.filter(email=request.user.email)
		if query.count() == 0:
			emailAddress = EmailAddress(email = request.user.email)
			emailAddress.save()
		else:
			emailAddress = query[0]
			
		context = {'username':request.user.get_username(),
				   'first_name':request.user.first_name,
				   'last_name':request.user.last_name,
				   'email':request.user.email,
				   'last_login':request.user.last_login,
				   'date_joined':request.user.date_joined,
				   'address':emailAddress.address,
				   'telephone':emailAddress.phone_number,
				   'comments':emailAddress.comments,
				   'imageData':emailAddress.imageData}
		
		return render(request, 'index.html', context)
	else:
		return HttpResponseRedirect('/accounts/login/')

def profile(request):
#	email = EmailAddress.objects.filter(email="")
	context = {}
	if request.method == 'POST':

		# process the data in form.cleaned_data as required
		# ...
		# redirect to a new URL:
		query = User.objects.filter(email=request.user.email)
	
		user = query[0]
		user.first_name = request.POST.get('first_name', '')
		user.last_name = request.POST.get('last_name', '')
		user.save()
		
		query = EmailAddress.objects.filter(email=request.user.email)
		
		if query.count() == 0:
			emailAddress = EmailAddress(email = request.user.email, address = request.POST.get('address', ''), phone_number = request.POST.get('telephone', ''), comments = request.POST.get('comments', ''))
			emailAddress.save()
		else:
			emailAddress = query[0]
			emailAddress.address = request.POST.get('address', '')
			emailAddress.phone_number = request.POST.get('telephone', '')
			emailAddress.comments = request.POST.get('comments', '')
			
			try:
				f = request.FILES['picture']
				with open('Website/static/'+request.user.email+'.jpeg', 'wb+') as destination:
					for chunk in f.chunks():
						destination.write(chunk)
			except:
				pass

			emailAddress.save()

		return HttpResponseRedirect('/')
	
	if request.user.is_authenticated():
		query = EmailAddress.objects.filter(email=request.user.email)
		if query.count() == 0:
			emailAddress = EmailAddress(email = request.user.email)
			emailAddress.save()
		else:
			emailAddress = query[0]
			
		context = {'username':request.user.get_username(),
				   'first_name':request.user.first_name,
				   'last_name':request.user.last_name,
				   'email':request.user.email,
				   'last_login':request.user.last_login,
				   'date_joined':request.user.date_joined,
				   'address':emailAddress.address,
				   'telephone':emailAddress.phone_number,
				   'comments':emailAddress.comments}
		
		return render(request, 'profile.html', context)
	else:
		return HttpResponseRedirect('/accounts/login/')