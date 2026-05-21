from typing import Any

from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes   
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/login' # This is the URL where users will be redirected if they are not authenticated. You can change this to match your actual login URL.

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes    
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/login'


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html" 
    login_url = '/login' 

    def get_queryset(self):
        return self.request.user.notes.all().order_by('-is_public', '-created') # Challenge Class 08: My approach to show public notes first, then private notes, both ordered by created date in descending order. Note that the is_public field is a boolean, so it will be ordered with False (private) first and True (public) last. To show public notes first, we need to order by -is_public (descending order), which will put True (public) before False (private). The created field is also ordered in descending order to show the most recent notes first.


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
    login_url = '/login'
    

# Challenge - Class 04
# My 1st approach using queryset attribute (commented out)
# My second approach using get_queryset method:
class NotesPopularListView(LoginRequiredMixin, ListView):
    model = Notes    
    # queryset = Notes.objects.filter(likes__gt=0) # 1st approach
    context_object_name = "notes"
    template_name = "notes/notes_popular.html"
    login_url = '/login'
    
    def get_queryset(self): # 2nd approach
        # Show popular notes while respecting visibility:
        # users can see their own notes and public notes from others.
        return Notes.objects.filter(
            Q(likes__gt=0) & (Q(user=self.request.user) | Q(is_public=True))
        ).order_by('-likes')
       

# Instructor's approach
# She uses queryset only. The way she does uses the note_list template, whithout creating a new one like I did. She also uses gte=1 which means "greater or equal to 1" instead of gt=0 (greater to zero)
class PopularNotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html" 
    queryset = Notes.objects.filter(likes__gte=1)
    login_url = '/admin'


# Final CRUD methods: Delete
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = '/login'

#------> Function-based views

# Challenge - Class 09: My implementation to share the note with other users.
# User should be able to share a note, its own note and else's note, with other unlogged users.
# Only public notes can be shared.
# If the user tries to share a private note, it should show a message saying that the note should be public to be shared.
  
def notes_share_view(request, pk):
    note = get_object_or_404(Notes, pk=pk) # Only allow sharing of public notes. If the note is not public, it will raise a 404 error.

    if not note.is_public:
        return render(request, 'notes/notes_share.html', {'note': note})
    
    
    if request.method == 'POST':
        # Here you would implement the logic to share the note, e.g., sending an email or generating a shareable link.
        # For simplicity, we'll just return a success message.
        def generate_shareable_link(note):
            # This is a placeholder function. You would implement the actual logic to generate a shareable link.
            return request.build_absolute_uri(reverse("notes.share", args=[note.id]))

        return HttpResponse(generate_shareable_link(note))
    
    return render(request, 'notes/notes_share.html', {'note': note})    
    




# Challenge - Class 07: Instructor's approach (Function-based view)
def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
    raise Http404("Add Like View Warning: Only POST requests are allowed for this view.")

# Challenge - Class 08: My approach
def mark_public_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.is_public = True
        # note.is_public = not note.is_public # This is the Instructor's approach for this part of Challenge - Class 08.
        note.save()
        return HttpResponseRedirect(reverse('notes.list', args=()))
    raise Http404("Mark Public View Warning: Only POST requests are allowed for this view.")

# Challenge - Class 08: My implementation to mark the note as private again (not mentioned in the video, but I thought it would be a good addition)
def mark_private_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.is_public = False
        note.save()
        return HttpResponseRedirect(reverse('notes.list', args=()))
    raise Http404("Mark Private View Warning: Only POST requests are allowed for this view.")



       