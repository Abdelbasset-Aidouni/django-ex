from django.contrib import admin
from .models import (
				LandingImage,
				GeneralInfo,
				Service,
				FeedBack,
				Voyage,
				
				Message,
				Requirement,
				NewsLetter,
				NewsLetterMember
				)


admin.site.register(LandingImage)

admin.site.register(Service)





admin.site.register(Requirement)
admin.site.register(NewsLetter)
admin.site.register(NewsLetterMember)

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display 	= ('username','client_badge')
    list_filter		= ('client_badge',)

@admin.register(Voyage)
class VoyageAdmin(admin.ModelAdmin):
    list_display 	= ('destination','price','availability','dure')
    list_filter		= ('availability',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display 	= ('first_name','last_name','phone_number','email','timestamp')
    list_filter		= ('timestamp',)


@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('phone_number','fax_number','email','location')