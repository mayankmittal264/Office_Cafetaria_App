from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Employee
from myapp.form import EmpForm
import datetime

# Create your views here.


def webpage(request, *args):
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        oname = request.POST.get('oname', '')
        eid = request.POST.get('eid', '')
        mono = request.POST.get('mono', '')
        email = request.POST.get('email', '')
        img = request.FILES.getlist('img')
        emp = EmpForm(data=request.POST, files=request.FILES)
        if emp.is_valid():
            emp.save()
            regid = Employee.objects.get(eid=eid).regid
            regdate=Employee.get_regdate(Employee.objects.get(eid=eid))
            frmtdate = regdate.strftime("%Y-%m-%d")
            registration_data = {
                'message': "Employee Registration is successful. Press Ok to continue",
                'Regid': regid,
                'Regdate': frmtdate,
            }
            return render(request, "confirm.html", registration_data)
        else:
            return render(request, "Error.html")

    return render(request, "webpage.html")
