<!doctype html>
<html lang="fr">
<head class="container-fluid">
    <meta charset="utf-8>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
   <title>GAMES</title>
</head>
<body>


<div class="container">
  <h2>Striped Rows</h2>
  <p>The .table-striped class adds zebra-stripes to a table:</p>

  <table class="table table-striped">

    <thead>
      <tr>
        <th>adresse IP</th>
        <th>Nom du serveur</th>
        <th>Nom du jeu</th>

      </tr>
    </thead>
       % for i in data_list:
    <tbody>
      <tr>
        <td>{{i.adress_ip}}</td>
        <td>{{i.nom_serveur}}</td>
        <td>{{i.game}}</td>

      </tr>
    </tbody>
  </table>
    %end
</div>

</header>


<footer>
</footer>
</body>
</html>