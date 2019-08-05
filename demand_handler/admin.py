from django.contrib import admin
from .models import (
				Demand, 
				Visa,
				VisaEtude, 
				PlaneTicket,
				Hebergement,
				Immigration,
				CreditCard,
				ContratDeTravail,
				HotelReservation,
				VoyageDemand
				)
admin.site.register(Demand)



admin.site.register(Hebergement)
admin.site.register(Immigration)


@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
    list_display 	= ('first_name','last_name','phone_number','destination','etat')
    list_filter		= ('etat','destination')


@admin.register(VisaEtude)
class VisaEtudeAdmin(admin.ModelAdmin):
    list_display 	= ('first_name','last_name','phone_number','destination','country','etat')
    list_filter		= ('etat','country')

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display 	= ('first_name','last_name','phone_number','designation','etat')
    list_filter		= ('etat','designation')



@admin.register(HotelReservation)
class HotelReservationAdmin(admin.ModelAdmin):
    list_display 	= ('first_name','last_name','phone_number','location','etat')
    list_filter		= ('etat','location')

@admin.register(VoyageDemand)
class VoyageDemandAdmin(admin.ModelAdmin):
    list_display 	= ('first_name','last_name','phone_number','voyage','etat')
    list_filter		= ('etat','voyage')



@admin.register(PlaneTicket)
class PlaneTicketAdmin(admin.ModelAdmin):
    list_display 	= ('first_name','last_name','phone_number','destination','etat')
    list_filter		= ('destination','etat')

@admin.register(ContratDeTravail)
class ContratDeTravailAdmin(admin.ModelAdmin):
    list_display 	= ('first_name','last_name','phone_number','etat')
    list_filter		= ('etat',)

