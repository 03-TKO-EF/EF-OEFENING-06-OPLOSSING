from .contact import Contact

import json
from os.path import exists

class ContactLijst:
    def __init__(self) -> None:
        '''
        constructor
        leest het JSON-bestand uit
        en maakt de corresponderende instanties van de klasse Contact toe
        '''
        self._contactLijst = []
        self._sorteerMode = 'NAAM'

        if exists('data/contacten.json'):
            with open('data/contacten.json', 'rt', encoding='utf-8') as bestand:
                lijst = json.load(bestand)['contactLijst']

                for item in lijst:
                    self._contactLijst.append(Contact(naam = item['naam'], telefoon = item['telefoon'], sorteerMode = self._sorteerMode))

    def nieuw(self) -> Contact:
        '''
        levert een nieuwe instantie van de klasse Contact

        :return :Contact
        '''
        oContact = Contact()
        oContact.sorteer(self._sorteerMode)
        return oContact
    
    def update(self, oContact:Contact, naam:str, telefoon:str) -> None:
        '''
        update de eigenschappen _naam en _telefoon van het object

        :param oContact:Contact
        :param naam:str
        :param telefoon:str
        '''
        if oContact not in self._contactLijst:
            self._contactLijst.append(oContact)

        oContact.naam = naam
        oContact.telefoon = telefoon

    def verwijder(self, oContact:Contact) -> None:
        '''
        verwijdert de betreffende instantie van Contact uit de _contactLijst

        :param oContact:Contact
        '''
        if oContact in self._contactLijst:
            self._contactLijst.remove(oContact)

    def lijst(self) -> list:
        '''
        sorteert _contactLijst
        en retourneert _contactLijst

        :return _contactLijst:list
        '''
        self._contactLijst = sorted(self._contactLijst)

        return self._contactLijst
    
    def sorteer(self, sorteerMode:str) -> None:
        '''
        zet de sorteerMode: 'NAAM' of 'TELEFOON'

        :param sorteerMode:str
        '''
        self._sorteerMode = sorteerMode

        for oContact in self._contactLijst:
            oContact.sorteer(sorteerMode)

    def bewaar(self) -> None:
        '''
        bewaart de inhoud van _contactLijst in het JSON-bestand
        '''
        lijst = []

        if len(self._contactLijst) > 0:
            for contact in self._contactLijst:
                lijst.append({
                    'naam': contact.naam,
                    'telefoon': contact.telefoon
                })

        with open('data/contacten.json', 'wt', encoding='utf-8') as bestand:
            json.dump({'contactLijst': lijst}, bestand, indent=4)

    @property
    def aantal(self) -> int:
        '''
        levert het aantal contact in _contactLijst

        :return :int
        '''
        return len(self._contactLijst)