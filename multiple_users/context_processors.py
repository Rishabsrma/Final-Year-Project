from .models import Patient_Appointment

def get_notification(request):
    count = Patient_Appointment.objects.filter(accepted=False).count()
    data = {
        "count":count
    }
    return data