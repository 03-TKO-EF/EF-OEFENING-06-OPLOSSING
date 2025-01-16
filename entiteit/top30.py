from .liedje import Liedje
import json

class Top30:
    def __init__(self) -> None:
        '''
        constructor
        - initieert de eigenschap _collectie
        - leest het JSON-bestand 'top30.json' uit
        - maakt van elk liedje in het bestand een instantie van 
          de klasse Liedje aan en voeg toe aan _collectie
        '''
        self._collectie = []

        with open('data/top30.json', 'rt') as bestand:
            lijst = json.load(bestand)
            for item in lijst['top30']:
                oLiedje = Liedje(item['performer'], item['titel'], item['foto'])
                self._collectie.append(oLiedje)
                
    def lijst(self) -> list:
        '''
        levert de inhoud van de eigenschap _collectie op
        '''
        return self._collectie