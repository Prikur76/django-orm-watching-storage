from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    """Возвращает список незакрытых посещений"""
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        who_entered = visit.passcard.owner_name
        entered_at = visit.entered_at
        duration = visit.format_duration()
        is_strange = visit.is_visit_long()
        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': entered_at,
                'duration': duration,
                'is_strange': is_strange
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
