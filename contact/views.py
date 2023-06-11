
from django.shortcuts import render
from .forms import BookRequestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def contact_view(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful 👍')
            form = BookRequestForm()
    else:
        form = BookRequestForm()

    context = {'form': form}
    return render(request, 'contact.html', context)


