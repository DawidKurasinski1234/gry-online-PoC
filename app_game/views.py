from django.shortcuts import render, Http404

# Create your views here.
news_items = [
                 {
                     "id":1,
                     "title": "Kółko i krzyżyk",
                     "image": "images/kk.png",
                     "description": "Klasyczne kółko i krzyżyk",
                     "date": "27 kwietnia 2025",
                     "label": "Arcade",
                     "iframe": 'kk/index.html'
                 },
                 {
                    "id":2,
                     "title": "Snake",
                     "image": "images/snake.png",
                     "description": "Zagraj w kultowego węża - zbieraj owoce aby zebrać jak najwięcej punktów",
                     "date": "27 kwietnia 2025",
                     "label": "Akcja",
                     "iframe": 'snake/index.html'
                 },
                 {
                    "id":3,
                     "title": "Tetris",
                     "image": "images/tetris.png",
                     "description": "Jedna z pierwszych gier wideo - musisz w nią zagrać",
                     "date": "27 kwietnia 2025",
                     "label": "Logiczne",
                      "iframe": 'tetris/index.html'
                 },
{
                    "id":4,
                     "title": "Unity VR",
                     "image": "images/unity.png",
                     "description": "Gra utworzona na silniku Unity przeniesiona na wersję web",
                     "date": "27 kwietnia 2025",
                     "label": "VR",
                      "iframe": 'Unity/index.html'
                 },
             ]


def index(request):
    context = {"news_items": news_items}
    return render(request, 'index.html', context)


def details(request, id):
    try:
        item = news_items[id - 1]
    except IndexError:
        raise Http404("Nie znaleziono wpisu.")

    context = {"item": item}
    return render(request, 'details.html', context)


from django.shortcuts import redirect

def kolko_i_krzyzyk_view(request):
    return redirect('/static/games/kk/index.html')

def snake_view(request):
    return redirect('/static/games/snake/index.html')

def tetris_view(request):
    return redirect('/static/games/tetris/index.html')

def unity_view(request):
    return redirect('/static/games/unity/index.html')