from django import forms
from .validators import validate_dot_com, validate_url 

class SubmitUrlForm(forms.Form):
    url=forms.CharField(label="submit your form ",validators=[validate_url,validate_dot_com])

    # def clean(self):
    #     cleaner_data= super(SubmitUrlForm,self).clean()
    #     print(cleaner_data)
    #     url=cleaner_data.get('url')

    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:

    #         raise forms.ValidationError("Invalid Url For the Field")
    #     return url
    #     #print(url)
      
