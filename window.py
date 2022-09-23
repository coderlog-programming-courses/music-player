import PySimpleGUI as sg



def window():
    color = ['#FF0000', '#FFFFFF', '#7D7373', '#3E3838', '#212423']

    layout_frame4 = []
    layout_column_musics = [
        [
            sg.Image(filename='./button_image/change_music.png', background_color='#212423', pad=(0,0))
        ]
    ]
    layout_column_playlists = [
        [
            sg.Image(filename='./button_image/change_playlist.png', background_color='#212423', pad=(0,0)),           
        ]
    ]
    layout_frame2 = [
        [
            sg.Frame('', [[
                sg.Column(layout_column_playlists, key='column_playlists', pad=(0,0), background_color='#212423'),
                sg.Column(layout_column_musics, key='column_musics', visible=False, pad=(0,0), background_color='#212423')
            ]],
            background_color='#212423', pad=(0,0), size=(325, 465), border_width=0, key='frame'),
            sg.Frame('', layout_frame4, background_color='#3E3838', pad=(2,2), size=(325, 465), border_width=0),
        ]
    ]
    layout_frame1 = [
        [
            sg.Button('', button_color='#212423', mouseover_colors='#3E3838',
                                image_filename= './button_image/deactive_button_musics.png', image_size=(100, 35), image_subsample=1, border_width=0, key='musics'),
            sg.Button('', button_color='#212423', mouseover_colors='#3E3838',
                                image_filename= './button_image/active_button_playlists.png', image_size=(100, 35), image_subsample=1, border_width=0, key='playlists'),
        ],
    ]

    layout = [
        [
            sg.Frame('', layout_frame1, background_color='#212423', pad=(0,1), size=(650, 35), border_width=0)
        ],
        [
            sg.Frame('', layout_frame2, background_color='#212423', pad=(0,1), size=(650, 465), border_width=0)
        ],
    ]

    window = sg.Window('Плеєр', layout, finalize=True, background_color='#3E3838', margins=(0,0))
    #window.size = (800, 600)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'playlists':
            window['musics'].update(image_filename= './button_image/deactive_button_musics.png')
            window['playlists'].update(image_filename= './button_image/active_button_playlists.png')
            window['column_playlists'].update(visible=True)
            window['column_musics'].update(visible=False)
            window.refresh()
        elif event == 'musics':
            window['musics'].update(image_filename= './button_image/active_button_musics.png')
            window['playlists'].update(image_filename= './button_image/deactive_button_playlists.png')
            window['column_playlists'].update(visible=False)
            window['column_musics'].update(visible=True)
            window.refresh()


    window.close()

window()