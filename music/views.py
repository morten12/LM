from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    # context_object_name = 'object_list' <-- By Default
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    # What type of object are you trying to get the details of?
    model = Album
    template_name = 'music/detail.html'
