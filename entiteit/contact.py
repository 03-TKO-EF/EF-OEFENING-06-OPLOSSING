import re

class Contact:
    def __init__(self, naam:str, telefoon:str, sorteerMode:str) -> None:
        '''
        constructor

        :param naam:str
        :param telefoon:str
        :param sorteerMode:str 
        '''
        self._sorteerMode = sorteerMode
        self._naam = naam
        self._telefoon = telefoon

    @property
    def naam(self) -> str:
        '''
        getter, levert de inhoud van de eigenschap _naam

        :return :str
        '''
        return self._naam
    
    @naam.setter
    def naam(self, naam: str) -> None:
        '''
        setter, zet de inhoud van de eigenschap _naam

        :param naam:str
        '''
        if type(naam) != str:
            raise Exception('Naam moet van het type string zijn...')
        
        naam = naam.strip()

        if len(naam) == 0:
            raise Exception('Naam is een verplicht veld')
        
        self._naam = naam.upper()

    @property
    def telefoon(self) -> None:
        '''
        getter, levert de inhoud van de eigenschap _telefoon

        :return :str
        '''
        return self._telefoon
    
    @telefoon.setter
    def telefoon(self, telefoon: str) -> None:
        '''
        setter, zet de inhoud van de eigenschap _telefoon

        :param telefoon:str
        '''
        telefoon = telefoon.strip()
        if not re.search('^((\+|00)32|0)?4[6789]\d{7}$', telefoon):
            raise Exception('Telefoonnummer is niet correct...')
        
        self._telefoon = telefoon
    
    def sorteer(self, sorteerMode:str) -> None:
        '''
        zet de inhoud van de eigenschap _sorteerMode

        :param sorteerMode:str
        '''
        self._sorteerMode = sorteerMode
        
    def __str__(self) -> str:
        '''
        tekst representatie van de klasse

        :return :str
        '''
        if self._sorteerMode == 'NAAM':
            return f'{self._naam} | {self._telefoon:>16}'
        else:
            return f'{self._telefoon:>16} | {self._naam}'
    
    def __repr__(self) -> str:
        '''
        string om object te hermaken

        :return :str
        '''
        return f'{type(self).__name__}(naam={self._naam}, telefoon={self._telefoon})'

    '''
    magische methode om twee objecten te vergelijken bij sorteren
    naargelang de inhoud van de eiegsnchap _sorteerMode
    '''
    def __lt__(self, obj):
        if self._sorteerMode == 'NAAM':
            return self._naam < obj._naam
        else:
            return self._telefoon < obj._telefoon  

    def __le__(self, obj):
        if self._sorteerMode == 'NAAM':
            return self._naam <= obj._naam
        else:
            return self._telefoon <= obj._telefoon

    def __gt__(self, obj):
        if self._sorteerMode == 'NAAM':
            return self._naam > obj._naam
        else:
            return self._telefoon > obj._telefoon

    def __ge__(self, obj):
        if self._sorteerMode == 'NAAM':
            return self._naam >= obj._naam
        else:
            return self._telefoon >= obj._telefoon

    def __eq__(self, obj):
        if self._sorteerMode == 'NAAM':
            return self._naam == obj._naam
        else:
            return self._telefoon == obj._telefoon