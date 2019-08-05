from django.db import models
from django.db.models import signals
from django.core.mail import send_mass_mail
from elbiban_tours.utilities import upload_image_path
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class LandingImage(models.Model):
	image 		= models.ImageField(upload_to=upload_image_path)
	active		= models.BooleanField(default=False)
	is_for_about= models.BooleanField(default=False)


class GeneralInfo(models.Model):
	landing_title_1 		= models.CharField(max_length=50)
	landing_title_2 		= models.CharField(max_length=50)
	phone_number			= models.DecimalField(max_digits=10,decimal_places=0)
	fax_number				= models.DecimalField(max_digits=9,decimal_places=0)
	email 					= models.EmailField()
	agency_description		= models.TextField()
	agency_detailed_desc	= models.TextField(default="frghana")
	location 				= models.CharField(max_length=100)
	facebook_link			= models.CharField(max_length=100)
	twitter_link			= models.CharField(max_length=100)
	instagram_link			= models.CharField(max_length=100)
	msg_confirmation		= models.CharField(max_length=250)



class Requirement(models.Model):
	designation 		= models.CharField(max_length=200)

	def __str__(self):
		return self.designation

class Service(models.Model):
	designation		= models.CharField(max_length=50)
	description		= models.TextField()
	is_in_landing	= models.BooleanField(default=False)
	svg				= models.FileField(upload_to=upload_image_path,null=True)
	requirements	= models.ManyToManyField(Requirement,related_name='service',null=True,blank=True)
	has_form 		= models.BooleanField(default=False)
	is_in_section_1 = models.BooleanField(default=False)
	is_on_about		= models.BooleanField(default=False)
	form 			= models.CharField(max_length=30,null=True,blank=True)

	def __str__(self):
		return self.designation

	def get_end_point(self):
		return reverse("requirements",kwargs={"pk":self.pk})


class FeedBack(models.Model):
	CLIENT_FIDELE = 'client fidèle'
	CLIENT_NEW	  = 'nouveau client'
	CLIENT_CHOICES = {
		(CLIENT_FIDELE,'client fidèle'),
		(CLIENT_NEW,'nouveau client')
	}
	user  			= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	image 			= models.ImageField(upload_to=upload_image_path)
	username		= models.CharField(max_length=50,blank=True,null=True)
	client_badge	= models.CharField(max_length=20,choices=CLIENT_CHOICES,default=CLIENT_NEW)
	feedback 		= models.TextField()
	def __str__(self):
		return self.username


class Voyage(models.Model):
	AVAILABLE	= 'Disponible'
	NOT_AVAILABLE 	= 'indisponible'
	AVAILABILITY 	= {
	(AVAILABLE,'disponible'),
	(NOT_AVAILABLE,'indisponible')
	}
	image		= models.ImageField(upload_to=upload_image_path)
	destination	= models.CharField(max_length=50)
	price		= models.DecimalField(max_digits=20,decimal_places=0)
	availability= models.CharField(max_length=20,choices=AVAILABILITY,default=AVAILABLE)
	timestamp	= models.DateField(auto_now_add=False)
	best		= models.BooleanField(default=False)
	dure 		= models.CharField(max_length=20,default="15 jours")

	def __str__(self):
		return self.destination

	def get_end_point(self):
		return reverse("voyage_demand",kwargs={"pk":self.pk})






class Message(models.Model):
	first_name		= models.CharField(max_length=20)
	last_name		= models.CharField(max_length=20)
	phone_number 	= models.DecimalField(max_digits=10,decimal_places=0)
	email 			= models.EmailField()
	content 		= models.TextField()
	timestamp		= models.DateField(auto_now_add=True)
	def __str__(self):
		return "{} {}".format(self.first_name,self.last_name)

class NewsLetter(models.Model):
	subject 			= models.CharField(max_length=200)
	message 			= models.TextField()

	def __str__(self):
		return self.subject


class NewsLetterMember(models.Model):
	email 				= models.EmailField()

	def __str__(self):
		return self.email



class TestModelKhra(models.Model):
	image 			= models.ImageField(upload_to=upload_image_path,null=True)









def send_newsletter(sender, instance, created, **kwargs):
	members					= NewsLetterMember.objects.all()
	sender_email 			= GeneralInfo.objects.all().first().email
	receivers_list 			= [ member.email for member in members ]
	data 					= (instance.subject,instance.message,sender_email,receivers_list)
	send_mass_mail((data,),fail_silently=False)




signals.post_save.connect(receiver=send_newsletter, sender=NewsLetter)