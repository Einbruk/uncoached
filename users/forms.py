from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class ExtendedRegister(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)
    # phone = forms.CharField(max_length=15, required=False)
    # tg_id = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')


class SurveyFormShort(forms.Form):
    CHOICES = (('1', 'Full season'), ('2', 'One race'))
    DAY_CHOICES = tuple([(i, i) for i in range(1, 32)])
    MONTH_CHOICES = (('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'),
    ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December'))
    hrs = forms.IntegerField(min_value=300, max_value=1200)
    strategy = forms.ChoiceField(choices=CHOICES)
    race_day = forms.ChoiceField(choices=DAY_CHOICES)
    race_month = forms.ChoiceField(choices=MONTH_CHOICES)
    seasonGoals = forms.CharField(widget=forms.Textarea, max_length=300)
    seasonObjectives = forms.CharField(widget=forms.Textarea, max_length=300)


