from mongoengine import Document, StringField , IntField, FloatField
class Post(Document):
    fullname = StringField()
    email= StringField()
    username = StringField()
    password= IntField