from django.urls import path
from .views import index, top_sellers, advertisement_post, advertisement_detail

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers/', top_sellers, name='top_sellers'),
    path('advertisement-post/', advertisement_post, name='adv_post'),
    path('advertisement/<int:pk>', advertisement_detail, name='adv_detail')
]
