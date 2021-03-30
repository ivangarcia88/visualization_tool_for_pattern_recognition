import PySimpleGUI as sg
import visplot as vp
#import visimg as vi
import widgets as w

# ------------------------------- PySimpleGUI CODE

window = sg.Window('Graph with controls', w.layout)
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):  # always,  always give a way out!
        break
    elif event is 'Plot':
        # Plot image
        #window["-IMAGE-"].update(filename="fu.png")
        dataset = values["dataset"]
        if(dataset==None or dataset==''):
            sg.Popup('Selecciona un dataset', 'Selecciona un dataset valido')
        else:
            speed = values["sp1"]*0 + values["sp2"]*1 + values["sp3"]*2  #0 fast, 1 slow
            dim = 2 + values["p3d"]*1 
            fig, neigh, classes, limg = vp.plotfunc(window,dataset,speed,dim)
            if(dim==2):
                #Function by click position
                position = fig.canvas.mpl_connect('button_press_event', lambda event: vp.click2D(event, window, neigh, classes, limg))
                #Function by click instance
                #fig.canvas.mpl_connect('pick_event', vp.on_pick)
                
            #else:
            #    cid = fig.canvas.callbacks.connect('button_press_event', demo_format_coord)
window.close()