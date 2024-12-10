from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import studytable1

class LatestStudyTableFeed(Feed):
    title = "Latest Study Table Entries"
    link = "/"
    description = "Latest entries from the Study Table."

    def items(self):
        return studytable1.objects.all()

    def item_title(self, item):
        return f"{item.Firstname} - {item.Age} years"

    def item_description(self, item):
        return f"Email: {item.Email}, Mobile: {item.Mob}"

    def item_link(self, item):
        return reverse('app8:studytable-detail', args=[str(item.id)])