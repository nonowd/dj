from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import Article

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    if int(month) > 12:
    	raise Http404
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)  
        
    ) 

def view_article(request, id_article):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article #{0} !".format(id_article)    
    )

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")

def date_actuelle(request):
	couleurs = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
	date = datetime.now()
	return render(request, 'blog/date.html', locals())

def addition(request, nombre1, nombre2):
	total = int(nombre1) + int(nombre2)
	return render(request, 'blog/addition.html', locals())

def accueil(request):
	articles = Article.objects.all()
	return render(request, 'blog/accueil.html', {'derniers_articles' : articles})

def lire(request, id):
	article = get_object_or_404(Article, id=id)
	return render(request, 'blog/lire.html', {'article': article})
 	

