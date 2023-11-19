from django.contrib import admin
from main1.models import Home, About, service, contact_us
@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    list_display_links = ('title', 'sub_title')


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    list_display_links = ('title', 'sub_title')


@admin.register(service)
class service(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    list_display_links = ( 'title', 'sub_title')


@admin.register(contact_us)
class contact_us(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )