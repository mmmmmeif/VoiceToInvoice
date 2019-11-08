from django.shortcuts import render
from datetime import datetime
from . import filetotext

def post_list(request):
    return render(request, 'invoice/post_list.html', {})

def makeinvoice(request):
    filename = filetotext.record.makeWave()
    results = filetotext.transcribe_file(filename)
    return render(request,'invoice/makeinvoice.html', results)

def result(request):
    return render(request, 'result.html')

def index(request):
    return render(request, 'index.html')

def exercise(request):
    text = 'テストです。'
    try:
        input_text = request.POST['input_text']
        print(input_text)
        text = input_text
    except:
        return render(request, 'index/exercise.html')

    now = datetime.now();
    context = {
        'text': text,
        'time': now,
    }
    return render(request, 'invoice/exercise.html', context)
