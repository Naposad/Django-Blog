from django import forms


class Contact(forms.Form):
    Name = forms.CharField(min_length=5)
    Email = forms.EmailField()
    Subject = forms.CharField()
    Massegs = forms.CharField(widget=forms.Textarea())


