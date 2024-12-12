from django.shortcuts import render, redirect, get_object_or_404
from .models import Note


def home(request):
    return render(request, 'index.html')

def note_list(request):
    notes = Note.objects.all()
    ctx = {'notes': notes}
    return render(request, 'notes/note-list.html', ctx)

def note_form(request):
    if request.method == 'POST':
        note_title = request.POST.get('note_title')
        content = request.POST.get('content')
        if note_title and content:
            Note.objects.create(
                note_title=note_title,
                content=content,
            )
            return redirect('notes:list')
    return render(request, 'notes/note-form.html')

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    ctx = {'note': note}
    return render(request, 'notes/note-detail.html', ctx)

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note_title = request.POST.get('note_title')
        content = request.POST.get('content')
        if note_title and content:
            note.note_title=note_title
            note.content=content
            note.save()
            return redirect(note.get_detail_url())
    ctx = {'note': note}
    return render(request, 'notes/note-form.html', ctx)

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes:list')
