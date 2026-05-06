from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes


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


# Model, remove these two commented out function based views (list, detail) when creating the DJANGO-LEARNING-NOTES-class_04.md. You can keep the learning notes at the bottom, as referece for the learning notes:
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
    
#     return render(request, 'notes/notes_detail.html', {'note': note})




# ---- For learning notes: ----
# 
# Django's generic CBVs (ListView, DetailView) automatically derive the template
# name using the convention: <app_label>/<model_name_lowercase>_<suffix>.html
# e.g. Notes + ListView → notes/notes_list.html, Notes + DetailView → notes/notes_detail.html
# So the explicit `template_name` attribute on NotesListView is redundant — both views work
# without it, as long as the template files match the naming convention.

# However, for the challenge 04, I had to explicitly declare and assign the template_name = "notes/notes_popular.html". The page won't load that template without it, otherwise, it falls back to template_name = "notes/notes_list.html" instead.

# Regarding my approach, I found this question at Stack Overflow that helped me to understand what I had to do (https://stackoverflow.com/questions/19707237/use-get-queryset-method-or-set-queryset-variable). It worked (screenshot at screenshots/Screenshot from 2026-05-06 17-14-29.png) - Model attach this screenshot to the learning notes in the correlated section. 
# 
# According to that forum, queryset, the approach I used, is created once when the server starts.
# However, the get_queryset() method is called for every request
# I will try use the get_queryset() method as my second approach, and then compare with the instructor's after I finish this challenge.

# ---- End of learning notes ----