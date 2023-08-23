from django.urls import path
from .views import index, top_sellers, advertisement_post

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers/', top_sellers, name='top_sellers'),
    path('advertisement-post/', advertisement_post, name='adv_post'),
]
