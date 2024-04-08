import peewee as pw

db = pw.SqliteDatabase('people.db')
class Person(pw.Model):
    name = pw.CharField()
    birthday = pw.DateField()
    is_relative = pw.BooleanField()

    class Meta:
        database = db

class Pet(pw.Model):
    owner = pw.ForeignKeyField(Person, related_name='pets')
    name = pw.CharField()
    animal_type = pw.CharField()
    
    class Meta:
        database = db

def create_and_connect():
    db.connect()
    db.create_tables([Person,Pet],safe=True)


if __name__ == "__main__":
    create_and_connect()