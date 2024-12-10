from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from app8.models import studytable,PageVisit
from app8.form import datatable,CommentForm
from app8.form import Comment
from django.core.mail import send_mail
from django.db.models import Q
from .feeds import LatestStudyTableFeed
from django.views.generic import DetailView
import feedparser
# Create your views here.


def fun1(request):
    a = datatable()
    if request.method == "POST":
        b = datatable(request.POST)

        if b.is_valid():
            b.save()
        return HttpResponse("saved")
    return render(request, "UserForm.html", {"datakey1":a})

def send_emails(request):
    if request.method == "POST":
        a = studytable.objects.values_list('Email', flat=True)
        for i in a:
            subject = "for testing"
            message = "Hi"
            from_email = 'iballplayboy@gmail.com'
            send_list = [i]
            send_mail(subject, message, from_email, send_list, fail_silently=False)
        return HttpResponse("success")


    return render(request, "sendmail.html")


def homepage(request):
    # Get or create the PageVisit object
    page_visit, created = PageVisit.objects.get_or_create(pk=1)

    # Increment the count
    page_visit.count += 1
    page_visit.save()
    return render(request,"Home.html",{"key5":page_visit.count})

def select_data(request):
    z = studytable.objects.filter(Q(Amount=0))
    b=z
    if request.method == "POST":

        a = b.values_list('Email', flat=True)
        for i in a:
            subject = "for testing"
            message = "Hi, please pay the due amount as early as possible"
            from_email = 'iballplayboy@gmail.com'
            send_list = [i]
            send_mail(subject, message, from_email, send_list, fail_silently=False)
        return HttpResponse("success")


    return render(request, "Defaulters.html", {"key1":b})

def comment_list(request):
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the same 'comment_list' URL to display updated comments
            return redirect(request.path)
    else:
        form = CommentForm()

    return render(request, 'comment_list.html', {'comments': comments, 'form': form})



class StudyTableDetailView(DetailView):
    model = studytable
    template_name = 'studytable_detail.html'
    context_object_name = 'studytable1'

def rss_reader(request):
    feed_url = 'http://127.0.0.1:8000/app8/latest/feed/'  # Replace with the actual feed URL
    feed = feedparser.parse(feed_url)
    entries = feed.entries
    return render(request, 'rss_reader.html', {'entries': entries})