from django import forms
from django.core.exceptions import ValidationError
from todo.views import TaskModel


# class TaskForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField(widget=forms.Textarea(),required=True)
    # def clean_description(self):
    #     description = self.cleaned_date.get('description')
    #     if any(char.isdigit() for char in description):
    #         raise ValidationError("description cannot contain numbers")
    #     return description

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title','description']

    def __init__(self, *args, **kwargs):
        super(TaskForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
