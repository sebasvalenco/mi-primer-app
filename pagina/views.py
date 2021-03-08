from django.shortcuts import render

def post_list(request):
    return render(request, 'pagina/post_list.html', {})
