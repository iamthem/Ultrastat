# This file handles all the graphical stuff  f
from rename import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import *
from pandastable import Table, TableModel
import pandas as pd
import main
from rename import *
from PIL import ImageTk 
from PIL import Image 
import numpy as np 

# First class and overall framework of object oriented TKinter taken from 
# https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/

class ultrastat(Tk):
    def __init__(self, *args, **kwargs): 

        Tk.__init__(self, *args, **kwargs)

        container = Frame(self, height = 500, width = 500)

        container.pack(side="top", fill="both", expand = True)

        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Prem, Liga, Bundesliga, SerieA, 
                HeadToHeadLiga, HeadToHeadBundes, HeadToHeadPrem, 
                HeadToHeadSerieA):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        tifo = Image.open('BVB.png')
        self.t = ImageTk.PhotoImage(tifo)
        title = Image.open('title.png')
        self.ti = ImageTk.PhotoImage(title)

        select = Image.open('Select.png')
        self.select= ImageTk.PhotoImage(select) 

        league = Image.open('League.png')
        self.league = ImageTk.PhotoImage(league) 

        imageLabel = Label(self, image=self.t)
        imageLabel.pack()

        titleLable = Label(self, image=self.ti)
        titleLable.pack()

        selectLable = Label(self, image=self.select)
        selectLable.place(x=310,y=650)
        
        leagueLable = Label(self, image=self.league)
        leagueLable.place(x=308, y=720)

        frame1 = Frame(self, bg = 'red')
        frame1.pack(side = LEFT, fill = BOTH)

        b = Button(frame1, text='Premier League', font='Times 13', command=
                                lambda : controller.show_frame(Prem))
        b.pack(pady = 20, padx = 20)

        c = Button(frame1, text='La Liga', font = 'Times 13', command=
                                lambda : controller.show_frame(Liga))
        c.pack(pady = 20, padx = 20)

        frame2 = Frame(self, bg = 'yellow')
        frame2.pack(side = RIGHT, fill = BOTH)

        d = Button(frame2, text='Serie A', font = 'Times 13', command=
                                lambda : controller.show_frame(SerieA))
        d.pack(pady = 20, padx = 20)

        e = Button(frame2, text='Bundesliga', font='Times 13', command=
                                lambda : controller.show_frame(Bundesliga))
        e.pack(pady = 20, padx = 20)

class Liga(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        label = Label(self, text='La Liga Matchday 15')
        label.pack(padx=10, pady=10)

        frame1 = Frame(self, bg = 'red')
        frame1.pack(fill = BOTH)
        
        def drawTable():
            df = main.predict('liga', 15)

            self.table = pt = Table(frame1, dataframe=df,
            showtoolbar=False, showstatusbar=True)

            pt.show()
       
        drawTable()

        button1 = Button(self, text='Back to Leagues', command =
            lambda : controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text='Head to Head', command =
            lambda : controller.show_frame(HeadToHeadLiga))
        button2.pack()

        # Graphing Help from this guy 
        # https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/
        # and this guy 
        #https://stackoverflow.com/questions/31549613/displaying-a-matplotlib-bar-chart-in-tkinter
        def callback():
            renamedList = [] 
            for i in main.getMatchday('liga', 15):
                renamedList.append([renameWrapper('goals', 'liga', i[0]), renameWrapper('goals', 'liga', i[1])])

            f = Figure(figsize=(5,5), dpi=100)

            x = np.arange(6)

            a = f.add_subplot(111)

            homeGoals = [float(str(main.predictGameProb('liga', 
                renamedList[0][0], renamedList[0][1])[i][0]).split()[1].rstrip()) for i in range(6)]

            width = .2

            rects1 = a.bar(x, homeGoals, width)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.show()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

            button4 = Button(self, text = 'Delete Graph', command = 
                    lambda: canvas.get_tk_widget().destroy())
            button4.pack()


        button3 = Button(self, text = 'Chance any team in this league scores N goals', command = callback)
        button3.pack()

class Prem(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        label = Label(self, text='Premier League Matchday 16')
        label.pack(padx=10, pady=10)

        frame1 = Frame(self, bg = 'red')
        frame1.pack(fill = BOTH)
        
        def drawTable():
            df = main.predict('prem', 16)

            self.table = pt = Table(frame1, dataframe=df,
            showtoolbar=False, showstatusbar=True)

            pt.show()
       
        drawTable()

        button1 = Button(self, text='Back to Leagues', command =
            lambda : controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text='Head to Head', command =
            lambda : controller.show_frame(HeadToHeadPrem))
        button2.pack()

        # Graphing Help from this guy 
        # https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/
        # and this guy 
        #https://stackoverflow.com/questions/31549613/displaying-a-matplotlib-bar-chart-in-tkinter
        def callback():
            renamedList = [] 
            for i in main.getMatchday('prem', 16):
                renamedList.append([renameWrapper('goals', 'prem', i[0]), renameWrapper('goals', 'prem', i[1])])

            f = Figure(figsize=(5,5), dpi=100)

            x = np.arange(6)

            a = f.add_subplot(111)

            homeGoals = [float(str(main.predictGameProb('prem', 
                renamedList[0][0], renamedList[0][1])[i][0]).split()[1].rstrip()) for i in range(6)]

            width = .2

            rects1 = a.bar(x, homeGoals, width)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.show()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

            button4 = Button(self, text = 'Delete Graph', command = 
                    lambda: canvas.get_tk_widget().destroy())
            button4.pack()


        button3 = Button(self, text = 'Chance any team in this league scores N goals', command = callback)
        button3.pack()

class SerieA(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        label = Label(self, text='Serie A Matchday 16')
        label.pack(padx=10, pady=10)

        frame1 = Frame(self, bg = 'red')
        frame1.pack(fill = BOTH)
        
        def drawTable():
            df = main.predict('serie A', 16)

            self.table = pt = Table(frame1, dataframe=df,
            showtoolbar=False, showstatusbar=True)

            pt.show()
       
        drawTable()

        button1 = Button(self, text='Back to Leagues', command =
            lambda : controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text='Head to Head', command =
            lambda : controller.show_frame(HeadToHeadSerieA))
        button2.pack()

        # Graphing Help from this guy 
        # https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/
        # and this guy 
        #https://stackoverflow.com/questions/31549613/displaying-a-matplotlib-bar-chart-in-tkinter
        def callback():
            renamedList = [] 
            for i in main.getMatchday('serie A', 16):
                renamedList.append([renameWrapper('goals', 'serie A', i[0]), renameWrapper('goals', 'serie A', i[1])])

            f = Figure(figsize=(5,5), dpi=100)

            x = np.arange(6)

            a = f.add_subplot(111)

            homeGoals = [float(str(main.predictGameProb('serie A', 
                renamedList[0][0], renamedList[0][1])[i][0]).split()[1].rstrip()) for i in range(6)]

            width = .2

            rects1 = a.bar(x, homeGoals, width)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.show()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

            button4 = Button(self, text = 'Delete Graph', command = 
                    lambda: canvas.get_tk_widget().destroy())
            button4.pack()


        button3 = Button(self, text = 'Chance any team in this league scores N goals', command = callback)
        button3.pack()

class Bundesliga(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        label = Label(self, text='Bundesliga Matchday 15')
        label.pack(padx=10, pady=10)

        frame1 = Frame(self, bg = 'red')
        frame1.pack(fill = BOTH)
        
        def drawTable():
            df = main.predict('bundes', 15)

            self.table = pt = Table(frame1, dataframe=df,
            showtoolbar=False, showstatusbar=True)

            pt.show()
       
        drawTable()

        button1 = Button(self, text='Back to Leagues', command =
            lambda : controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text='Head to Head', command =
            lambda : controller.show_frame(HeadToHeadBundes))
        button2.pack()

        # Graphing Help from this guy 
        # https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/
        # and this guy 
        #https://stackoverflow.com/questions/31549613/displaying-a-matplotlib-bar-chart-in-tkinter
        def callback():
            renamedList = [] 
            for i in main.getMatchday('bundes', 15):
                renamedList.append([renameWrapper('goals', 'bundes', i[0]), renameWrapper('goals', 'bundes', i[1])])

            f = Figure(figsize=(5,5), dpi=100)

            x = np.arange(6)

            a = f.add_subplot(111)

            homeGoals = [float(str(main.predictGameProb('bundes', 
                renamedList[0][0], renamedList[0][1])[i][0]).split()[1].rstrip()) for i in range(6)]

            width = .2

            rects1 = a.bar(x, homeGoals, width)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.show()
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

            button4 = Button(self, text = 'Delete Graph', command = 
                    lambda: canvas.get_tk_widget().destroy())
            button4.pack()


        button3 = Button(self, text = 'Chance any team in this league scores N goals', command = callback)
        button3.pack()

class HeadToHeadBundes(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='Head To Head Bundesliga')
        label.pack(padx=10, pady=10)
        label4 = Label(self, text='Copy teams from list into prompt')
        label4.pack() 
        frame1 = Frame(self, bg='red')
        frame1.pack(side=LEFT, fill=BOTH)
        
        def drawHeadToHead(frame = None):
            df = main.getTeams('bundes')
            self.table = pt = Table(frame1, dataframe=df,
            showtoolbar=False, showstatusbar=True)
            pt.show()

        drawHeadToHead(frame1)
        button1 = Button(self, text='Back to Leagues', command =
            lambda : controller.show_frame(StartPage))
        button1.pack()

        label1 = Label(self, text='Home Team')
        label1.pack(pady=10)
        entry = Entry(self)
        entry.pack()
        entry.focus_set()
        label2 = Label(self, text='Away Team')
        label2.pack(pady=10)
        entry2 = Entry(self)
        entry2.pack()
        entry2.focus_set()
        
        def callback():
            try:
                home2 = renameWrapper('players', 'bundes', entry.get())
                away2 = renameWrapper('players', 'bundes', entry2.get())

                game = [{'Away': entry2.get(),'Home': entry.get(), 
                'Home Goals': main.predictGame('bundes', entry.get(), entry2.get())[0], 
                'Away Goals': main.predictGame('bundes', entry.get(), entry2.get())[1],
                'Home Attack Rating': main.averagesHome('bundes', home2)[0],
                'Away Attack Rating': main.averagesAway('bundes', away2)[0], 
                'Home Midfield Rating': main.averagesHome('bundes', home2)[1],
                'Away Midfield Rating': main.averagesAway('bundes', away2)[1],
                'Home Defense Rating': main.averagesHome('bundes', home2)[2], 
                'Away Defense Rating': main.averagesAway('bundes', away2)[2],
                'Home Best Player': main.averagesHome('bundes', home2)[3],
                'Away Best Player': main.averagesAway('bundes', away2)[3],
                'Home Player Age': main.averagesHome('bundes', home2)[4],
                'Away Player Age': main.averagesAway('bundes', away2)[4]
                }]
                df = pd.DataFrame(game, 
                    columns=['Home', 'Home Goals', 'Away', 'Away Goals',
                'Home Attack Rating', 'Away Attack Rating', 'Home Midfield Rating',
                'Away Midfield Rating', 'Home Defense Rating', 'Away Defense Rating',
                'Home Best Player', 'Away Best Player', 'Home Player Age',
                'Away Player Age'])

                self.table = pt = Table(frame1, dataframe=df,
                showtoolbar=False, showstatusbar=True)
                pt.show()
            
            except:

                for i in range(18):
                    if i == 17 and entry.get() != main.getTeams('bundes')['Teams'][i]:
                        label3 = Label(self, text='No Such Home Team', fg='red')
                        label3.pack()

                    elif entry.get() != main.getTeams('bundes')['Teams'][i]:
                        continue
                    elif entry.get() == main.getTeams('bundes')['Teams'][i]:
                        break
                
                for i in range(18):
                    if i == 17 and entry2.get() != main.getTeams('bundes')['Teams'][i]:
                        label3 = Label(self, text='No Such Away Team', fg='red')
                        label3.pack()
                    elif entry2.get() != main.getTeams('bundes')['Teams'][i]:
                        continue
                    elif entry2.get() == main.getTeams('bundes')['Teams'][i]:
                        break
                
                   
        
        button3 = Button(self, text = 'Predict', command = callback)
        button3.pack()

        button4 = Button(self, text='Back to Head To Head', command=
                        drawHeadToHead)
        button4.pack()

class HeadToHeadLiga(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='Head To Head La Liga')
        label.pack(padx=10, pady=10)
        label4 = Label(self, text='Copy teams from list into prompt')
        label4.pack() 
        frame1 = Frame(self, bg='red')
        frame1.pack(side=LEFT, fill=BOTH)
        
        def drawHeadToHead(frame = None):
            df = main.getTeams('liga')
            self.table = pt = Table(frame1, dataframe=df,
            showtoolbar=False, showstatusbar=True)
            pt.show()

        drawHeadToHead(frame1)
        button1 = Button(self, text='Back to Leagues', command =
            lambda : controller.show_frame(StartPage))
        button1.pack()

        label1 = Label(self, text='Home Team')
        label1.pack(pady=10)
        entry = Entry(self)
        entry.pack()
        entry.focus_set()
        label2 = Label(self, text='Away Team')
        label2.pack(pady=10)
        entry2 = Entry(self)
        entry2.pack()
        entry2.focus_set()
        
        def callback():
            try:
                home2 = renameWrapper('players', 'liga', entry.get())
                away2 = renameWrapper('players', 'liga', entry2.get())

                game = [{'Away': entry2.get(),'Home': entry.get(), 
                'Home Goals': main.predictGame('liga', entry.get(), entry2.get())[0], 
                'Away Goals': main.predictGame('liga', entry.get(), entry2.get())[1],
                'Home Attack Rating': main.averagesHome('liga', home2)[0],
                'Away Attack Rating': main.averagesAway('liga', away2)[0], 
                'Home Midfield Rating': main.averagesHome('liga', home2)[1],
                'Away Midfield Rating': main.averagesAway('liga', away2)[1],
                'Home Defense Rating': main.averagesHome('liga', home2)[2], 
                'Away Defense Rating': main.averagesAway('liga', away2)[2],
                'Home Best Player': main.averagesHome('liga', home2)[3],
                'Away Best Player': main.averagesAway('liga', away2)[3],
                'Home Player Age': main.averagesHome('liga', home2)[4],
                'Away Player Age': main.averagesAway('liga', away2)[4]
                }]
                df = pd.DataFrame(game, 
                    columns=['Home', 'Home Goals', 'Away', 'Away Goals',
                'Home Attack Rating', 'Away Attack Rating', 'Home Midfield Rating',
                'Away Midfield Rating', 'Home Defense Rating', 'Away Defense Rating',
                'Home Best Player', 'Away Best Player', 'Home Player Age',
                'Away Player Age'])

                self.table = pt = Table(frame1, dataframe=df,
                showtoolbar=False, showstatusbar=True)
                pt.show()
            
            except:

                for i in range(18):
                    if i == 17 and entry.get() != main.getTeams('liga')['Teams'][i]:
                        label3 = Label(self, text='No Such Home Team', fg='red')
                        label3.pack()

                    elif entry.get() != main.getTeams('liga')['Teams'][i]:
                        continue
                    elif entry.get() == main.getTeams('liga')['Teams'][i]:
                        break
                
                for i in range(18):
                    if i == 17 and entry2.get() != main.getTeams('liga')['Teams'][i]:
                        label3 = Label(self, text='No Such Away Team', fg='red')
                        label3.pack()
                    elif entry2.get() != main.getTeams('liga')['Teams'][i]:
                        continue
                    elif entry2.get() == main.getTeams('liga')['Teams'][i]:
                        break
                
                   
        
        button3 = Button(self, text = 'Predict', command = callback)
        button3.pack()

        button4 = Button(self, text='Back to Head To Head', command=
                        drawHeadToHead)
        button4.pack()

class HeadToHeadPrem(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='Head To Head Premier League')
        label.pack(padx=10, pady=10)
        label4 = Label(self, text='Copy teams from list into prompt')
        label4.pack() 
        frame1 = Frame(self, bg='red')
        frame1.pack(side=LEFT, fill=BOTH)
        
        def drawHeadToHead(frame = None):
            df = main.getTeams('prem')
            self.table = pt = Table(frame1, dataframe=df,
            showtoolbar=False, showstatusbar=True)
            pt.show()

        drawHeadToHead(frame1)
        button1 = Button(self, text='Back to Leagues', command =
            lambda : controller.show_frame(StartPage))
        button1.pack()

        label1 = Label(self, text='Home Team')
        label1.pack(pady=10)
        entry = Entry(self)
        entry.pack()
        entry.focus_set()
        label2 = Label(self, text='Away Team')
        label2.pack(pady=10)
        entry2 = Entry(self)
        entry2.pack()
        entry2.focus_set()
        
        def callback():
            try:
                home2 = renameWrapper('players', 'prem', entry.get())
                away2 = renameWrapper('players', 'prem', entry2.get())

                game = [{'Away': entry2.get(),'Home': entry.get(), 
                'Home Goals': main.predictGame('prem', entry.get(), entry2.get())[0], 
                'Away Goals': main.predictGame('prem', entry.get(), entry2.get())[1],
                'Home Attack Rating': main.averagesHome('prem', home2)[0],
                'Away Attack Rating': main.averagesAway('prem', away2)[0], 
                'Home Midfield Rating': main.averagesHome('prem', home2)[1],
                'Away Midfield Rating': main.averagesAway('prem', away2)[1],
                'Home Defense Rating': main.averagesHome('prem', home2)[2], 
                'Away Defense Rating': main.averagesAway('prem', away2)[2],
                'Home Best Player': main.averagesHome('prem', home2)[3],
                'Away Best Player': main.averagesAway('prem', away2)[3],
                'Home Player Age': main.averagesHome('prem', home2)[4],
                'Away Player Age': main.averagesAway('prem', away2)[4]
                }]
                df = pd.DataFrame(game, 
                    columns=['Home', 'Home Goals', 'Away', 'Away Goals',
                'Home Attack Rating', 'Away Attack Rating', 'Home Midfield Rating',
                'Away Midfield Rating', 'Home Defense Rating', 'Away Defense Rating',
                'Home Best Player', 'Away Best Player', 'Home Player Age',
                'Away Player Age'])

                self.table = pt = Table(frame1, dataframe=df,
                showtoolbar=False, showstatusbar=True)
                pt.show()
            
            except:

                for i in range(18):
                    if i == 17 and entry.get() != main.getTeams('prem')['Teams'][i]:
                        label3 = Label(self, text='No Such Home Team', fg='red')
                        label3.pack()

                    elif entry.get() != main.getTeams('prem')['Teams'][i]:
                        continue
                    elif entry.get() == main.getTeams('prem')['Teams'][i]:
                        break
                
                for i in range(18):
                    if i == 17 and entry2.get() != main.getTeams('prem')['Teams'][i]:
                        label3 = Label(self, text='No Such Away Team', fg='red')
                        label3.pack()
                    elif entry2.get() != main.getTeams('prem')['Teams'][i]:
                        continue
                    elif entry2.get() == main.getTeams('prem')['Teams'][i]:
                        break
                
                   
        
        button3 = Button(self, text = 'Predict', command = callback)
        button3.pack()

        button4 = Button(self, text='Back to Head To Head', command=
                        drawHeadToHead)
        button4.pack()

class HeadToHeadSerieA(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='Head To Head Serie A')
        label.pack(padx=10, pady=10)
        label4 = Label(self, text='Copy teams from list into prompt')
        label4.pack() 
        frame1 = Frame(self, bg='red')
        frame1.pack(side=LEFT, fill=BOTH)
        
        def drawHeadToHead(frame = None):
            df = main.getTeams('serie A')
            self.table = pt = Table(frame1, dataframe=df,
            showtoolbar=False, showstatusbar=True)
            pt.show()

        drawHeadToHead(frame1)
        button1 = Button(self, text='Back to Leagues', command =
            lambda : controller.show_frame(StartPage))
        button1.pack()

        label1 = Label(self, text='Home Team')
        label1.pack(pady=10)
        entry = Entry(self)
        entry.pack()
        entry.focus_set()
        label2 = Label(self, text='Away Team')
        label2.pack(pady=10)
        entry2 = Entry(self)
        entry2.pack()
        entry2.focus_set()
        
        def callback():
            try:
                home2 = renameWrapper('players', 'serie A', entry.get())
                away2 = renameWrapper('players', 'serie A', entry2.get())

                game = [{'Away': entry2.get(),'Home': entry.get(), 
                'Home Goals': main.predictGame('serie A', entry.get(), entry2.get())[0], 
                'Away Goals': main.predictGame('serie A', entry.get(), entry2.get())[1],
                'Home Attack Rating': main.averagesHome('serie A', home2)[0],
                'Away Attack Rating': main.averagesAway('serie A', away2)[0], 
                'Home Midfield Rating': main.averagesHome('serie A', home2)[1],
                'Away Midfield Rating': main.averagesAway('serie A', away2)[1],
                'Home Defense Rating': main.averagesHome('serie A', home2)[2], 
                'Away Defense Rating': main.averagesAway('serie A', away2)[2],
                'Home Best Player': main.averagesHome('serie A', home2)[3],
                'Away Best Player': main.averagesAway('serie A', away2)[3],
                'Home Player Age': main.averagesHome('serie A', home2)[4],
                'Away Player Age': main.averagesAway('serie A', away2)[4]
                }]
                df = pd.DataFrame(game, 
                    columns=['Home', 'Home Goals', 'Away', 'Away Goals',
                'Home Attack Rating', 'Away Attack Rating', 'Home Midfield Rating',
                'Away Midfield Rating', 'Home Defense Rating', 'Away Defense Rating',
                'Home Best Player', 'Away Best Player', 'Home Player Age',
                'Away Player Age'])

                self.table = pt = Table(frame1, dataframe=df,
                showtoolbar=False, showstatusbar=True)
                pt.show()
            
            except:

                for i in range(18):
                    if i == 17 and entry.get() != main.getTeams('serie A')['Teams'][i]:
                        label3 = Label(self, text='No Such Home Team', fg='red')
                        label3.pack()

                    elif entry.get() != main.getTeams('serie A')['Teams'][i]:
                        continue
                    elif entry.get() == main.getTeams('serie A')['Teams'][i]:
                        break
                
                for i in range(18):
                    if i == 17 and entry2.get() != main.getTeams('serie A')['Teams'][i]:
                        label3 = Label(self, text='No Such Away Team', fg='red')
                        label3.pack()
                    elif entry2.get() != main.getTeams('serie A')['Teams'][i]:
                        continue
                    elif entry2.get() == main.getTeams('serie A')['Teams'][i]:
                        break
                
                   
        
        button3 = Button(self, text = 'Predict', command = callback)
        button3.pack()

        button4 = Button(self, text='Back to Head To Head', command=
                        drawHeadToHead)
        button4.pack()


app = ultrastat()
app.mainloop()
