from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Имя: {name}, Электронная почта: {email}, Сообщение от пользователя: {message}")

    return render(request, 'catalog/contact.html')
