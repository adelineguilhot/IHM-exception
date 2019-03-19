import peewee
import datetime
import settings


mysql_db = peewee.MySQLDatabase(host=settings.DB_HOST, user=settings.DB_USER, password=settings.DB_PASSWORD, database=settings.DB_DATABASE)


class Base(peewee.Model):

    class Meta:
        database = mysql_db


class GameServer(Base):
    adress_ip = peewee.CharField(unique=True, max_length=255)
    nom_serveur = peewee.CharField(unique=True, max_length=255)
    game = peewee.CharField(max_length=20)
    max_player_delay = peewee.IntegerField()
    max_coin_blink_delay = peewee.IntegerField()
    victory_blink_delay = peewee.IntegerField()
    level = peewee.IntegerField()
    player_1_color = peewee.CharField()
    player_2_color = peewee.CharField()

    def get_config(self, msg_ID):
        reponse = {"Msg type": "CONFIG",
                   "Msg ID": msg_ID,
                   "Max player delay": self.max_player_delay,
                   "Max coin blink delay": self.max_coin_blink_delay,
                   "Victory blink delay": self.victory_blink_delay,
                   "Level": self.level,
                   "Player1 color": self.player_1_color,
                   "Player2 color": self.player_2_color}
        return reponse

    def __str__(self):
        return self.nom_serveur

    @classmethod
    def list_serveur(cls):
        """Affiche tous les serveurs connues. Il lui faut les paramétres nom_serveur
         et elle renvoie une liste avec tous les serveurs connues"""
        return cls.select()


class ReceiverMessage(Base):
    msg_id = peewee.IntegerField()
    msg_machine = peewee.ForeignKeyField(GameServer, backref='message_recu')
    msg = peewee.CharField(max_length=1000)
    date_message = peewee.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.msg_machine.nom_serveur + " " + str(self.msg_id) + " " + str(self.date_message) + " " + self.msg

    @classmethod
    def liste_message(cls, nom):
        """Affiche la liste des messages par date d'arrivée.
        Il lui faut les parametres msg_machine, msg et date_message. Elle renvoie la date, la machine et le message"""
        return cls.select().join(GameServer).order_by(cls.date_message).where(GameServer.nom_serveur == nom)


class StatsPerMatch(Base):
    machine_name = peewee.ForeignKeyField(GameServer, backref='stat_per_match')
    start_game = peewee.DateTimeField()
    duree = peewee.IntegerField()
    winner = peewee.CharField(max_length=255)

    @classmethod
    def stat_jour(cls):
        """"""
        return cls.select()


class StatsPerDay(Base):
    date = peewee.DateField()
    machine_name = peewee.ForeignKeyField(GameServer, backref='stat_per_day')
    nombre_partie = peewee.IntegerField()
    duree_moy_partie = peewee.IntegerField()
    joueur1_win = peewee.IntegerField()
    joueur2_win = peewee.IntegerField()
    egalite = peewee.IntegerField()


mysql_db.connect()
GameServer.create_table()
ReceiverMessage.create_table()
StatsPerMatch.create_table()
StatsPerDay.create_table()
GameServer.list_serveur()
ReceiverMessage.liste_message(ReceiverMessage.msg_machine)
#
# StatsPerDay.create(machine="serveur", nombre_partie=5, duree_moy_partie=52, joueur1_win=6, joueur2_win=4, egalite=3)
#
# for p in StatsPerDay.select():
#     print(type(p), ':', p.machine, p.nombre_partie, p.duree_moy_partie, p.joueur1_win, p.date)
