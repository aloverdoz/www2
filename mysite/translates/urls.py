from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('translates/<int:translates_id>/', view_translates, name='view_translates'),
]