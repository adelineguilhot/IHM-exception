% include('header.tpl', title='Street GAMES')
<body>

<table class="table">
  <thead>
    <tr>
      <th scope="col">adresse IP</th>
      <th scope="col">nom du serveur</th>
      <th scope="col">jeu utilisé</th>
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
  % end
</table>
% include('footer.tpl')
</body>

