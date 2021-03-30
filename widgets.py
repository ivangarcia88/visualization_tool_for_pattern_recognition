import PySimpleGUI as sg

image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

layout = [
    
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="dataset"),
        #sg.FolderBrowse(),
        sg.FileBrowse(),
    ],
    [sg.Radio('No transform (Fast)', 'speed', default=True, key="sp1"), sg.Radio('UMAP (Average)', 'speed', key="sp2" ), sg.Radio('UMAP + ICN (Slow)', 'speed', key="sp3" ) ],
    [sg.Radio('2D', 'dim', default=True, key="p2d"), sg.Radio('3D (interaction not available)', 'dim', key="p3d" )],
    [sg.B('Plot'), sg.B('Exit')],
    
    [sg.Canvas(key='controls_cv')],
    [sg.T('Figure:')],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # it's important that you set this size
                       size=(500 * 2, 400)
                       )]
        ],
        background_color='#DAE0E6',
        pad=(0, 0)
    )],
    [sg.T("Image1"),sg.Image(key="-MAIN-IMAGE-", filename="default-img.png"),
     sg.T("Image2"),sg.Image(key="-NN1-IMAGE-", filename="default-img.png"),
     sg.T("Image3"),sg.Image(key="-NN2-IMAGE-", filename="default-img.png")],
    #[sg.T("Image"),sg.Image(key="-IMAGE-", filename="default-img.png")],
   
]
