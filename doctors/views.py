from django.shortcuts import render


def doctors(request):
    return render(request, 'doctors.html')


def appointments(request):
    return render(request, 'appointments.html')
