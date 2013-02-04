# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from offers_applications.models import Recruiter, Offer, Application


def index(request):#lists all offers
	all_offers=Offer.objects.all()
	template = loader.get_template('offers/index.html')
	context = Context({'all_offers_list': all_offers,
			    })
	return HttpResponse(template.render(context))


def create(request):	#can get additonal parameters formed from url path here
	pass

	
