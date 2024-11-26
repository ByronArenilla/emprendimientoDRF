from django.urls import path
from emprende_app.api.views import RolesLista, RolesCrear
#from watchlist_app.api.views import movie_list, movie_details

urlpatterns = [
path('roles/', RolesLista.as_view(), name='roles-lista'),
path('roles/crear', RolesCrear.as_view(), name='roles-crear'),
]