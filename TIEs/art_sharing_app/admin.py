from django.contrib import admin
from .models import Artwork, ArtworkComment, Like, Userprofile, Event, TiesLogo

# Register your models here.
@admin.register(Artwork)
class TIEs_admin(admin.ModelAdmin):
    list_display=(
        "titre",
        "image",
        "user",
        "created_at",
    )
    list_editable = ()
    list_display_links = ()



@admin.register(Userprofile)
class Profiles(admin.ModelAdmin):
    list_display=(
        "user",
        "image",
        "bio",
        "premium",
        'num_like',
    )

@admin.register(Event)
class Evenements(admin.ModelAdmin):
    list_display=(
        "image",
        "theme"
    )

@admin.register(TiesLogo)
class Logo(admin.ModelAdmin):
    list_display= (
        "name",
        "profile",
    )
    
