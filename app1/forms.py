from django import forms
from app1.models import emp

class empform(forms.ModelForm):
    class Meta:
        model=emp 
        fields=['eid','ename','esalary','eaddress','econtact']
