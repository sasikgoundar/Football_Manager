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
        #messagebox.showinfo("Success!", "Insertion successful!", command=insertData())
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



