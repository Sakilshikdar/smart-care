from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvilableTime
# Create your models here.

APPOINTMENT_TYPE = [
    ('Online', 'Online'),
    ('Offline', 'Offline'),
]

APPOINTMENT_STATUS = [
    ('Pending', 'Pending'),
    ('Running', 'Running'),
    ('Completed', 'Completed'),
]


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    symptom = models.TextField()
    appointment_type = models.CharField(
        choices=APPOINTMENT_TYPE, max_length=10)
    appointment_status = models.CharField(
        choices=APPOINTMENT_STATUS, max_length=10, default='Pending')
    time = models.OneToOneField(
        AvilableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f'Patient: {self.patient.user.first_name}  Doctor: {self.doctor.user.first_name}'
