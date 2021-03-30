import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import space_reduction as sr
from sklearn.neighbors import NearestNeighbors


# ------------------------------- This is to include a matplotlib figure in a Tkinter canvas

def click2D(event, window, neigh, classes, limg):
    k = 3
    position = (event.xdata, event.ydata)
    q = neigh.kneighbors([ position ], k, return_distance=True)
    #print(q)
    dist = q[0][0][0]
    #ind = q[1][0][0]
    if(dist<0.1):
        imgpath1 = "images/"+limg[q[1][0][0]]
        imgpath2 = "images/"+limg[q[1][0][1]]
        imgpath3 = "images/"+limg[q[1][0][2]]
        window["-MAIN-IMAGE-"].update(filename=imgpath1)
        window["-NN1-IMAGE-"].update(filename=imgpath2)
        window["-NN2-IMAGE-"].update(filename=imgpath3)
    else:
        window["-MAIN-IMAGE-"].update(filename="default-img.png")
        window["-NN1-IMAGE-"].update(filename="default-img.png")
        window["-NN2-IMAGE-"].update(filename="default-img.png")
        
def on_pick(event):
    print(event.ind)
    #print (testData[event.ind], "clicked")
    #coll._facecolors[event.ind,:] = (1, 1, 0, 1)
    #coll._edgecolors[event.ind,:] = (1, 0, 0, 1)
    #fig.canvas.draw()

def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

def plotData(Xp,y,dim):
    #fig = plt.figure()
    plt.figure(1)
    fig = plt.gcf()
    DPI = fig.get_dpi()
    # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
    fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
    # -------------------------------
    
    if(dim==2):
        ax = fig.add_subplot(111)
        ax.scatter(Xp[:,0], Xp[:,1], c=y, marker='.', alpha=0.3, s=200)
    else:
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(Xp[:,0], Xp[:,1], Xp[:,2], c=y, marker='.', alpha=0.3)
        #plt.show()
    return fig

def plotAndEvaluate(Xp,y,dim,show=True):
    if(show):
        fig = plt.figure()
        if(dim==2):
            ax = fig.add_subplot(111)
            ax.scatter(Xp[:,0], Xp[:,1], c=y, marker='.', alpha=0.3)
        else:
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(Xp[:,0], Xp[:,1], Xp[:,2], c=y, marker='.', alpha=0.3)
        #plt.show()
    if(dim==2):
        return evplot(Xp[:,0:2],y,k=11),fig
    else:
        return evplot(Xp[:,0:3],y,k=11),fig



def plotfunc(window,dataset,speed,dim):
    print(dataset,speed,dim)
    #-plt.figure(1)
    #-fig = plt.gcf()
    #-DPI = fig.get_dpi()
    # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
    #-fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
    # -------------------------------
    X,y,classes,le,limg = sr.dataPrePro(dataset)
    if(speed==0):
        fig = plotData(X,y,dim)
        X = X[:,0:2]
    elif(speed==1):
        X =  sr.normalize(sr.umapTransfromData(X,y,dim=2))
        fig = plotData(X,y,dim=2)
    else:
        X =  sr.normalize(sr.umapICNNTransfromData(X,y,dim=2))
        fig = plotData(X,y,dim=2)
    neigh = NearestNeighbors(n_neighbors=3)
    neigh.fit(X)
    print(X.shape)
    draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
    return fig, neigh, classes, limg
    

