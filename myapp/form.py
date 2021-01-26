from django import forms
from myapp.models import Employee


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("fname", "lname", "oname", "eid", "mono", "email", "img")
