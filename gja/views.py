from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Member, Event

# Create your views here.
def members_by_category(request, slug):

    if slug not in dict(Member.CATEGORY_CHOICES):
        raise Http404()

    members = Member.objects.filter(
        category=slug
    )

    return render(
        request,
        'members/members_list.html',
        {
            'members': members,
            'category': dict(
                Member.CATEGORY_CHOICES
            )[slug]
        }
    )


def event_detail(request, slug):

    event = get_object_or_404(
        Event,
        slug=slug
    )

    return render(
        request,
        'events/event_detail.html',
        {
            'event': event
        }
    )


def home(request):

    categories = Member.CATEGORY_CHOICES

    events = Event.objects.all()

    context = {
        'categories': categories,
        'events': events,
    }

    return render(
        request,
        'home.html',
        context
    )
