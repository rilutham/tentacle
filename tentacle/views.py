from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Activity, Note
from .forms import IncreaseHourForm
from django.utils import timezone

def index(request):
    activities = Activity.objects.order_by('-total_hour')
    activity_list = activities.filter(parent_activity_id = 0)
    top_level_activity = activity_list.exclude(id=0)
    return render(request, 'tentacle/index.html', {'top_level_activity': top_level_activity})

def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)

    # Increase and decrease total hour form.
    if request.method == 'POST':
        if 'inc_hour_btn' in request.POST:
            increase_hour_form = IncreaseHourForm(request.POST)
            if increase_hour_form.is_valid():
                choice = increase_hour_form.cleaned_data['choice_field']
                if choice == 'pos':
                    num = int(increase_hour_form.cleaned_data['num'])
                elif choice == 'neg':
                    num = -int(increase_hour_form.cleaned_data['num'])
                activity.latest_hour = num
                activity.update_total_hour()
                activity.get_last_update()
                activity.save()
                note = increase_hour_form.cleaned_data['note']
                n = Note(note=note, activity_id=activity_id)
                n.save()
                return HttpResponseRedirect('/' + activity_id)
    else:
        increase_hour_form = IncreaseHourForm()

    activities = Activity.objects.order_by('-total_hour')
    activity_list = activities.filter(parent_activity_id = 0)
    top_level_activity = activity_list.exclude(id=0)

    return render(request, 'tentacle/detail.html', {'activity': activity, \
            'increase_hour_form': increase_hour_form, 'top_level_activity': top_level_activity})

def delete_activity(request, activity_id=None):
    activity = get_object_or_404(Activity, pk=activity_id)
    activity.delete()
    return HttpResponseRedirect('/')