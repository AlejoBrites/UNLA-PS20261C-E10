from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LibraryEntry


@login_required
def library(request):
    entries = LibraryEntry.objects.filter(user=request.user).select_related('game')
    return render(request, 'library/library.html', {'entries': entries})


@login_required
def update_status(request, entry_id):
    if request.method != 'POST':
        return redirect('library:library')

    entry = get_object_or_404(LibraryEntry, id=entry_id, user=request.user)
    action = request.POST.get('action')

    # Transiciones de estado válidas según la acción
    transitions = {
        'download': LibraryEntry.STATUS_DOWNLOADING,
        'install': LibraryEntry.STATUS_INSTALLED,
        'update': LibraryEntry.STATUS_INSTALLED,
    }

    if action in transitions:
        entry.status = transitions[action]
        entry.save(update_fields=['status'])
        messages.success(request, f'Estado de "{entry.game.title}" actualizado.')

    return redirect('library:library')
