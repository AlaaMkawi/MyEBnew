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
from .models import InformationBoard
from .models import Paropinion
from .models import Profile , Meeting

class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ParentSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']




class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text']


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

class InformationBoardForm(forms.ModelForm):
    class Meta:
        model = InformationBoard
        fields = ['title', 'content']


#alaa

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'

class PediatricianForm(forms.ModelForm):
    class Meta:
        model = Pediatrician
        fields = '__all__'

class PsychologistForm(forms.ModelForm):
    class Meta:
        model = Psychologist
        fields = '__all__'

class ExtraInfoForm(forms.ModelForm):
    class Meta:
        model = ExtraInfo
        fields = '__all__'


class AddTrackForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"name", "class":"form-control"}), label="")
    explanation = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Explanation", "class":"form-control"}), label="")

    class Meta:
        model = Track
        exclude = ("user",)



class Paropinionform(forms.ModelForm):
    class Meta:
        model = Paropinion
        fields = ['title', 'content']



class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['title', 'day', 'time', 'link']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number', 'age', 'gender']


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'date', 'time', 'host']


