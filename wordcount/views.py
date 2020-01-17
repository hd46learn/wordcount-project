#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    worddict = {}
    for word in words:
        worddict[word] = worddict.get(word,0) + 1
    wordlist = list()
    for word, appear in list(worddict.items()):
        wordlist.append((appear, word))
    wordlist.sort(reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'wordcount':len(words), 'wordlist': wordlist})
