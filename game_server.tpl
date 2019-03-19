% include('header.tpl', title='Street GAMES')
<body>

            <ul>
            % for i in data_list:
                <li><p>L'adresse IP est :<p>{{i.adress_ip}}</li>
                <li><p>Le nom du serveur est :</p>{{i.nom_serveur}}</li>
                <li><p>Le jeu utilisé est :</p>{{i.game}}</li>
                <a href="modification/{{i.nom_serveur}}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Modifier le Serveur</a>
                <br>
            % end
            </ul>

% include('footer.tpl')
</body>
