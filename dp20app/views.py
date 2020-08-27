from django.shortcuts import render
from django.http import HttpResponse
from dp20app import utilities
from dp20app import forms

#whats new: importing validators and also using builtin and custom validators in the form to check fields

def home(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)
        if form.is_valid()==False:
            return render(request,"dp20app/sample.html",{'form':form})
        else:
            data=form.cleaned_data
            propic=data['propic']
            utilities.storeimage(propic)
            print(form.cleaned_data)
    form=forms.SampleForm()
    return render(request,"dp20app/sample.html",{'form':form})
