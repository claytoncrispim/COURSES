from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-5', 'rows': 5}), # "'rows': 5" was added by the model. I'm keeping it here for reference.
        }
        labels = {            
            'text': 'Write your thoughts here:'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        
        # Validating the user input using the word "Django" as an example
        # if 'Django' not in title:
        #     raise ValidationError("We only accept notes about Django!")
        return title