from django.shortcuts import render, HttpResponse
import wikipedia

def home(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            summary = wikipedia.summary(search, sentences=12)
            result = summary.split('. ')
        except wikipedia.exceptions.DisambiguationError as e:
            result = ["Multiple results found: " + ', '.join(e.options)]
        except wikipedia.exceptions.PageError:
            result = ["No results found for the search term."]
        except Exception as e:
            result = [str(e)]
        return render(request, "main/index.html", {"result": result})
    return render(request, "main/index.html")
