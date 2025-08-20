from django.db import models

# Create your models here.
class Bono(models.Model):
    nombre = nombre = models.CharField(max_length=20,blank=True)
    descuento  = models.DecimalField(max_digits=5, decimal_places=2, default=0,null=True, blank=True)
    vencimiento = models.DateField()
    comentarios = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
    
import secrets
from django.db import models
from django.utils.timezone import now

ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  # sin O/0/I/1

def generate_ticket():
    yyyymm = now().strftime("%Y%m")
    rand = "".join(secrets.choice(ALPHABET) for _ in range(5))
    return f"L-{yyyymm}-{rand}"

class Lead(models.Model):
    ticket = models.CharField(
        max_length=20, unique=True, editable=False, db_index=True
    )
    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)
    empresa = models.CharField(max_length=120, blank=True)
    mensaje = models.TextField(blank=True)
    acepta_politica = models.BooleanField(default=False)

    source_url = models.URLField(blank=True)
    user_agent = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado"]

    def save(self, *args, **kwargs):
        if not self.ticket:
            # intenta generar un ticket único (muy baja probabilidad de colisión)
            for _ in range(5):
                cand = generate_ticket()
                if not Lead.objects.filter(ticket=cand).exists():
                    self.ticket = cand
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket} — {self.nombre} <{self.email}>"
