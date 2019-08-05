from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import VoyageDemand
from time import sleep
from administration.models import Voyage
from .forms import (
				VisaForm, 
				VisaEtudeForm,
				HotelReservationForm,
				ContratDeTravailForm,
				CreditCardForm,
				ImmigrationForm,
				PlaneTicketForm,
				VoyageForm,
				VoyageServiceForm,
				)



def visa_demand(request,pk=None):
	form = VisaForm(request.POST,request.FILES)
	if form.is_valid():
		print(form.cleaned_data)
		form.save()
		print("saved successfuly")
		return JsonResponse({},status=200)

	else:
		print(form)
		print("fail")
		return JsonResponse({},status=400)
	context = {
		"form":form
	}
	return render(request,'test.html',context)



def visa_etude_demand(request):
	form = VisaEtudeForm(request.POST,request.FILES)

	if form.is_valid():
		print(form.cleaned_data)
		form.save()

		return JsonResponse({},status=200)
	print(form.cleaned_data)
	return JsonResponse({},status=400)




def credit_card_demand(request):
	form = CreditCardForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		return JsonResponse({},status=200)
	print(form)
	print(form.errors)
	return JsonResponse({},status=400)



def immigration_demand(request):
	form = ImmigrationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return JsonResponse({},status=200)
	return JsonResponse({},status=400)



def voyage_demand(request,pk=None):
	if pk:
		form 			= VoyageForm(request.POST or None)
		if form.is_valid():
			form_data = form.cleaned_data
			obj = VoyageDemand(
					first_name=form_data.get("first_name"),
					last_name=form_data.get("last_name"),
					phone_number=form_data.get("phone_number"),
					voyage=get_object_or_404(Voyage,pk=pk)
				)
			obj.save()
			return JsonResponse({},status=200)
		return JsonResponse({},status=400)
	else:
		form 			= VoyageServiceForm(request.POST or None)
		if form.is_valid():
			form.save()
			return JsonResponse({},status=200)
		return JsonResponse({},status=400)




def plane_ticket_demand(request,pk=None):
	form = PlaneTicketForm(request.POST or None)

	if form.is_valid():
		form.save()
		# form_data = form.cleaned_data
		# obj = PlaneTicket(
		# 		first_name=form_data.get("first_name"),
		# 		last_name=form_data.get("last_name"),
		# 		phone_number=form_data.get("phone_number"),
		# 		destination=get_object_or_404(Voyage,pk=pk)
		# 	)
		# obj.save()
		return JsonResponse({},status=200)
	else:
		return JsonResponse({},status=400)

def contrat_travail_demand(request):
	form = ContratDeTravailForm(request.POST or None)
	if form.is_valid():
		form.save()
		return JsonResponse({},status=200)
	return JsonResponse({},status=400)

def hotel_reservation_demand(request):
	form = HotelReservationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return JsonResponse({},status=200)
	return JsonResponse({},status=400)




def send_demand(request):
	pass

