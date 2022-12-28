from django import forms
from users.models import Week, Workout


class WeekEditForm(forms.ModelForm):
    PRIO_CHOICES = (('A', 'A'), ('B', 'B'), ('C', 'C'), (None, None))
    priority = forms.ChoiceField(choices=PRIO_CHOICES, required=False)
    comment = forms.CharField(widget=forms.Textarea, max_length=80, required=False)
    race = forms.CharField(required=False)

    class Meta:
        model = Week
        fields = ('period', 'hrs_planned',  'race', 'priority', 'comment')


class WorkoutCreateForm(forms.ModelForm):
    WO_TYPE = (('Workout', 'Workout'), ('Race', 'Race'), ('Test', 'Test'))
    type = forms.ChoiceField(choices=WO_TYPE, required=True)

    class Meta:
        model = Workout
        fields = ('title', 'type', 'task', 'duration_min')


class WorkoutEditForm(forms.ModelForm):
    WO_TYPE = (('Workout', 'Workout'), ('Race', 'Race'), ('Test', 'Test'))
    type = forms.ChoiceField(choices=WO_TYPE, required=True)

    class Meta:
        model = Workout
        fields = ('title', 'type', 'task', 'duration_min', 'distance', 'alt_gain', 'feelings', 'pe')

