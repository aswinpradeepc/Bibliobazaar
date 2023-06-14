from django.shortcuts import render
from .forms import ResellRequestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def resell_view(request):
    if request.method == 'POST':
        form = ResellRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Form submission successful 👍')
            form = ResellRequestForm()
    else:
        form = ResellRequestForm()

    context = {'form': form}
    return render(request, 'resell.html', context)


