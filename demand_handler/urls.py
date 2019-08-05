from django.urls import path,re_path
from .views import (
			visa_demand,
			visa_etude_demand,
			contrat_travail_demand,
			hotel_reservation_demand,
			immigration_demand,
			credit_card_demand,
			plane_ticket_demand,
			voyage_demand
			)

urlpatterns = [
	path('visa/', visa_demand,name='visa_demand'),
	path('visa-etude/', visa_etude_demand,name='visa_etude_demand'),
	path('contrat-de-travail/', contrat_travail_demand,name='contrat_travail_demand'),
	path('hotel-reservation/', hotel_reservation_demand,name='hotel_reservation_demand'),
	path('immigration/', immigration_demand,name='immigration_demand'),
	path('plane-ticket/', plane_ticket_demand,name='plane_ticket_demand'),
	re_path(r'^voyage/(?P<pk>\d+)/$', voyage_demand,name="voyage_demand"),
	path('voyage/', voyage_demand,name="voyage_demand"),
	path('credit-card/', credit_card_demand,name='credit_card_demand'),
	
    
]