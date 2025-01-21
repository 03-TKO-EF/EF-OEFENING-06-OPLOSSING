import FreeSimpleGUI as sg

from .init_layout import vensterKop, horizontaal

kolomLinks = sg.Column(
        layout = [
            [
                sg.Frame(
                    title = 'Contacten',
                    layout = [
                        [
                            sg.Listbox(
                                values = [],
                                size = (30, 20),
                                pad = (12, 12),
                                select_mode = sg.LISTBOX_SELECT_MODE_SINGLE,
                                key = '-LBX-CONTACTEN-',
                                enable_events = True
                            )
                        ]
                    ]
                )
            ]
        ]
    )


kolomRechts = sg.Column(
    layout = [
        # RIJ 1
        [
            sg.Text(
                text = 'Aantal contacten',
                size = (18,1)
            ),
            sg.Text(
                text = '0',
                key = '-TXT-AANTAL-',
                size = (8, 1),
                justification = 'right'
            )
        ],
        # RIJ 2
        [
            sg.HorizontalSeparator(
                pad = (0, 70)
            )
        ],
        # RIJ 3
        [
            sg.Text(
                text = 'Sorteer op'
            )
        ],
        # RIJ 4
        [
            sg.Radio(
                text = 'Naam',
                default = True,
                group_id = 'sorteer',
                enable_events = True,
                key = '-RBN-NAAM-',
                size = (8, 1)
            ),
            sg.Radio(
                text = 'Telefoon',
                group_id = 'sorteer',
                enable_events = True,
                key = '-RBN-TELEFOON-',
                size = (8, 1)
            ),
        ],
        # RIJ 5
        [
            sg.HorizontalSeparator(
                pad = (0, 70)
            )
        ],
        # RIJ 6
        [
            sg.Button(
                button_text = 'Nieuw',
                size = (26,2),
                key = '-BTN-NIEUW-'
            )
        ],
        # RIJ 7
        [
            sg.Button(
                button_text = 'Afsluiten',
                size = (26,2),
                key = '-BTN-AFSLUITEN-'
            )
        ]
    ]
)

def appLaylout():
    return [
        # RIJ 1
        vensterKop(),
        # RIJ 2
        horizontaal(),
        # RIJ 3
        [
            [
                kolomLinks,
                sg.VerticalSeparator(
                    pad = (5, 0)
                ),
                kolomRechts
            ]
        ],
    ]