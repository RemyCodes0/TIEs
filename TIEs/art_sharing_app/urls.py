from django.urls import path
from .views import home, discussions, zoom, comments, staff, modifier_profile, ranking, like_artwork, profile,add_artwork, post_artwork, event, publish_event, current_event

urlpatterns = [
    path("", home, name= 'home' ),
    path('zoom/<int:artwork_id>/', zoom, name= 'zoom'),
    path("discussions/", discussions, name= 'discussions' ),
    path("ranking/", ranking, name= "ranking"), # type: ignore
    path("profile/<int:user_id>/", profile, name= 'profile' ),
    path("post_artwork/", post_artwork, name= "post_artwork"),
    path('events/', event, name="event"),
    path('like/<int:artwork_id>/', like_artwork, name="like_artwork"),
    path('publish_event/', publish_event, name= 'publish_event'),
    path('current_event/', current_event, name='current_event'),
    path('add_artwork/', add_artwork, name='add_artwork'),
    path('comment/<int:artwork_id>/', comments, name= 'comments'), 
    path("modifier_profile/<int:user_id>", modifier_profile, name="modifier_profile"),
    path("created_by/", staff, name="created_by")
]
