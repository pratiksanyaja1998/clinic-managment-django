from django.db import models
from django.contrib.auth import get_user_model
from patients.models import Patients


class Doctors(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='doctors_user')

    is_accepted = models.BooleanField(default=None, null=True)
    # total member allow to with us
    total_person = models.IntegerField(default=1, error_messages={"blank": "Total person field may not be blank.",
                                                                  "required": "Total person is required."})
    # if mail has been send invited is true , so user can track witch contacts is invited
    is_invited = models.BooleanField(default=None, null=True)
    is_ticket = models.BooleanField(default=False, null=False)
    # ticket id
    token = models.CharField(max_length=30, unique=True)
    invite_type = models.CharField(max_length=6, default=None, null=True)

    def __str__(self):
        return str(self.user.username)


class Appointments(models.Model):

    patients = models.ForeignKey(Patients, on_delete=models.CASCADE, related_name='appointments_patients')
    doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='appointments_doctors')
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(null=True, blank=True)
    is_accepted = models.BooleanField(default=None, null=True)

    def __str__(self):
        return str(self.user.username)