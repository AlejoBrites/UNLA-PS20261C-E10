from django.shortcuts import render, get_object_or_404
from .models import Game, Category


def catalog(request):
    games = Game.objects.filter(is_available=True).select_related('category')
    categories = Category.objects.all()

    query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '').strip()

    if query:
        games = games.filter(title__icontains=query)

    if category_slug:
        games = games.filter(category__slug=category_slug)

    return render(request, 'games/catalog.html', {
        'games': games,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
    })


def detail(request, slug):
    game = get_object_or_404(Game, slug=slug, is_available=True)
    # Verificar si el usuario ya tiene el juego en su biblioteca
    already_owned = False
    if request.user.is_authenticated:
        already_owned = request.user.library_entries.filter(game=game).exists()
    return render(request, 'games/detail.html', {
        'game': game,
        'already_owned': already_owned,
    })
