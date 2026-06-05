from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Member, Event, HomeImage

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


def events_by_category(request, slug):

    if slug not in dict(Event.CATEGORY_CHOICES):
        raise Http404()

    events = Event.objects.filter(
        category=slug
    )

    return render(
        request,
        'events/events_list.html',
        {
            'events': events,
            'category': dict(
                Event.CATEGORY_CHOICES
            )[slug]
        }
    )


def home(request):

    categories = Member.CATEGORY_CHOICES

    events = Event.objects.all()

    hero_image = HomeImage.objects.filter(
        category='hero'
    ).first()

    about_image = HomeImage.objects.filter(
        category='about'
    ).first()

    member_images = HomeImage.objects.filter(
        category='member'
    )

    leadership_image = HomeImage.objects.filter(
        category='leadership'
    ).first()

    context = {
        'categories': categories,
        'events': events,
        'hero_image': hero_image,
        'about_image': about_image,
        'member_images': member_images,
        'leadership_image': leadership_image,
    }

    return render(
        request,
        'home.html',
        context
    )
