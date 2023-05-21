from django import forms

class RegisterForm(forms.Form):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "MonAutreChamp"
        
        fname = forms.CharField(label='First Name', max_length=100)
        lname = forms.CharField(label='Last Name', max_length=100)
        email = forms.EmailField(label='Email')
        phone = forms.CharField(label='Phone Number', max_length=100)
        age = forms.IntegerField(label='Age')
        zip = forms.CharField(label='Zipcode', max_length=100)
    
    
    
    #to be continued