from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.utils import timezone

class HomeView(TemplateView):
    template_name = "leads/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["year"] = timezone.now().year
        ctx["canonical"] = f"https://{self.request.get_host()}/"
        return ctx

from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from leads.forms import LeadForm
from leads.models import Lead

class ContactoView(FormView):
    template_name = "leads/contacto.html"
    form_class = LeadForm
    success_url = reverse_lazy("leads:gracias")

    def form_valid(self, form):
        req = self.request
        lead = Lead.objects.create(
            nombre=form.cleaned_data["nombre"],
            email=form.cleaned_data["email"],
            telefono=form.cleaned_data.get("telefono",""),
            empresa=form.cleaned_data.get("empresa",""),
            mensaje=form.cleaned_data.get("mensaje",""),
            acepta_politica=form.cleaned_data["acepta_politica"],
            source_url=req.build_absolute_uri(),
            user_agent=req.META.get("HTTP_USER_AGENT","")[:1000],
            ip_address=self._client_ip(),
        )
        # Notificación (SES)
        #try:
        #    send_mail(
        #        subject="Nuevo lead de Switchh (sitio)",
        #        message=f"{lead.nombre} <{lead.email}>\n{lead.telefono}\n{lead.empresa}\n\n{lead.mensaje}",
        #        from_email=None,  # usa DEFAULT_FROM_EMAIL
        #        recipient_list=["[email protected]"],
        #        fail_silently=True,
        #    )
        #except Exception:
        #    pass
        #messages.success(req, "¡Gracias! Te contactaremos muy pronto.")
        return super().form_valid(form)

    def _client_ip(self):
        xff = self.request.META.get("HTTP_X_FORWARDED_FOR")
        return xff.split(",")[0].strip() if xff else self.request.META.get("REMOTE_ADDR")

class GraciasView(TemplateView):
    template_name = "leads/gracias.html"

from django.views.generic import TemplateView

class PrecioView(TemplateView):
    template_name = "leads/precio.html"
