# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from offers_applications.models import Recruiter, Offer, Application


def index(request):#lists all offers
	all_offers=Offer.objects.all()
	context = Context({'all_offers_list': all_offers,})
	return render(request,'offers/index.html',context)


def show(request,offer_id):	#shows each offer
	offer=Offer.objects.get(id=offer_id)
	context=Context({'offer':offer})
	return render(request,'offers/details.html',context)


def apply(request,offer_id):	#apply for an application
	applicant_uid=1		#to be obtained from auth system
#poll tathya.iiserkol.ac.in, check that applicant satisfies all criteria for the Application
	newappl=Application(offer_id=offer_id)
	newappl.applicant_uid=applicant_uid
	newappl.save()
	return HttpResponse("Applicaton saved!")


def create(request):	#can get additonal parameters formed from url path here
	pass

	
