from django import forms

class StudentForm(forms.Form):
    sname = forms.CharField()
    spassword = forms.CharField()
    sage = forms.IntegerField()