from django import forms

class MyForm(forms.Form):
    Username=forms.CharField(label="UserName",max_length=100)
    Password=forms.CharField(label="Password",max_length=100)
    PhoneNo=forms.IntegerField(label="Phone No")
    Address=forms.CharField(label="Address",max_length=100)