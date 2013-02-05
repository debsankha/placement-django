from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from offers_applications import offer_views
from offers_applications.models import *


#url(regex, view func, name) Dunno still what the 'name' is for


#/offers/REGEX matches to func's we attach here
urlpatterns = patterns('',
#    url(r'^$', offer_views.index, name='listing'),
	url(r'^$',
		ListView.as_view(
			queryset=Offer.objects.all(),
			context_object_name='all_offers_list',
			template_name='offers/index.html'),
		name='index'),


	url(r'^(?P<pk>\d+)/$',
		DetailView.as_view(
			model=Offer,
			template_name='offers/details.html'),
		name='details'),

	url(r'^(?P<offer_id>\d+)/apply$', offer_views.apply, name='apply'),
	url(r'^', offer_views.create, name=''),

#Examples of more #urlpatterns:
    #url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)

