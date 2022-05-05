import PySimpleGUI as sg
import visplot as vp
import widgets as w

window = sg.Window('Graph with controls', w.layout)
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):  # always,  always give a way out!
        break
    elif event == 'Plot':
        dataset = values["dataset"]
        if(dataset==None or dataset==''):
            sg.Popup('Selecciona un dataset', 'Selecciona un dataset valido')
        else:
            speed = values["sp1"]*0 + values["sp2"]*1 + values["sp3"]*2  #0 fast, 1 slow
            dim = 2 + values["p3d"]*1 #Setting the number of dimension set
            ax, fig, neigh, y, classes, limg = vp.plotfunc(window,dataset,speed,dim) #Function to call plot
            if(dim==2): #Call to evaluate clicked point
                position = fig.canvas.mpl_connect('button_press_event', lambda event: vp.click2D(event, window, values, neigh, y, classes, limg))
window.close()