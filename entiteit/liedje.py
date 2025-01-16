class Liedje:
    def __init__(self, performer:str, titel:str, foto:str) -> None:
        '''
        constructor

        :param performer:str
        :param titel:str
        :param foto:str
        :return :None

        >>> l = Liedje('Tyla','On and on','tyla.jpg')
        '''
        self._performer = performer
        self._titel = titel
        self._foto = foto

    @property
    def performer(self) -> str:
        '''
        property performer: levert de naam van de performer

        :return str

        >>> l = Liedje('Tyla','On and on','tyla.jpg')
        >>> l.performer
        'Tyla'
        '''
        return self._performer

    @property
    def titel(self) -> str:
        '''
        property titel: levert de titel van het liedje

        :return str

        >>> l = Liedje('Tyla','On and on','tyla.jpg')
        >>> l.titel
        'On and on'
        '''
        return self._titel

    @property
    def foto(self) -> str:
        '''
        property foto: levert de bestandsnaam van de correspondrende foto

        :return str

        >>> l = Liedje('Tyla','On and on','tyla.jpg')
        >>> l.foto
        'tyla.jpg'
        '''        
        return self._foto
    
    def __str__(self) -> str:
        '''
        string representatie van de klasse

        :return :str
        '''
        return f'{self._performer}: {self._titel}'
    
    def __repr__(self) -> str:
        '''
        representeert instantie van de klasse

        >>> l = Liedje('Tyla','On and on','tyla.jpg')
        >>> repr(l)
        'Liedje("Tyla", "On and on", "tyla.jpg")'
        '''
        return f'{self.__class__.__name__}("{self._performer}", "{self._titel}", "{self._foto}")'
    
if __name__ == '__main__':
    from doctest import testmod
    testmod()