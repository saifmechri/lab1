Compte rendu tp Lab1 

Nom : mechri 

Prénom; saif 

Classe: DSI21 

 

1) Ce code utilise Pydantic pour créer un modèle User avec des champs validés automatiquement (name, email, account_id). Il inclut un validateur personnalisé pour s’assurer que account_id est positif. Ensuite, un objet User est instancié, converti en JSON et en dictionnaire. Enfin, une chaîne JSON valide est utilisée pour recréer un objet User via model_validate_json(). Ce script montre comment valider, manipuler et convertir des données de manière sûre avec Pydantic. 

 

 

 

 

 

 

 

 

2)Explication du Code Python : Requêtes HTTP et Web Scraping 

 

 

Ce script constitue un excellent tutoriel pratique pour maîtriser plusieurs compétences essentielles en Python dans le domaine des communications web. Il couvre : 

Les requêtes HTTP basiques et avancées (GET, POST), 

La gestion des erreurs réseau comme les codes 404 ou les délais d’attente (timeout), 

L’utilisation d’en-têtes personnalisés (notamment pour l’authentification), 

Le web scraping avec BeautifulSoup, pour extraire efficacement des informations d’une page HTML, 

Et la comparaison entre les bibliothèques requests et urllib, chacune avec ses spécificités. 

Grâce à ces exemples, un développeur peut acquérir une base solide pour interagir avec des APIs, récupérer et analyser des contenus web, gérer des erreurs avec robustesse, et intégrer des techniques modernes de scraping. Ce type de compétences est indispensable dans les domaines de l’automatisation, des systèmes distribués, de l’agrégation de données, et du développement de services web. 

 

3)Ce code crée une API permettant de gérer des items dans une liste (simulation d'une base de données). Les fonctionnalités offertes sont : 

Afficher tous les items. 

Afficher un item spécifique par son ID. 

Ajouter un nouvel item. 

Mettre à jour un item existant. 

Chaque action est associée à une route (GET, POST, PUT), et les réponses sont envoyées au format JSON. 

 

 

 

4) Le code que tu as partagé est un script Streamlit qui crée une interface web interactive. Voici un aperçu de ce que le code affiche et de ce qu'il permet de faire lorsque tu l'exécutes : 

1. Message de bienvenue : 

Le texte Hello World est affiché en haut de l'application avec st.write('Hello World'). 

2. Demander à l'utilisateur son film préféré : 

Un champ de saisie de texte (input) est affiché avec la question "Favorite Movie?". L'utilisateur peut entrer le nom de son film préféré. 

Lorsque l'utilisateur entre un texte, le film préféré est affiché sous la forme Your favorite movie is: [Nom du film]. 

3. Bouton : 

Un bouton nommé "Click Me" est affiché, mais l'action n'est pas encore définie dans ton code. Il ne fait rien tant que tu n'ajoutes pas d'action pour ce bouton. 

4. Affichage d'un titre H2 : 

Un titre de niveau 2 This is a H2 Title! est affiché à l'écran avec st.write("## This is a H2 Title!"). 

5. Texte formaté en Markdown : 

Le texte est affiché en utilisant du Markdown, ce qui permet de mettre en forme du texte avec des styles comme l'italique, le gras, et des couleurs de texte. 

Par exemple, tu verras des textes comme "Streamlit is really cool". 

Un bouquet d'emoji (🌸🌼🌷) sera aussi affiché grâce à une ligne avec des emojis dans le Markdown. 

6. Lecture d'un fichier CSV (movies.csv) : 

Le script essaie de lire un fichier CSV nommé movies.csv et d'afficher son contenu sous forme de tableau. 

Si le fichier n'existe pas dans le répertoire actuel, un message d'erreur est affiché : "movies.csv not found in the current directory." 

7. Graphiques avec des données aléatoires : 

Des graphiques générés avec des données aléatoires sont affichés : 

Un graphique en barres (st.bar_chart) et un graphique linéaire (st.line_chart) représentant les données aléatoires dans un DataFrame. 

8. Calculateur de paiements hypothécaires : 

Un calculateur d'hypothèque est affiché, avec plusieurs champs de saisie pour que l'utilisateur entre : 

La valeur de la maison 

Le dépôt 

Le taux d'intérêt 

La durée du prêt en années 

Le calcul des paiements mensuels est effectué et affiché sous la forme de 3 mesures : 

Paiement mensuel 

Total des paiements 

Total des intérêts 

9. Tableau des paiements hypothécaires : 

Un tableau avec l'échéancier des paiements est créé et affiché sous forme de graphique linéaire. 

Le graphique montre le solde restant à chaque année du prêt. 

Ce qui sera affiché concrètement dans le navigateur : 

Hello World 

Input pour entrer le film préféré 

Un bouton "Click Me" 

Titre H2 

Texte formaté en Markdown avec des couleurs et des emojis 

Tableau (si movies.csv est trouvé) ou erreur si le fichier n'est pas trouvé 

Graphiques générés aléatoirement avec np.random.randn 

Calcul du prêt hypothécaire avec résultats financiers 

Graphique montrant le plan de remboursement sur la durée du prêt 

 

 
