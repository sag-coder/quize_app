# ls=[(1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,)]
# add=0
#
# for i in range(len(ls)):
#     print(i)
#     stor=(ls[i][0])
#     add=stor+add
#
# print(add)

# from tkinter import *
# import time
# class timer:
#
#     def __init__(self):
#         self.root = Tk()
#         self.tim = 60
#         self.root.minsize(500, 500)
#         self.root.maxsize(500, 500)
#         self.main()
#         self.root.mainloop()
#     def main(self):
#         self.label_1=Label(self.root)
#         self.label_1.pack()
#         self.clock()
#
#
#
#     def clock(self):
#         hours=time.strftime('%H')
#         minuts=time.strftime('%M')
#         second=time.strftime('%S')
#         self.label_1.configure(text=hours +':'+minuts +':'+second)
#         self.label_1.after(1000, self.clock)
#
#
#
#
#
#
#
# obj=timer()
# import mysql.connector
#
#
#
# try:
#     conn = mysql.connector.connect(host='localhost', port='8889', user='root', password='root',
#                                         database='quiz')
#     mycursor = conn.cursor()
#     print("connected")
# except Exception as e:
#     print(e)
#
# mycursor.execute("SELECT * FROM sub1")
# question_data=mycursor.fetchall()

#mycursor.execute("create table sub1_answer(result_id INT NOT NULL AUTO_INCREMENT,user_id INT NOT NULL,PRIMARY KEY ( result_id ))")
# update='user_id'
# for i in question_data:
#
#     #print(i)
#     mycursor.execute("ALTER TABLE `sub1_answer` ADD `{}` VARCHAR(255) NOT NULL AFTER `{}`".format('qno_'+str(i[0]), update))
#     conn.commit()
#     #update_col=question_data[0][1]
#     update=str('qno_'+str(i[0]))
#     print(update)

# mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'sub1_answer'ORDER BY ORDINAL_POSITION")
# data=mycursor.fetchall()
# ex=(data[2:])
# for i in data[2:]:
#     mycursor.execute("INSERT INTO sub1_answer(")


import time
from tkinter import *
def countdown(tim):

    timer.configure(text=str(tim))

    print(tim)
    if tim>0:
        tim = tim - 1
        time.sleep(1)
        countdown(tim)
    else:
        timer.configure(text="time up")

root=Tk()
root.geometry("600x400")
timer=Label(root)
timer.pack()

tim=5

countdown(tim)
root.mainloop()
