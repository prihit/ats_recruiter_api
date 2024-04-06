from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create_candidate, name='create_candidate'), #POST api for creating candidate. Data needs to be passed as request body payload
    path('candidate/<int:candidate_id>', views.get_candidate_data, name='get_candidate_data'), # get api used for testing candidate data
    path('candidate/<int:candidate_id>/update-status', views.update_candidate_status, name='update_candidate_status'), #PATCH api to update status for given candidate id
    path('candidate_search/', views.candidate_list, name='candidate-list'), # Get api to search/filter candidates on different fields. fields and value need to send as query parameters
    path('candidate_namesearch/', views.name_search, name='name-search'), # Get API for searching candidates by name and returning data in order of relevance
]