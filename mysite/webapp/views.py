from django.shortcuts import render


def index(request):
    return render(request, 'webapp/index.html')


def contact(request):
    return render(request,
                  'webapp/basic.html',
                  {'info': [
                        'I\'d love to hear from you!',
                        'Send me an email and say hi',
                        'blooma116 -at- gmail',
                  ]})
