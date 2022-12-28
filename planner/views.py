import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from users.models import Year, Week, User, Workout, Day
from planner.forms import WeekEditForm, WorkoutCreateForm, WorkoutEditForm

class YearView(View):
    def get(self, request, year):
        if request.user.is_authenticated:
            try:
                plan = Year.objects.get(athlete=request.user, year=year)
            except:
                plan = None
            return render(request, 'planner/year.html', {'plan': plan, 'prev_year': year-1,
                                                         'year': year, 'next_year': year+1})
        else:
            return HttpResponseRedirect('/users/login/')


class WeekView(View):
    def get(self, request, year, week):
        year_obj = Year.objects.get(athlete=request.user, year=year)
        week_obj = Week.objects.get(year=year_obj, week_no=week)
        days = Day.objects.filter(week=week_obj)
        workouts = Workout.objects.filter(week=week_obj)

        hrs, dist = 0, 0
        for workout in workouts:
            hrs += round(workout.duration_min / 60, 1)
            dist += workout.distance
        week_obj.hrs_fact = hrs
        week_obj.km_fact = dist

        context = {
            'week': week_obj,
            'days': days,
            'workouts': workouts,
        }
        return render(request, 'planner/week.html', context)


class WeekEditView(View):
    def get(self, request, year, week):
        year_obj = Year.objects.get(athlete=request.user, year=year)
        week_obj = Week.objects.get(year=year_obj, week_no=week)
        form = WeekEditForm(instance=week_obj)
        return render(request, 'planner/week-edit.html', {'form': form})

    def post(self, request, year, week):
        year_obj = Year.objects.get(athlete=request.user, year=year)
        week_obj = Week.objects.get(year=year_obj, week_no=week)
        form = WeekEditForm(request.POST, instance=week_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/year/{year}/')
        return render(request, 'planner/week-edit.html', {'form': form})


class WorkoutCreateView(View):
    def get(self, request, year, week, day, month):
        form = WorkoutCreateForm()
        return render(request, 'planner/workout-edit.html', {'form': form, 'day': day, 'month': month})

    def post(self, request, year, week, day, month):
        form = WorkoutCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            type = form.cleaned_data['type']
            task = form.cleaned_data['task']
            duration = form.cleaned_data['duration_min']
            date = datetime.date(year, month, day)
            year_obj = Year.objects.get(athlete=request.user, year=year)
            week_obj = Week.objects.get(year=year_obj, week_no=week)
            day_obj = Day.objects.get(week=week_obj, day=date)
            Workout.objects.create(title=title, type=type, task=task, duration_min=duration, day=day_obj, week=week_obj)
            return HttpResponseRedirect(f'/year/{year}/week/{week}/')
        return render(request, 'planner/week-edit.html', {'form': form})


class WorkoutView(View):
    def get(self, request, year, week, id):
        workout = Workout.objects.get(id=id)
        duration = [workout.duration_min // 60, workout.duration_min - (workout.duration_min // 60) * 60]
        avg_spd = round(workout.distance / (workout.duration_min / 60), 1)
        context = {
            'workout': workout,
            'duration': duration,
            'avg_spd': avg_spd
        }
        return render(request, 'planner/workout-detailed.html', context)


class WorkoutDeleteView(View):
    def get(self, request, year, week, id):
        Workout.objects.filter(id=id).delete()
        return HttpResponseRedirect(f'/year/{year}/week/{week}/')


class WorkoutEditView(View):
    def get(self, request, year, week, id):
        workout = Workout.objects.get(id=id)
        form = WorkoutEditForm(instance=workout)
        return render(request, 'planner/workout-edit.html', {'form': form})

    def post(self, request, year, week, id):
        workout = Workout.objects.get(id=id)
        form = WorkoutEditForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/year/{year}/week/{week}/{id}/')
        return render(request, 'planner/workout-edit.html', {'form': form})

