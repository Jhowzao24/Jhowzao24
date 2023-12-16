from django.db import models

# Create your models here.

Instruments = (
    (0, 'Violin'),
    (1, 'Viola'),
    (2, 'Cello')
)

class RegisterClasses(models.Model):
    FullName = models.CharField(max_length=150, blank=True, null=True)
    Age = models.IntegerField(default=0)
    ResidencePhone = models.CharField(max_length=20, blank=True, null=True)
    WhatsApp = models.CharField(max_length=55, blank=True, null=True)
    Adress = models.TextField(max_length=300, blank=True, null=True)
    SelfDescription = models.TextField(max_length=450, blank=True, null=True)
    InstrumentChoice = models.IntegerField(choices=Instruments, default=2)
    DateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FullName