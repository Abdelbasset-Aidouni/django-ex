from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from .forms import MessageForm,NewsLetterForm,TestFormKhra
from .models import Requirement


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Requirement):
            return str(obj)
        return super().default(obj)



def message_handler(request):
	msg_form		= MessageForm(request.POST or None)
	if msg_form.is_valid():
		msg_form.save()
		return JsonResponse({},status=200)
	else:
		return JsonResponse({},status=400)
	

def newsletter_subscribe(request):
	newsletter_form = NewsLetterForm(request.POST or None)
	if newsletter_form.is_valid():
		newsletter_form.save()
		return JsonResponse({},status=200)
	else:
		return JsonResponse({},status=400)


def get_requirements(request,pk):
	qs 		= Requirement.objects.filter(service__id=pk)
	
	data = [{"designation":obj.designation} for obj in qs ]
	print(data)
	return JsonResponse(data,safe=False)



def test(request):
	print(request.POST)
	form = TestFormKhra(request.POST or None)
	if form.is_valid():
		form.save()
		print(form)
		return JsonResponse({},status=200)
	print(form)
	return JsonResponse({"msg": "rak g3artha"},status=400)
	return render(request,'test.html',{"form",form})










