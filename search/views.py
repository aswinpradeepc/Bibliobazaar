# search/views.py

from django.shortcuts import render
from book_shop.models import BookForSale

def search_books(request):
    if request.method == 'POST':
        search_text = request.POST.get('q', '')
        obj = None
        count = 0

        if search_text:
            obj = BookForSale.objects.filter(title__icontains=search_text) | \
                  BookForSale.objects.filter(author__icontains=search_text)
            count = obj.count()

        context = {'results': obj, 'search_text': search_text, 'count': count}

        # Render the template with the given context
        return render(request, 'search/search_results.html', context)

    return render(request, 'search/search_results.html')
