from django.shortcuts import render, get_object_or_404

from .models import Board


def home(request):
    boards = Board.objects.all()

    context = {
        'boards': boards
    }

    return render(request, 'home.html', context)


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)

    context = {
        'board': board
    }

    return render(request, 'topics.html', context)
