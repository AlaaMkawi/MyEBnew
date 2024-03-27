from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from .models import Feedback
from .models import Parent
from .models import Comment
from .models import WorkshopSummary
from django import forms
from .models import BabyHealth
class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ParentSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

from .models import ParentProfile

class ParentProfileForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        fields = '__all__'



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comments']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your comment here...'})
        }




class SummaryForm(forms.ModelForm):
    class Meta:
        model = WorkshopSummary
        fields = ['psychologist_name', 'workshop_date', 'summary_text']
from .models import PsychologistComment

class PsychologistCommentForm(forms.ModelForm):
    class Meta:
        model = PsychologistComment
        fields = ['psychologist_name', 'comment']



class BabyHealthForm(forms.ModelForm):
    class Meta:
        model = BabyHealth
        fields = ['name', 'description']
