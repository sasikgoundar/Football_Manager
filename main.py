from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("footballdata.db")
cursor = conn.cursor()

def exot():
    exit(0)
'''
#Create Table Agent
cursor.execute('CREATE TABLE AGENTS(NAME varchar(40),'
               'NATIONALITY VARCHAR(20),'
               'RATING NUMBER(2),'
               'PRIMARY KEY (NAME))')

#Create Table Clubs
cursor.execute('CREATE TABLE CLUBS (CLUB_ID number (2) NOT NULL, '
               'CLUB_NAME varchar (30) NOT NULL, '
               'CLUB_RATING number (2), '
               'CLUB_MANAGER varchar (30), '
               'CLUB_CHAIRMAN varchar (30), '
               'LEAGUE varchar (30), '
               'CLUB_TITLEs number (2), '
               'YEAr_FOUNDED number (4), '
               'PRIMARY KEY (CLUB_NAME))')

#Create Table Nationals
cursor.execute('CREATE TABLE NATIONALS(NATION varchar(20),'
               'MANAGER varchar(30),'
               'WORLD_CUP_WON number(2),'
               'RATING number(2),'
               'primary key (NATION))')

#Create Table Players
cursor.execute('CREATE TABLE PLAYERS(FIRST_NAME VARCHAR(20) NOT NULL,'
               'LAST_NAME VARCHAR(20),'
               'NATIONALITY VARCHAR(20),'
               'CLUB__NAME varchar(30),'
               'AGE NUMBER(2),YEARS_AT_CLUB NUMBER(2),'
               'AGENT_NAME VARCHAR(40),'
               'RATING NUMBER(2),'
               'POSITION VARCHAR(4),'
               'FOREIGN KEY(CLUB__NAME) REFERENCES CLUBS(CLUB_NAME),'
               'FOREIGN KEY(AGENT_NAME) REFERENCES AGENTS(NAME),'
               'FOREIGN KEY(NATIONALITY) REFERENCES NATIONALS(NATION))')
'''



# insering into club
def insertClub():
    def saveClub():
        cursor.execute('INSERT INTO CLUBS VALUES(?,?,?,?,?,?,?,?)', (
        cEntry0.get(), cEntry1.get(), cEntry2.get(), cEntry3.get(), cEntry4.get(), cEntry5.get(), cEntry6.get(),
        cEntry7.get()))
        conn.commit()
        messagebox.showinfo("Success!", "Insertion successful!", command=insertData())
        ()

    clubWindow = Tk()
    clubWindow.title("Insert Club data")
    clubWindow.geometry("750x750")
    clubLabel = Label(clubWindow, text="Enter Club details:", anchor=CENTER, font=("helvetica", 25, "bold"))
    clubInsert = Button(clubWindow, text="INSERT", width=20, height=2, command=saveClub, bg="white", fg="BLACK",
                        font=("bold"))
    clubExit = Button(clubWindow, text="BACK", width=20, height=2, command=clubWindow.destroy, fg="red", bg="black",
                      font=("bold"))

    cLabel0 = Label(clubWindow, text="Club ID", fg="red", font=("bold"))
    cLabel1 = Label(clubWindow, text="Club Name", fg="red", font=("bold"))
    cLabel2 = Label(clubWindow, text="Rating", fg="red", font=("bold"))
    cLabel3 = Label(clubWindow, text="Manager", fg="red", font=("bold"))
    cLabel4 = Label(clubWindow, text="Chairman", fg="red", font=("bold"))
    cLabel5 = Label(clubWindow, text="League", fg="red", font=("bold"))
    cLabel6 = Label(clubWindow, text="Titles", fg="red", font=("bold"))
    cLabel7 = Label(clubWindow, text="Year Founded", fg="red", font=("bold"))

    cEntry0 = Entry(clubWindow, bd=5)
    cEntry1 = Entry(clubWindow, bd=5)
    cEntry2 = Entry(clubWindow, bd=5)
    cEntry3 = Entry(clubWindow, bd=5)
    cEntry4 = Entry(clubWindow, bd=5)
    cEntry5 = Entry(clubWindow, bd=5)
    cEntry6 = Entry(clubWindow, bd=5)
    cEntry7 = Entry(clubWindow, bd=5)

    cLabel0.grid(row=0, column=0, padx=100, pady=10)
    cLabel1.grid(row=1, column=0, padx=100, pady=10)
    cLabel2.grid(row=2, column=0, padx=100, pady=10)
    cLabel3.grid(row=3, column=0, padx=100, pady=10)
    cLabel4.grid(row=4, column=0, padx=100, pady=10)
    cLabel5.grid(row=5, column=0, padx=100, pady=10)
    cLabel6.grid(row=6, column=0, padx=100, pady=10)
    cLabel7.grid(row=7, column=0, padx=100, pady=10)

    cEntry0.grid(row=0, column=1, pady=10)
    cEntry1.grid(row=1, column=1, pady=10)
    cEntry2.grid(row=2, column=1, pady=10)
    cEntry3.grid(row=3, column=1, pady=10)
    cEntry4.grid(row=4, column=1, pady=10)
    cEntry5.grid(row=5, column=1, pady=10)
    cEntry6.grid(row=6, column=1, pady=10)
    cEntry7.grid(row=7, column=1, pady=10)
    clubInsert.grid(row=8, column=0, pady=50)
    clubExit.grid(row=8, column=1, padx=50, pady=50, columnspan=2)
    clubWindow.mainloop()


# insert into agents
def insertAgent():
    def saveAgent():
        cursor.execute('INSERT INTO AGENTS VALUES(?,?,?)', (aEntry0.get(), aEntry1.get(), aEntry2.get()))
        conn.commit()
        messagebox.showinfo("Success!", "Insertion successful!")
        ()

    agentWindow = Tk()
    agentWindow.title("Insert Agent data")
    agentWindow.geometry("750x750")
    agentLabel = Label(agentWindow, text="Enter Agent details:", anchor=CENTER, font=("helvetica", 25, "bold"))
    agentInsert = Button(agentWindow, text="INSERT", width=20, height=2, command=saveAgent, bg="white", fg="BLACK",
                         font=("bold"))
    agentExit = Button(agentWindow, text="BACK", width=20, height=2, command=agentWindow.destroy, fg="red", bg="black",
                       font=("bold"))

    aLabel0 = Label(agentWindow, text="Agent Name", fg="red", font=("bold"))
    aLabel1 = Label(agentWindow, text="Nationality", fg="red", font=("bold"))
    aLabel2 = Label(agentWindow, text="Rating", fg="red", font=("bold"))

    aEntry0 = Entry(agentWindow, bd=5)
    aEntry1 = Entry(agentWindow, bd=5)
    aEntry2 = Entry(agentWindow, bd=5)

    aLabel0.grid(row=0, column=0, padx=100, pady=10)
    aLabel1.grid(row=1, column=0, padx=100, pady=10)
    aLabel2.grid(row=2, column=0, padx=100, pady=10)

    aEntry0.grid(row=0, column=1, pady=10)
    aEntry1.grid(row=1, column=1, pady=10)
    aEntry2.grid(row=2, column=1, pady=10)

    agentInsert.grid(row=3, column=0, pady=50)
    agentExit.grid(row=3, column=1, padx=50, pady=50, columnspan=2)

    agentWindow.mainloop()


# insert into nationals
def insertNational():
    def saveNational():
        cursor.execute('INSERT INTO NATIONALS VALUES(?,?,?,?)',
                       (nEntry0.get(), nEntry1.get(), nEntry2.get(), nEntry3.get()))
        conn.commit()
        nationalWindow.destroy()
        messagebox.showinfo("Success!", "Insertion successful!")
        ()

    nationalWindow = Tk()
    nationalWindow.title("Insert National Team data")
    nationalWindow.geometry("750x750")
    nationalLabel = Label(nationalWindow, text="Enter National Team details:", anchor=CENTER,
                          font=("helvetica", 25, "bold"))
    nationalInsert = Button(nationalWindow, text="INSERT", width=20, height=2, command=saveNational, bg="white",
                            fg="BLACK", font=("bold"))

    nationalExit = Button(nationalWindow, text="BACK", width=20, height=2, command=nationalWindow.destroy, fg="red",
                          bg="black", font=("bold"))

    nLabel0 = Label(nationalWindow, text="Nation", fg="red", font=("bold"))
    nLabel1 = Label(nationalWindow, text="Manager", fg="red", font=("bold"))
    nLabel2 = Label(nationalWindow, text="World Cups won", fg="red", font=("bold"))
    nLabel3 = Label(nationalWindow, text="Rating", fg="red", font=("bold"))

    nEntry0 = Entry(nationalWindow, bd=5)
    nEntry1 = Entry(nationalWindow, bd=5)
    nEntry2 = Entry(nationalWindow, bd=5)
    nEntry3 = Entry(nationalWindow, bd=5)

    nLabel0.grid(row=0, column=0, padx=100, pady=10)
    nLabel1.grid(row=1, column=0, padx=100, pady=10)
    nLabel2.grid(row=2, column=0, padx=100, pady=10)
    nLabel3.grid(row=3, column=0, padx=100, pady=10)

    nEntry0.grid(row=0, column=1, pady=10)
    nEntry1.grid(row=1, column=1, pady=10)
    nEntry2.grid(row=2, column=1, pady=10)
    nEntry3.grid(row=3, column=1, pady=10)

    nationalInsert.grid(row=4, column=0, pady=50)
    nationalExit.grid(row=4, column=1, padx=50, pady=50, columnspan=2)

    nationalWindow.mainloop()


# insert into players
def insertPlayer():
    def savePlayer():
        cursor.execute('INSERT INTO PLAYERS VALUES(?,?,?,?,?,?,?,?,?)', (
        pEntry0.get(), pEntry1.get(), pEntry2.get(), pEntry3.get(), pEntry4.get(), pEntry5.get(), pEntry6.get(),
        pEntry7.get(), pEntry8.get()))
        conn.commit()
        messagebox.showinfo("Success!", "Insertion successful!")
        ()

    playerWindow = Tk()
    playerWindow.title("Insert Player data")
    playerWindow.geometry("750x750")
    playerLabel = Label(playerWindow, text="Enter Player details:", anchor=CENTER, fg="red",
                        font=("helvetica", 25, "bold"))
    playerInsert = Button(playerWindow, text="INSERT", width=20, height=2, command=savePlayer, bg="white", fg="BLACK",
                          font=("bold"))
    playerExit = Button(playerWindow, text="BACK", width=20, height=2, command=playerWindow.destroy, fg="red",
                        bg="black", font=("bold"))

    pLabel0 = Label(playerWindow, text="First Name", fg="red", font=("bold"))
    pLabel1 = Label(playerWindow, text="Last Name", fg="red", font=("bold"))
    pLabel2 = Label(playerWindow, text="Nationality", fg="red", font=("bold"))
    pLabel3 = Label(playerWindow, text="Club Name", fg="red", font=("bold"))
    pLabel4 = Label(playerWindow, text="Age", fg="red", font=("bold"))
    pLabel5 = Label(playerWindow, text="Years At Club", fg="red", font=("bold"))
    pLabel6 = Label(playerWindow, text="Agent Name", fg="red", font=("bold"))
    pLabel7 = Label(playerWindow, text="Rating", fg="red", font=("bold"))
    pLabel8 = Label(playerWindow, text="Position", fg="red", font=("bold"))

    pEntry0 = Entry(playerWindow, bd=5)
    pEntry1 = Entry(playerWindow, bd=5)
    pEntry2 = Entry(playerWindow, bd=5)
    pEntry3 = Entry(playerWindow, bd=5)
    pEntry4 = Entry(playerWindow, bd=5)
    pEntry5 = Entry(playerWindow, bd=5)
    pEntry6 = Entry(playerWindow, bd=5)
    pEntry7 = Entry(playerWindow, bd=5)
    pEntry8 = Entry(playerWindow, bd=5)

    pLabel0.grid(row=0, column=0, padx=100, pady=10)
    pLabel1.grid(row=1, column=0, padx=100, pady=10)
    pLabel2.grid(row=2, column=0, padx=100, pady=10)
    pLabel3.grid(row=3, column=0, padx=100, pady=10)
    pLabel4.grid(row=4, column=0, padx=100, pady=10)
    pLabel5.grid(row=5, column=0, padx=100, pady=10)
    pLabel6.grid(row=6, column=0, padx=100, pady=10)
    pLabel7.grid(row=7, column=0, padx=100, pady=10)
    pLabel8.grid(row=8, column=0, padx=100, pady=10)

    pEntry0.grid(row=0, column=1, pady=10)
    pEntry1.grid(row=1, column=1, pady=10)
    pEntry2.grid(row=2, column=1, pady=10)
    pEntry3.grid(row=3, column=1, pady=10)
    pEntry4.grid(row=4, column=1, pady=10)
    pEntry5.grid(row=5, column=1, pady=10)
    pEntry6.grid(row=6, column=1, pady=10)
    pEntry7.grid(row=7, column=1, pady=10)
    pEntry8.grid(row=8, column=1, pady=10)

    playerInsert.grid(row=9, column=0, pady=30)
    playerExit.grid(row=9, column=1, padx=50, pady=30, columnspan=2)
    playerWindow.mainloop()

#defining data disp window

def insertData():
    insertWindow = Tk()
    insertWindow.title("Insert data")
    insertWindow.geometry("550x550")
    insertLabel = Label(insertWindow, text="Which table to enter data into?",anchor=CENTER,font=("helvetica",25,"bold"))
    insertButton1 = Button(insertWindow,text="CLUBS",width=20,height=2,command=insertClub,bg="white",fg="BLACK",font=("bold"))
    insertButton2 = Button(insertWindow,text="AGENTS",width=20,height=2,command=insertAgent,bg="white",fg="BLACK",font=("bold"))
    insertButton3 = Button(insertWindow,text="NATIONAL TEAM",width=20,height=2,command=insertNational,bg="white",fg="BLACK",font=("bold"))
    insertButton4 = Button(insertWindow,text="PLAYERS",width=20,height=2,command=insertPlayer,bg="white",fg="BLACK",font=("bold"))
    insertExit = Button(insertWindow,text="BACK",width=20,height=2,command=insertWindow.destroy,bg="black",fg="red",font=("bold"))
    insertLabel.pack(fill=X,anchor=CENTER)
    insertButton1.pack(anchor=CENTER,pady=20)
    insertButton2.pack(anchor=CENTER,pady=20)
    insertButton3.pack(anchor=CENTER,pady=20)
    insertButton4.pack(anchor=CENTER,pady=20)
    insertExit.pack(anchor=CENTER,pady=20)
    ()
    insertWindow.mainloop()


# defining view data window
def viewalldata():
    def viewNation():
        def allNation():
            class ScrolledFrame(Frame):

                def __init__(self, parent, vertical=True, horizontal=False):
                    super().__init__(parent)

                    # self._canvas = tk.Canvas(self)
                    self._canvas = Canvas(self, height=700, width=1200)
                    self._canvas.grid(row=0, column=0)

                    self._vertical_bar = Scrollbar(self, orient="vertical", command=self._canvas.yview)
                    if vertical:
                        self._vertical_bar.grid(row=0, column=1, sticky="ns")
                    self._canvas.configure(yscrollcommand=self._vertical_bar.set)

                    self._horizontal_bar = Scrollbar(self, orient="horizontal", command=self._canvas.xview)
                    if horizontal:
                        self._horizontal_bar.grid(row=1, column=0, sticky="we")
                    self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

                    self.frame = Frame(self._canvas)
                    self._canvas.create_window((0, 0), window=self.frame, anchor="nw")

                    self.frame.bind("<Configure>", self.resize)

                def resize(self, event=None):
                    self._canvas.configure(scrollregion=self._canvas.bbox("all"))

            # --- functions ---

            def display_nation(master, data):

                headers = [
                    ("Nation", 10),
                    ("Manager", 10),
                    ("World Cups Won", 10),
                    ("Rating", 10),
                ]

                # create row with headers
                for col, (header, size) in enumerate(headers):
                    l = Label(master, text=header, width=size, fg="red", font=("helvetica", 25, "bold"))
                    l.grid(row=0, column=col)

                # create rows with players
                for row, nation in enumerate(data, 1):
                    for col in range(4):
                        l = Label(master, text=nation[col], font=("bold"))
                        l.grid(row=row, column=col)

            # --- main ---

            # - create random data for test -

            # import random
            # import string

            # data = []
            # for rows in range(20):
            #    row = []
            #    for cols in range(9):
            #        row.append(random.choice(string.ascii_letters))
            #    data.append(row)

            # - start -

            root = Tk()

            # ---

            # create scrolled frame with vertical and horizontal scrollbar
            sf = ScrolledFrame(root, True, True)
            sf.pack()

            # you  have to use `sf.frame` as parent for widgets
            cursor.execute("SELECT * from NATIONALS order by nation")
            data = cursor.fetchall()

            display_nation(sf.frame, data)

            root.mainloop()

        def displayNation(data):
            master = Tk()
            master.geometry('500x500')
            master.title('All Nations')
            Label1 = Label(master, text="Nation", width=10, fg="red", font=("helvetica", 25, "bold"))
            Label1.grid(row=0, column=0)
            Label2 = Label(master, text="Manager", width=10, fg="red", font=("helvetica", 25, "bold"))
            Label2.grid(row=0, column=1)
            Label3 = Label(master, text="World Cups Won", width=10, fg="red", font=("helvetica", 25, "bold"))
            Label3.grid(row=0, column=2)
            Label4 = Label(master, text="Rating", width=10, fg="red", font=("helvetica", 25, "bold"))
            Label4.grid(row=0, column=3)

            for index, dat in enumerate(data):
                Label(master, text=dat[0], font=("bold")).grid(row=index + 1, column=0)
                Label(master, text=dat[1], font=("bold")).grid(row=index + 1, column=1)
                Label(master, text=dat[2], font=("bold")).grid(row=index + 1, column=2)
                Label(master, text=dat[3], font=("bold")).grid(row=index + 1, column=3)

        def nameNation():
            def searchName3():
                cursor.execute('select * from  NATIONALS  where Nation  like ?', (nEntry.get() + '%',))
                data = cursor.fetchall()
                displayNation(data)

            name = Tk()
            name.title("Search Nation name")
            name.geometry("750x750")
            nameLabel = Label(name, text="Enter a Nation Name", anchor=CENTER, font=("helvetica", 25, "bold"))
            name1 = Label(name, text="Nation Name", font=("bold"))
            name1.grid(row=2, column=0, padx=100, pady=20)
            nEntry = Entry(name, bd=5)
            nEntry.grid(row=2, column=2, pady=20)
            print(nEntry.get())
            nameSearch = Button(name, text="SEARCH", width=20, height=2, command=searchName3, bg="white", fg="BLACK",
                                font=("bold"))
            nameSearch.grid(row=5, column=0, pady=30)

            nameExit = Button(name, text="BACK", width=20, height=2, command=name.destroy, fg="red", bg="black",
                              font=("bold"))
            nameExit.grid(row=5, column=2, padx=50, pady=30, columnspan=2)

            name.mainloop()

        def manNation():
            def searchManager():
                cursor.execute('select * from  NATIONALS  where MANAGER  like ?', (nEntry.get() + '%',))
                data = cursor.fetchall()
                displayNation(data)

            name = Tk()
            name.title("Search Nation name")
            name.geometry("750x750")
            nameLabel = Label(name, text="Enter Manager", anchor=CENTER, font=(None, 20, "bold"))
            name1 = Label(name, text="Manager", font=("bold"))
            name1.grid(row=2, column=0, padx=100, pady=20)
            nEntry = Entry(name, bd=5)
            nEntry.grid(row=2, column=2, pady=20)
            print(nEntry.get())
            nameSearch = Button(name, text="SEARCH", width=20, height=2, command=searchManager, bg="white", fg="BLACK",
                                font=("bold"))
            nameSearch.grid(row=5, column=0, pady=30)

            nameExit = Button(name, text="BACK", width=20, height=2, command=name.destroy, fg="red", bg="black",
                              font=("bold"))
            nameExit.grid(row=5, column=2, padx=50, pady=30, columnspan=2)

            name.mainloop()

        def ratingNation():
            def searchRating():
                cursor.execute('select * from  NATIONALS  where RATING BETWEEN ? AND ?', (nEntry1.get(), nEntryy.get()))
                data = cursor.fetchall()
                displayNation(data)

            name = Tk()
            name.title("Search by rating")
            name.geometry("750x750")
            nameLabel = Label(name, text="Rating of NAtion", anchor=CENTER, font=("helvetica", 25, "bold"))
            name1 = Label(name, text="Minimum", fg="red", font=("bold"))
            name1.grid(row=2, column=0, padx=100, pady=20)
            name2 = Label(name, text="Maximum", fg="red", font=("bold"))
            name2.grid(row=3, column=0, padx=100, pady=20)
            nEntry = Entry(name, bd=5)
            nEntry.grid(row=2, column=2, pady=20)
            nEntryy = Entry(name, bd=5)
            nEntryy.grid(row=3, column=2, pady=20)
            nameSearch = Button(name, text="SEARCH", width=20, height=2, command=searchRating, bg="white", fg="BLACK",
                                font=("bold"))
            nameSearch.grid(row=5, column=0, pady=30)
            nameExit = Button(name, text="BACK", width=20, height=2, command=name.destroy, fg="red", bg="black",
                              font=("bold"))
            nameExit.grid(row=5, column=2, padx=50, pady=30, columnspan=2)

            name.mainloop()

        # defining viewing window
        Nation = Tk()
        Nation.title("Search Nation")
        Nation.geometry("750x750")
        viewLabel = Label(Nation, text="Which data?", anchor=CENTER, font=(None, 20, "bold")).pack()
        NationButton1 = Button(Nation, text="ALL", width=20, height=2, command=allNation, bg="white", fg="BLACK",
                               font=("bold")).pack(anchor=CENTER, pady=25)
        NationButton2 = Button(Nation, text="Nation Name", width=20, height=2, command=nameNation, bg="white",
                               fg="BLACK", font=("bold")).pack(anchor=CENTER, pady=25)
        NationButton3 = Button(Nation, text="Manager", width=20, height=2, command=manNation, bg="white", fg="BLACK",
                               font=("bold")).pack(anchor=CENTER, pady=25)
        NationButton5 = Button(Nation, text="Rating", width=20, height=2, command=ratingNation, bg="white", fg="BLACK",
                               font=("bold")).pack(anchor=CENTER, pady=25)
        NationExit = Button(Nation, text="BACK", width=20, height=2, command=Nation.destroy, fg="red", bg="black",
                            font=("bold")).pack(anchor=CENTER, pady=25)


def mainPage():
    mWindow = Tk()
    mWindow.configure(background="white")
    mWindow.title("Choose option")
    mWindow.geometry("550x500")
    MLabel1 = Label(mWindow, text="What would you like to do?", anchor=CENTER, font=("helvetica", 25, "bold"))
    MButton1 = Button(mWindow, text="Insert data", width=10, height=2, command=insertData, bg="white", fg="BLACK",
                      font=("bold"))
    MButton2 = Button(mWindow, text="View all data", width=10, height=2, command=viewalldata, bg="white", fg="BLACK",
                      font=("bold"))
    MExit = Button(mWindow, text="Exit", width=10, height=2, command=exot, fg="red", bg="black", font=("bold"))

    MLabel1.pack(fill=X, anchor=CENTER)
    MButton1.pack(anchor=CENTER, pady=50)
    MButton2.pack(anchor=CENTER, pady=50)
    MExit.pack(side=BOTTOM, anchor=S)
    mWindow.mainloop()


def login():
    root = Toplevel()
    root.title("Log In")
    root.configure(bg="white")
    root.geometry("500x500")

    def abcde():
        if E1.get() == 'abc' and E2.get() == 'def':
            messagebox.showinfo("Success", "Logged in")
            root.destroy()
            frontpage.destroy()
            mainPage()
        else:
            messagebox.showinfo("Failure", "Incorrect info")

            root.destroy()

    L1 = Label(root, text="User Name", font=("bold"))
    L1.config(bg="white")
    E1 = Entry(root, bd=5)
    L2 = Label(root, text="Password", font=("bold"))
    L2.config(bg="white")
    E2 = Entry(root, bd=5, show='*')
    B1 = Button(root, text="Log In", width=10, height=1, command=abcde, font=("bold"))
    B2 = Button(root, text="Exit", width=10, height=1, command=root.destroy, fg="red", bg="black", font=("bold"))

    L1.grid(row=0, column=0, padx=100, pady=100)
    E1.grid(row=0, column=1, pady=10, columnspan=2)
    L2.grid(row=1, column=0, pady=50)
    E2.grid(row=1, column=1, pady=50)
    B1.grid(row=3, column=0, pady=10)
    B2.grid(row=3, column=1, pady=10)

    root.mainloop()


frontpage = Tk()
frontpage.geometry("500x500")
frontpage.title("Start Page")
B = Label(frontpage, text="Welcome to football database", font=("times", 16, "bold"), fg="red").pack()
from PIL import Image, ImageTk

image = Image.open('ab.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(frontpage, image=photo_image)
label.pack()
button1 = Button(frontpage, text="Start", width=20, height=2, command=login, bg="white", fg="BLACK", font=("bold"))
button2 = Button(frontpage, text="Exit", width=20, height=2, command=exot, fg="red", bg="black", font=("bold"))
# B.pack(fill=X,anchor=CENTER)
button1.pack(side=LEFT, anchor=SW)
button2.pack(side=RIGHT, anchor=SE)
# frontpage.iconify()

frontpage.mainloop()
