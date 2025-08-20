from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    # website = forms.CharField(required=False, widget=forms.HiddenInput)  # honeypot

    class Meta:
        model = Lead
        fields = ["nombre", "email", "telefono", "empresa", "mensaje", "acepta_politica"]
        widgets = {
            "nombre":   forms.TextInput(attrs={"class": "mt-1 w-full rounded-xl border border-brand-gray/40 px-4 py-2", "placeholder": "Tu nombre"}),
            "email":    forms.EmailInput(attrs={"class": "mt-1 w-full rounded-xl border border-brand-gray/40 px-4 py-2", "placeholder": "[email protected]"}),
            "telefono": forms.TextInput(attrs={"class": "mt-1 w-full rounded-xl border border-brand-gray/40 px-4 py-2"}),
            "empresa":  forms.TextInput(attrs={"class": "mt-1 w-full rounded-xl border border-brand-gray/40 px-4 py-2"}),
            "mensaje":  forms.Textarea(attrs={"rows": 4, "class": "mt-1 w-full rounded-xl border border-brand-gray/40 px-4 py-2"}),
        }

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("website"):
            raise forms.ValidationError("Spam detectado.")
        if not cleaned.get("acepta_politica"):
            self.add_error("acepta_politica", "Debes aceptar la política de privacidad.")
        return cleaned
