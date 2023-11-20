from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails, Holidays, DoctorLeave
# Register your models here.


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(PatientDischargeDetails)
admin.site.register(Holidays)
admin.site.register(DoctorLeave)

