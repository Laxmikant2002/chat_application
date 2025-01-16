from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmailForm
from .utils.aws_lambda import invoke_lambda

@login_required
def profile_settings_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)
        if form.is_valid():
            email = form.cleaned_data['email']
            payload = {
                'email': email
            }
            response = invoke_lambda('YourLambdaFunctionName', payload)
            if response['statusCode'] == 200:
                messages.success(request, 'Email updated successfully.')
            else:
                messages.error(request, 'Failed to update email.')
            return redirect('profile-settings')
    else:
        form = EmailForm(instance=request.user)
    return render(request, 'users/profile_settings.html', {'form': form})