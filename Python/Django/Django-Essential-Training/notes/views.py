from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .models import Notes
from .forms import NotesForm

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'text'] # replaced by "form_class = NotesForm" bellow
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes    
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html" 


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    

# Challenge - Class 04
# My 1st approach using queryset attribute (commented out)
# My second approach using get_queryset method:
class NotesPopularListView(ListView):
    model = Notes    
    # queryset = Notes.objects.filter(likes__gt=0) # 1st approach
    context_object_name = "notes"
    template_name = "notes/notes_popular.html"
    
    def get_queryset(self): # 2nd approach
        return Notes.objects.filter(likes__gt=0)
       

# Instructor's approach
# She uses queryset only. The way she does uses the note_list template, whithout creating a new one like I did. She also uses gte=1 which means "greater or equal to 1" instead of gt=0 (greater to zero)
class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html" 
    queryset = Notes.objects.filter(likes__gte=1)


# Final CRUD methods: Delete
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


# Challenge - Class 07: Instructor's approach (Function-based view)
def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
    raise Http404("Only POST requests are allowed for this view.")