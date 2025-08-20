from django.urls import path
from leads.views import HomeView
from leads.views import ContactoView, GraciasView
from leads.views import PrecioView

app_name='leads'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("contacto/", ContactoView.as_view(), name="contacto"),
    path("gracias/", GraciasView.as_view(), name="gracias"),
    path("precio/", PrecioView.as_view(), name="precio"),
]
