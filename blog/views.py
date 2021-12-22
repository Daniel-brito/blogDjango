from django.shortcuts import render

def post_list(request):
    #resposta da requisição
    return render(request, 'blog/post_list.html', {})
