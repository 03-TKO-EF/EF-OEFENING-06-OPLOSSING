import FreeSimpleGUI as sg
from . import init_layout
from .init_layout import vensterTitel

from .app_layout import appLaylout
from entiteit.contactlijst import ContactLijst
from .dlgcontact import DlgContact

class App:
    def __init__(self):
        self._contactLijst = ContactLijst()

    def toon(self):
        venster = sg.Window(
            title = vensterTitel,
            layout = appLaylout(),
            disable_close = True,
            resizable = False,
            finalize = True
        )

        venster['-LBX-CONTACTEN-'].update(values = self._contactLijst.lijst())
        venster['-TXT-AANTAL-'].update(str(self._contactLijst.aantal))

        while True:
            evt, vals = venster.read()

            match evt:
                case sg.WIN_CLOSED | '-BTN-AFSLUITEN-':
                    self._contactLijst.bewaar()
                    break

                case '-RBN-NAAM-':
                    self._contactLijst.sorteer('NAAM')
                    venster['-LBX-CONTACTEN-'].update(values = self._contactLijst.lijst())

                case '-RBN-TELEFOON-':
                    self._contactLijst.sorteer('TELEFOON')
                    venster['-LBX-CONTACTEN-'].update(values = self._contactLijst.lijst())

                case '-BTN-NIEUW-':
                    self._update(venster, 'NIEUW', self._contactLijst.nieuw(), self._contactLijst)

                case '-LBX-CONTACTEN-':
                    self._update(venster, 'BEWERK', vals['-LBX-CONTACTEN-'][0], self._contactLijst)

        venster.close()

    def _update(self, venster, mode, oContact, oContactLijst):
        dlgContact = DlgContact()
        dlgContact.toon(mode, oContact, oContactLijst)

        venster['-LBX-CONTACTEN-'].update(values = self._contactLijst.lijst())
        venster['-TXT-AANTAL-'].update(str(oContactLijst.aantal))