from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Activity
from .forms import IncreaseHourForm, DecreaseHourForm

def index(request):
    activity_list = Activity.objects.order_by('-total_hour')
    context = {'activity_list': activity_list}
    return render(request, 'tentacle/index.html', context)

def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    
    # Increase and decrease total hour form.
    if request.method == 'POST':
        if 'inc_hour_btn' in request.POST:
            increase_hour_form = IncreaseHourForm(request.POST)
            if increase_hour_form.is_valid():
                activity.latest_hour = int(increase_hour_form.cleaned_data['num'])
                activity.update_total_hour()
                activity.get_last_update()
                activity.save()
                return HttpResponseRedirect('/' + activity_id)
        elif 'dec_hour_btn' in  request.POST:
            decrease_hour_form = DecreaseHourForm(request.POST)
            if decrease_hour_form.is_valid():
                activity.latest_hour = -int(decrease_hour_form.cleaned_data['num'])
                activity.update_total_hour()
                activity.get_last_update()
                activity.save()
                return HttpResponseRedirect('/' + activity_id)  
    else:
        increase_hour_form = IncreaseHourForm()
        decrease_hour_form = DecreaseHourForm()

    return render(request, 'tentacle/detail.html', {'activity': activity, 'increase_hour_form': increase_hour_form, 'decrease_hour_form': decrease_hour_form})

