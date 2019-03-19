% include('header.tpl', title='Street GAMES')
<body>
<h1> LAST GAME RESULT </h1>

<p>Adresse IP : {{game.machine_name.adress_ip}}</p>
<p>Nom de la machine : {{game.machine_name.nom_serveur}}</p>
<p>Nom du jeu : {{game.machine_name.game}}</p>
<p>Date et heure début de jeu : {{game.start_game}}</p>
<p>Gagnant : {{game.winner}}</p>

% include('footer.tpl')
</body>