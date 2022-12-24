from datetime import date
import datetime
from users.models import User, Year, Week, Day, Workout


def create_plan(year, cleaned_data, user):
    periods = ['Prep', 'Base 1 w1', 'Base 1 w2', 'Base 1 w3', 'Base 1 w4', 'Base 2 w1', 'Base 2 w2', 'Base 2 w3',
               'Base 2 w4', 'Base 3 w1', 'Base 3 w2', 'Base 3 w3', 'Base 3 w4', 'Build 1 w1', 'Build 1 w2',
               'Build 1 w3', 'Build 1 w4', 'Build 2 w1', 'Build 2 w2', 'Build 2 w3', 'Build 2 w4', 'Peak w1',
               'Peak w2', 'Race', 'Trans']
    week_days = ['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun', 'Total']
    hrs = int(cleaned_data.get('hrs'))
    day = int(cleaned_data.get('race_day'))
    month = int(cleaned_data.get('race_month'))
    goals = cleaned_data.get('seasonGoals')
    objectives = cleaned_data.get('seasonObjectives')

    first_a_race_date = date(year, month, day)
    week_num = first_a_race_date.isocalendar()[1]

    plan = Year.objects.create(year=year, athlete=user, hrs_planned=hrs, goals=goals, objectives=objectives)
    ind = periods.index('Race')

    for w_n in range(week_num, 0, -1):
        shrt = '{}-{}-1'.format(year, w_n)
        dt = datetime.datetime.strptime(shrt, "%Y-%W-%w")
        mon = datetime.date(dt.year, dt.month, dt.day)
        w = Week.objects.create(week_no=w_n, starts_with=mon, hrs_planned=10, period=periods[ind], year=plan)
        ind -= 1
        for i in range(7):
            Day.objects.create(week=w, day=mon+datetime.timedelta(i), week_day=week_days[i])

    for w_n in range(week_num+1, 53):
        shrt = '{}-{}-1'.format(year, w_n)
        dt = datetime.datetime.strptime(shrt, "%Y-%W-%w")
        mon = datetime.date(dt.year, dt.month, dt.day)
        w = Week.objects.create(week_no=w_n, starts_with=mon, hrs_planned=8, period=periods[24], year=plan)
        for i in range(7):
            Day.objects.create(week=w, day=mon + datetime.timedelta(i), week_day=week_days[i])
