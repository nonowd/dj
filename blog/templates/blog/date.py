{% extends "base.html" %}
{% block title %}Ma page d'accueil{% endblock %}
{% block content %}
    <h2>Bienvenue !</h2>
	<p>La date actuelle est : {{ date }}</p>
    <p>
       Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rhoncus 
       massa non tortor. Vestibulum diam diam, posuere in viverra in, 
       ullamcorper et libero. Donec eget libero quis risus congue imperdiet ac 
       id lectus. Nam euismod cursus arcu, et consequat libero ullamcorper sit 
       amet.
    </p>
    <a href="{% url "afficher_article" 42 %}">
    Lien vers mon super article N° 42
</a>
{% endblock %}



