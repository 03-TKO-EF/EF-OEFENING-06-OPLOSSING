import FreeSimpleGUI as sg

from .dlgcontact_layout import dlgContactLayout
from .init_layout import vensterTitel

class DlgContact:
    def __init__(self):
        pass

    def toon(self, mode, oContact, oContactLijst):
        venster = sg.Window(
            title = vensterTitel,
            layout = dlgContactLayout(),
            disable_close = True,
            resizable = False,
            finalize = True
        )

        venster['-INP-NAAM-'].update(oContact.naam)
        venster['-INP-TELEFOON-'].update(oContact.telefoon)
        venster['-BTN-VERWIJDER-'].update(visible  = True if mode == 'BEWERK' else False)

        while True:
            evt, vals = venster.read()

            match evt:
                case sg.WIN_CLOSED | '-BTN-ANNULEER-':
                    break

                case '-BTN-VERWIJDER-':
                    oContactLijst.verwijder(oContact)
                    break

                case '-BTN-BEWAAR-':
                    try:
                        oContactLijst.update(oContact, vals['-INP-NAAM-'], vals['-INP-TELEFOON-'])
                        break
                    except Exception as ex:
                        sg.popup_error(
                            ex,
                            title = 'FOUT...'
                        )

        venster.close()