% include('header.tpl', title='Street GAMES')
<form action='' method='post'>
    <!--
        Fichier de modification de configuration d'un contrôleur de jeu.
        Adapter les variables ci-dessous selon votre modèle.
    -->
    adresse_ip :
<input type="text" name="adresse_ip" value="{{ config.adress_ip }}"> <br>

    nom du serveur :
    <input type="text" name="nom_serveur" value="{{ config.nom_serveur }}"> <br>

    Jeux :
    <select name="game">
      <option {{ "selected" if config.game == "morpion" else ""}} value="morpion">Morpion</option>
      <option {{ "selected" if config.game == "puissance 4" else ""}} value="puissance 4">Puissance 4</option>
   </select> <br>

    max player delay :
    <input type="number" name="max_player_delay" value="{{ config.max_player_delay }}"> <br>

    max coin blink delay :
    <input type="number" name="max_coin" value="{{ config.max_coin_blink_delay }}"> <br>

    Victory Blink delay :
    <input type="number" name="victory_blink_delay" value="{{ config.victory_blink_delay }}"> <br>

    Level :
    <input type="number" name="level" min="1" max="5" value="{{ config.level }}"> <br>

    Player 1 color :
    <select name="player1_color">
       <option {{ "selected" if config.player_1_color == "bleu" else "" }} value="bleu">Bleu</option>
       <option {{ "selected" if config.player_1_color == "vert" else ""}} value="vert">Vert</option>
       <option {{ "selected"  if config.player_1_color == "rouge" else ""}} value="rouge">Rouge</option>
    </select>
    <br>

    Player 2 color :
    <select name="player2_color">
       <option {{ "selected" if config.player_2_color == "bleu" else ""}} value="bleu">Bleu</option>
       <option {{ "selected" if config.player_2_color == "vert" else ""}} value="vert">Vert</option>
       <option {{ "selected" if config.player_2_color == "rouge" else ""}} value="rouge">Rouge</option>
    </select>
    <br> <br>

   <input type="reset">
   <input type="submit">
</form>

% include('footer.tpl')
