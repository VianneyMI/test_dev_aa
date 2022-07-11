<h1 style="text-align:center">
    <u>
    Tests techniques<br>
    DEV BACKEND PYTHON
    </u>
</h1>

<h2>
    <ol>
        <li>Développement d'un nouveau endpoint</li>
    </ol>
</h2>

<ol>
    <h3>
        Application d'une stratégie différenciée par marque /carburant
    </h3>
</ol>


<ol>
    <li>Code Review</li>
    <p>Pour les commentaires de review voir fichier <i>legacy.py</i> et l'image <i>problems.png</i> dans le dossier image</p>
    <li>Processus suivi pour le développement d'une nouvelle fonctionnalité</li>
        <ol>
            <li>Définition du cahier des charges avec le product owner ou l'équipe métier</li>
            <ul>
                <li>Définition du besoin</li>
                <li>Spécification de la fonctionnalité et des sous-fonctionnalités attendues</li>
                <li>Spécification de la qualité attendue</li>
                <li>Estimation du délai</li>
                <li>Documentation pour tracabilité</li>
            </ul>
            <li>Synchronisation avec le(s) dev(s) front si la fonctionnalité l'implique (cas le plus courant)</li>
            <ul>
                <li>Définition de la rêquete attendue par le back (request body, request headers, query params, etc...)</li>
                <li>Définition de la réponse attendue par le front (body, headers, status codes, cookies, etc...)</li>
                <li>Documentation pour tracabilité</li>
            </ul>
            <li>Développement de la fonctionnalité ou bugfix</li>
            <li>Tests manuels via Swagger/Postman et le frontend (s'il existe déjà)</li>
            <li>Ecriture de tests unitaires et si possible fonctionnels, essentiellement pour prévenir d'éventuelles régressions</li>
            <li>Soumission du code pour review avant intégration au code existant</li>
            <li>Intégration dans environnement cloud de DEV (non-visible aux end users)</li>
            <li>Tests et validation par l'équipe métier</li>
            <li>Mise en production (si validé, sinon on recommence le cycle à l'étape 1 ou 3 en fonction des cas)</li>
        </ol>
    <li>Proposition d'amélioration</li>
    <p>Voir backend.app package</p>
    <li>Testing</li>
    <p>Voir backend.test package</p>
</ol>

<ol>
    <h3>
        Architecture du backend
    </h3>
</ol>

<ul>
    <li>Pré-requis</li>
    <p>Pour pouvoir s'intégrer à l'API le modèle doit:
        <ul>
            <li>- exposer une fonction de prédiction du style predict() (c'est toujours le cas avec Sklearn)</li>
            <li>- le modèle une fois entrainé doit pouvoir être sauvegardé et exporté</li>
            <li>- il faut que le modèle sauvegardé et exporté soit sérialisable pour que le backend puisse le recréer rapidement à l'initialisation du serveur par exemple sans avoir à ré-entrainer complètement le modèle à chaque appel</li>
        </ul>
    </p>
    <li>Architecture</li>
    <p>Pour prendre en compte les contraintes du Data Scientist je propose de:
        <ul>
            <li>Mettre en place un endpoint d'entrainement du modèle qui sauvegarde en base les paramètres de l'estimateur. Ainsi la miste à jour du modèle se fera de façon fluide</li>
            <li>Créer un enpoint de prédiction. Deux cas possible pour cet endpoint</li>
            <ul>
                <li>Le modèle est reconstruit à partir de ses paramètres sauvegardés en base au moment de l'initialisation du serveur. Auquel cas, à chaque mise à jour il faut relancer le serveur</li>
                <li>La reconstruction du modèle se fait à l'intérieur de l'endpoint. La contrepartie est que la performance de l'endpoint va en prendre un coup</li>
            </ul>
        </ul>
     </p>
</ul>

<h2>
    <ol>
        <li>Développement d'un nouveau endpoint</li>
    </ol>
</h2>

<p>Voir fichier sql_exercice.sql</p>

<h2>
    <ol>
        <li>Echange technique</li>
    </ol>
</h2>

<h3>Questions Git</h3>
<ol>
    <li>Changement de branche => git checkout branch_name</li>
    <li>Git stash sert à mettre en cache des changements dans l'index mais non commit pour facilement passer d'une branche à l'autre sans avoir à commit. Git stash peut ainsi aussi servir à transférer des changements en cours d'une branch à l'autre. Mais attention au conflits !</li>
    <li><a href="https://mviewerdoc.readthedocs.io/fr/latest/doc_contrib/git.html">Celui-ci</a> c'est un workflow assez standard et qui marche bien</li>
<ol>

<h3>Questions Docker</h3>
<ol>
    <li>Afficher tous les conteneurs docker => docker ps -a</li>
    <li>Afficher toutes les images docker => docker images</li>
    <li>Se connecter à un conteneur docker => docker exec container_name</li>
    <li>docker rmi my_image => Supprime une image</li>
    <li>Rôle d'un volume docker => Assurer la persistence des données</li>
    <li>Docker compose => Au préalable il faut définir une "recette" dans un fichier yaml ensuite en fonction de la version de docker il faut utiliser la commande docker-compose up ou docker compose up</li>
</ol>

<h3>Questions Docker</h3>
<p>Les tests unitaires servent à s'assurer que les différentes unités de codes fonctionnent, c'est-à-dire qu'elles ne contiennent pas d'erreurs flagrantes de syntaxe ou autre pouvant empêcher l'exécution par exemple. <br>
Les test fonctionnels eux servent à s'assurer que le code remplit sa fonction. Par exemple, dans le cadre d'un un modèle de ML, on peut avoir un test unitaire qui s'assure que le modèle est capable de faire une prédiction. En revanche, un test fonctionnel lui s'assurera elle que la prédiction est correcte ou du moins vraisemblable </p>

<h3>Questions gestionnaire de cache</h3>
<p>J'ai déjà utilisé un gestionnaire de cache pour faire du rate limiting par exemple qui est un moyen parmi d'autre de se protéger du scraping</p>

<h3>Questions Peer Review/Pull Request</h3>
<ol>
    <li>A quoi ça sert ?<li>
    <p>Les Peer Review et les Pull Requests servent à améliorer la qualité du code et à la rendre plus robuste. Deux développeurs valent mieux qu'un et le fait d'avoir son code relu par un pair permet souvent d'identifier des bugs pernicieux ou de repérer des mauvaises structures (bad code smells). Relire le code de quelqu'un d'autre permet d'explorer des parties de la solution sur lesquelles on a pas l'habitude de travailler et par conséquent de s'approprier une plus grande partie du code source</p>
    <li>Bonne pull request</li>
    <p>C'est une pull request qui répond à un problème(bug, refactoring) ou au développement d'une fonctionnalité, qui est documenté (i.e la request est accompagné d'un message résumant ce qui a été fait et en cohérence avec l'historique des messages de commits). C'est une pull request qui vient accompagné de tests automatiques qui viennent couvrir les nouveaux pans de code développés et avec un reviewer désigné, le tout dans un timing adécuat</p>
    <li>Bonne peer review</li>
    <p>Une bonne peer review est une review qui identifie les points d'amélioration voir les points problématiques du code soumis et où le reviewer est bien veillant vis à vis de son collègue et commente le code en distinguant bien les bugs avérés, des bugs potentiels, les changements qu'il serait bien d'avoir des changements nécessaires </p>
</ol>
