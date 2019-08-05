from django import forms
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
				VoyageDemand,
				)
class DemandForm(forms.ModelForm):
    class Meta:
        model 		= Demand
        fields 		= ('first_name','last_name','phone_number')
        labels 		= {
        	"first_name"	:'Nom',
        	"last_name"		:'Prénom',
        	"phone_number"	:'Numéro Téléphone',
        }


class VisaForm(DemandForm):
	class Meta:
		model 					= Visa
		fields 					= DemandForm.Meta.fields + ('passport','destination') 
		labels 					= DemandForm.Meta.labels
		labels["passport"]		= 'Passport Scané'
		labels["destination"]	= 'Pays'

class VisaEtudeForm(VisaForm):
	class Meta:
		model 					= VisaEtude
		fields 					= DemandForm.Meta.fields + ('country','passport') 
		labels 					= DemandForm.Meta.labels
		labels["country"]		= 'Pays'
		labels["passport"]		= 'Passport Scané'

class CreditCardForm(DemandForm):
	class Meta:
		model 					= CreditCard
		fields 					= DemandForm.Meta.fields + ('passport','designation') 
		labels 					= DemandForm.Meta.labels
		labels["passport"]		= 'Passport Scané'
		labels["designation"]	= 'Type'


class ImmigrationForm(DemandForm):
	class Meta:
		model 		= Immigration
		fields 		= DemandForm.Meta.fields + ('country',) 


class PlaneTicketForm(DemandForm):
	class Meta:
		model 		= PlaneTicket
		fields 		= DemandForm.Meta.fields + ('destination',)
		labels 		= DemandForm.Meta.labels

class VoyageForm(DemandForm):
	class Meta:
		model 		= VoyageDemand
		fields 		= DemandForm.Meta.fields
		labels 		= DemandForm.Meta.labels

class VoyageServiceForm(DemandForm):
	class Meta:
		model 		= VoyageDemand
		fields 		= DemandForm.Meta.fields + ('voyage',)
		labels 		= DemandForm.Meta.labels


class ContratDeTravailForm(DemandForm):
	class Meta:
		model 		= ContratDeTravail
		fields 		= DemandForm.Meta.fields 
		labels 		= DemandForm.Meta.labels

class HotelReservationForm(DemandForm):
	class Meta:
		model 					= HotelReservation
		fields 					= DemandForm.Meta.fields + ('location',) 
		labels 					= DemandForm.Meta.labels
		labels["location"]		= 'Emplacement'