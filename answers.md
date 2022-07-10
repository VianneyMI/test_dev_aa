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

<h3>
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
</h3>