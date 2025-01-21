import FreeSimpleGUI as sg

fntStandaard = ('Calibri', 14)
fntKop = ('Calibri', 24, 'bold')

vensterTitel = 'CONTACTEN'

def vensterKop():
    return [
        sg.Push(),
        sg.Image(
            source = 'assets/logo.png'
        ),
        sg.Text(
            text = 'CONTACTEN',
            font = fntKop
        ),
        sg.Push()
    ]

def horizontaal():
    return [
        sg.HorizontalSeparator(
            pad = (10, 0)
        )
    ]

sg.theme('DefaultNoMoreNagging')

sg.set_options(
    icon = 'assets/favicon.ico',
    font = fntStandaard
)