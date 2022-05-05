import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import space_reduction as sr
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from matplotlib.colors import ListedColormap
import os.path
#import matplotlib as mpl
#from mpl_toolkits.mplot3d import Axes3D, proj3d

#Function that process and display information of clicked instances
def click2D(event, window, values, neigh, y, classes, limg):
    k = 3
    position = (event.xdata, event.ydata)
    q = neigh.kneighbors([ position ], k, return_distance=True)
    #print(q)
    dist = q[0][0][0]
    #ind = q[1][0][0]
    if(dist<0.05):
        #Information display
        index = q[1][0][0]
        colors = ['purple', 'yellow', 'blue', 'green', 'red', 'black', 'brown', 'orange']
        pointClass = classes[index]
        thisy = y[index]
        color = colors[thisy]
        window.Element('info').update(f"{color}: {pointClass}: {limg[index]}")
        #Images Display
        imgpath1 = "images/"+limg[q[1][0][0]]
        imgpath2 = "images/"+limg[q[1][0][1]]
        imgpath3 = "images/"+limg[q[1][0][2]]
        print(imgpath1)
        if(os.path.exists(imgpath1) and os.path.exists(imgpath1) and os.path.exists(imgpath1)):
            window["-MAIN-IMAGE-"].update(filename=imgpath1)
            window["-NN1-IMAGE-"].update(filename=imgpath2)
            window["-NN2-IMAGE-"].update(filename=imgpath3)
        else:
            print("Images not found")
            window["-MAIN-IMAGE-"].update(filename="notfound-img.png")
            window["-NN1-IMAGE-"].update(filename="notfound-img.png")
            window["-NN2-IMAGE-"].update(filename="notfound-img.png")
    else:
        window["-MAIN-IMAGE-"].update(filename="default-img.png")
        window["-NN1-IMAGE-"].update(filename="default-img.png")
        window["-NN2-IMAGE-"].update(filename="default-img.png")

#Draw figure on toolbar
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

#Create toolbar class
class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

#Create figure and scatter 
def plotData(Xp,y,dim,le):
    plt.figure()
    plt.subplots_adjust(left=0.04, right=0.98, top=0.98, bottom=0.04)
    fig = plt.gcf()
    DPI = fig.get_dpi()
    # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
    fig.set_size_inches(520 * 2 / float(DPI), 520 / float(DPI))
    # -------------------------------
    classes = list(le.classes_)
    colors = ['purple','yellow','blue','green','red','black','brown','orange']
    colors = colors[:len(classes)]
    lc = ListedColormap(colors)
    
    if(dim==2):
        ax = fig.add_subplot(111)
        scatter = ax.scatter(Xp[:, 0], Xp[:, 1], c=y, marker='.', alpha=0.3, s=75, cmap=lc)
        ax.legend(handles=scatter.legend_elements()[0], labels=classes)
        
    else:
        ax = fig.add_subplot(111, projection='3d')
        scatter = scatter = ax.scatter(Xp[:, 0], Xp[:, 1], Xp[:, 2], c=y, marker='.', alpha=0.3, s=75, cmap=lc)  # , cmap=colors)
        ax.legend(handles=scatter.legend_elements()[0], labels=classes)
    return ax, fig

#Function used to select manage correct parameters of transformation
def plotfunc(window,dataset,speed,dim):
    print(dataset,speed,dim)
    X,y,classes,le,limg = sr.dataPrePro(dataset)
    if(speed==0):
        pca = PCA(n_components=dim)
        X = sr.normalize(pca.fit_transform(X))
    elif(speed==1):
        X = sr.normalize(sr.umapTransfromData(X,y,dim=dim))
    else:
        X = sr.normalize(sr.umapICNNTransfromData(X,y,dim=dim))
    ax, fig = plotData(Xp=X,y=y,dim=dim,le=le)
    print("X shape", X.shape)
    neigh = NearestNeighbors(n_neighbors=3)
    neigh.fit(X)
    print(X.shape)
    draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
    return ax, fig, neigh, y, classes, limg