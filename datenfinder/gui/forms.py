"""
Citizen Date Search / Input form
"""
from django.forms import ModelForm, CharField, ChoiceField
from .models import CitizenDate
import hashlib

DATE_TYPES = [
    ('telephone', 'Telefonnummer'),
    ('e-mail', 'E-Mail-Adresse'),
    ('zipcode', 'Postleitzahl'),
]

class CitizenDateForm(ModelForm):
    """
    Search form for citizen date types
    """
    citizen_name = CharField(label="Bürger:innen-Name")
    date_type = ChoiceField(
        required=True,
        choices=DATE_TYPES,
        label="Datumstyp")
    owner_new = CharField(label="Amt (*)", required=False)
    type_hash = None
    owner = None

    class Meta:
        model = CitizenDate
        fields = ["citizen_name", "date_type", "owner_new"]

    def is_valid(self):
        print(self.data)
        if 'citizen_name' in self.data and 'date_type' in self.data:
            name_and_type = self.data["citizen_name"] + self.data["date_type"]
            self.type_hash = hashlib.sha256(name_and_type.encode('utf-8')).hexdigest()
            
        if self.type_hash is not None and 'owner_new' in self.data and 'citizen_data_enter' in self.data:
            self.owner = self.data["owner_new"]
            return True
        else:
            return False

    def save(self):
        instance = CitizenDate()
        instance.type_hash = self.type_hash
        instance.owner = self.owner
        instance.save()
        return True
