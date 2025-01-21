import FreeSimpleGUI as sg

from .init_layout import vensterKop, horizontaal


def dlgContactLayout():
    return [
        # RIJ 1
        vensterKop(),
        # RIJ 2
        horizontaal(),
        # RIJ 3
        [
            sg.Text(
                text = 'Naam',
                size = (10, 1)
            ),
            sg.Input(
                default_text = '',
                size = (30, 1),
                key = '-INP-NAAM-'
            )
        ],
        # RIJ 4
        [
            sg.Text(
                text = 'Telefoon',
                size = (10, 1)
            ),
            sg.Input(
                default_text = '',
                size = (30, 1),
                key = '-INP-TELEFOON-'
            )
        ],
        # RIJ 5
        horizontaal(),
        # RIJ 6
        [
            sg.Push(),
            sg.Button(
                button_text = 'Verwijder',
                size = (10, 1),
                key = '-BTN-VERWIJDER-'
            ),
            sg.Button(
                button_text = 'Bewaar',
                size = (10, 1),
                key = '-BTN-BEWAAR-'
            ),
            sg.Button(
                button_text = 'Annuleer',
                size = (10, 1),
                key = '-BTN-ANNULEER-'
            )
        ]
    ]