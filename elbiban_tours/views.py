from django.shortcuts import render,reverse
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login,get_user_model
from administration.models import Service,FeedBack,Voyage,GeneralInfo,LandingImage
from demand_handler.forms import (
								VisaForm, 
								VisaEtudeForm,
								HotelReservationForm,
								ContratDeTravailForm,
								CreditCardForm,
								ImmigrationForm,
								PlaneTicketForm,
								VoyageServiceForm,
								VoyageForm
								)

User = get_user_model()
def index(request):
	general_info	= GeneralInfo.objects.all().first()
	landing_image	= LandingImage.objects.filter(active=True).filter(is_for_about=False).first()
	visa_form 		= VisaForm()
	voyage_form		= VoyageForm()

	voyages			= Voyage.objects.all()
	
	feedbacks 		= FeedBack.objects.all() 
	services 		= Service.objects.all()
	services_1 		= services.filter(is_in_section_1=True)
	services_2 		= services.filter(is_in_landing=True).filter(is_in_section_1=False)
	context = {
		"landing_image"	:landing_image,
		"info"			:general_info,
		"services_1"	:services_1,
		"services_2"	:services_2,
		"feedbacks"		:feedbacks,
		"voyages"		:voyages,
		"visa_form"		:visa_form,
		"voyage_form"	:voyage_form


	}
	return render(request,"base.html",context)


def voyage_page(request):
	general_info	= GeneralInfo.objects.all().first()
	form 			= VoyageForm(request.POST or None)
	voyages 		= Voyage.objects.all()
	paginated 		= False
	if len(voyages) > 16 :
		page 			= request.GET.get('page') or 1
		paginated 		= True
		paginator 		= Paginator(voyages, 16)
		voyages 		= paginator.get_page(page)
	context 		= {
		"info":general_info,
		'voyages':voyages,
		'form':form,
		'is_paginated': paginated,
	}
	return render(request,'voyage/voyage.html',context)


def services_page(request):
	general_info						= GeneralInfo.objects.all().first()
	services_objects 					= Service.objects.all().filter(has_form=True)
	services_without_form				= Service.objects.all().filter(has_form=False)
	forms 								= {}
	forms["visa_demand"] 				= VisaForm(request.POST or None)
	forms["visa_etude_demand"]			= VisaEtudeForm(request.POST or None)
	forms["hotel_reservation_demand"]	= HotelReservationForm(request.POST or None)
	forms["contrat_travail_demand"]		= ContratDeTravailForm(request.POST or None)
	forms["credit_card_demand"]			= CreditCardForm(request.POST or None)
	forms["plane_ticket_demand"]		= PlaneTicketForm(request.POST or None)
	forms["voyage_demand"]				= VoyageServiceForm(request.POST or None)
	services 							= [ (service,forms[service.form],reverse(service.form)) for service in services_objects ]
	print(services_objects)
	
	context 				= {
		"info":general_info,
		"services" : services,
		"services_without_form" : services_without_form,
	}
	print(services_objects[1].get_end_point())

	return render(request,"services/services.html",context)


def about_page(request):
	landing_image			= LandingImage.objects.filter(active=True).filter(is_for_about=True).first()
	general_info			= GeneralInfo.objects.all().first()
	services 				= Service.objects.all().filter(is_on_about=True)[:8]
	context 				= {
		"landing_image":landing_image,
		"services":services,
		"info":general_info,
	}
	print(services)
	return render(request,"about/about.html",context)