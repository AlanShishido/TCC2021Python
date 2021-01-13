import peewee
from choices import DatabaseInfo as DB

db = peewee.SqliteDatabase(DB.TABLE_NAME)

class BaseModel(peewee.Model):

    class Meta:
        database = db

class Gardens(BaseModel):
    name = peewee.CharField(unique=True)
    number = peewee.IntegerField()

class LettuceDatas(BaseModel):
    garden = peewee.ForeignKeyField(Gardens)
    acquired_time = peewee.TimeField()
    ph = peewee.FloatField()
    tds = peewee.FloatField()
    ambient_temp = peewee.FloatField()
    water_temp = peewee.FloatField()
    



if __name__ == '__main__':
    try:
        Gardens.create_table()
        print("Tabela 'Horta' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Horta' ja existe!")

    try:
        LettuceDatas.create_table()
        print("Tabela 'Dados da Alface' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Dados da Alface' ja existe!")