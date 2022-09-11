import PySimpleGUI as sg



def border_frame(elem):
    return sg.Column([[elem]], pad=(3, 3), background_color='#D7A700')

def window():
    layout_frame1 = [
        [
            sg.Frame('', [
                [sg.Text('Плейлисти', background_color='#2B2B2B', text_color='#D7A700', justification='center', size=(132,20))]
            ], pad=(6,6), size=(132, 20), background_color='#2B2B2B', border_width=0)
        ],
        [
            sg.Frame('', [], pad=(6,0), size=(132, 306), background_color='#2B2B2B', border_width=0)
        ]
    ]

    layout_frame2 = [
        [
            sg.Frame('', [
                [sg.Text('', background_color='#2B2B2B', text_color='#D7A700', justification='center', size=(432,20))]
            ], pad=(6,6), size=(432, 20), background_color='#2B2B2B', border_width=0)
        ],
        [
            sg.Frame('', [], pad=(6,0), size=(432, 306), background_color='#2B2B2B', border_width=0)
        ]
    ]

    layout_frame3 = []

    layout = [
        [
            border_frame(sg.Frame('', layout_frame1, pad=(1, 1), size=(144, 344), background_color='#353535', border_width=0)),
            border_frame(sg.Frame('', layout_frame2, pad=(1, 1), size=(444, 344), background_color='#353535', border_width=0))
        ],
        [
            border_frame(sg.Frame('', layout_frame3, pad=(1,1), size=(594, 44), background_color='#353535', border_width=0))
        ],
    ]

    window = sg.Window('Плеєр', layout, finalize=True, background_color='#353535')
    window.size = (600, 400)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()