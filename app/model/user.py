from mongoengine.fields import DateTimeField, IntField, StringField, URLField
from flask_mongoengine import MongoEngine
from marshmallow import fields
from flask_marshmallow import Marshmallow
db = MongoEngine()
ma = Marshmallow()

class User(db.Document):
    """Class for defining structure of user collection."""
    email = db.EmailField()
    first_name = db.StringField()
    last_name = db.StringField()
    _id = db.IntField()
    salutation =  db.StringField()
    maritalName = db.StringField()
    taxCountry = db.StringField()
    nationality = db.StringField()
    phone = db.StringField()
    nationality = db.StringField()
    dateBirth = db.DateTimeField()
    age = db.StringField()
    startDate = db.DateTimeField()
    maritalStatus = db.StringField()
    jobDescription = db.BooleanField()
    scoring = db.StringField()
    flags = db.StringField()
    aum = db.StringField()
    type = db.StringField()
    totalEstWealth = db.StringField()
    estWealthRealEstate = db.StringField()
    estWealthProfessional = db.StringField()
    estWealthFinancial = db.StringField()
    annualIncome = db.StringField()
    incomeRealEstate = db.StringField()
    incomeProfessional = db.StringField()
    annualSpending = db.StringField()
    familyRelationships = db.ListField(StringField(max_length=50))
    #bankRelationships = db.ListField(EmbeddedDocumentField(StringField))
    # externalBusinessRelationships = db.MapField()
    # externalRelationships = db.MapField()



#     date = DateTimeField(required=True)
#     date_str = StringField(max_length=10, required=True)
#     commentsUrl = URLField(required=False)



# Serialization/Deserialization schema definition
class UserSchema(ma.Schema):

    first_name = fields.String(required=False)


