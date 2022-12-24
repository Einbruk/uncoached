from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from users.models import Year, Week, User, Workout, Day


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

