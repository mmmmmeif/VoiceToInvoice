from django.shortcuts import render

def post_list(request):
    return render(request, 'invoice/post_list.html', {})
