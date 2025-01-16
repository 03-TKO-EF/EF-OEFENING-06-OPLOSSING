import FreeSimpleGUI as sg

font = ['Calibri', 14]

fontItalic = font.copy()
fontItalic.append('italic')

fontKop = font.copy()
fontKop[1] = 20
fontKop.append('bold')

sg.set_options(
    icon = 'assets/favicon.ico',
    font = tuple(font),
    margins = (15,15),
    use_ttk_buttons = True
)

sg.theme('DefaultNoMoreNagging')

kolomLinks = sg.Column(
    layout = [
        [
            sg.Frame(
                title = 'TOP 30',
                layout = [
                    [
                        sg.Listbox(
                            values = [],
                            key = '-LBX-TOP30-',
                            select_mode = sg.LISTBOX_SELECT_MODE_SINGLE,
                            enable_events = True,
                            no_scrollbar = False,
                            size = (30, 15)
                        )
                    ]
                ]
            )
        ]
    ]
)

kolomRechts = sg.Column(
    layout = [
            [
                sg.Text(
                    text = 'Titel',
                    font = ('Calibri', 12, 'italic'),
                    size = (12,1)
                ),
                sg.Text(
                    text = '',
                    key = '-TXT-TITEL-',
                    font = ('Calibri', 12, 'roman bold'),
                    expand_x = True
                )
            ],
            [
                sg.Text(
                    text = 'Performer',
                    font = ('Calibri', 12, 'italic'),
                    size = (12,1)
                ),
                sg.Text(
                    text = '',
                    key = '-TXT-PERFORMER-',
                    font = ('Calibri', 12, 'roman bold'),
                    expand_x = True
                )
            ],
            [
                sg.Text(
                    text = '',
                    font = ('Calibri', 12, 'italic'),
                    size = (12,1)
                ),
                sg.Image(
                    size = (250,250),
                    key = '-IMG-FOTO-'
                )
            ]
        ],
        size = (400, 300)
)

def appLayout():
    return [
        # -- RIJ 1
        [
            sg.Push(),
            sg.Image(
                source = 'assets/logo.png'
            ),
            sg.Text(
                text = 'TOP 30',
                font = tuple(fontKop)
            ),
            sg.Push()
        ],
        # -- RIJ 2
        [
            sg.HorizontalSeparator(
                pad = (0, 16)
            )
        ],
        # -- RIJ 3
        [
            kolomLinks,
            sg.VerticalSeparator(
                pad = (15, 0)
            ),
            kolomRechts
        ],
        # -- RIJ 4
        [
            sg.HorizontalSeparator(
                pad = (0, 16)
            )
        ],
        # -- RIJ 5
        [
            sg.Push(),
            sg.Button(
                button_text = 'Afsluiten',
                key = '-BTN-AFSLUITEN-',
                size = (10, 1)
            )
        ]
    ]