import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import font
import datetime




win = Tk()
win.title("호노의 메모장")
# win.option_add("*Font", "맑음고딕 20")

def saveFile():
    t = datetime.datetime.now().strftime("%Y년%m월%d일") + ".txt"
    file = open(t, 'a')
    file.write(ta)

def addList():
    index = txt.get("1.0", END)
    if index == '':
        return
    list_file.insert(END, txt.get("1.0", END))
    txt.delete("1.0", END)

titleFont = font.Font(family="맑은 고딕", size=15)
listFont = font.Font(family="맑은 고딕", size=15)

list_frame = Frame(win)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set, font=listFont)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

#파일 프레임
file_frame = Frame(win)
file_frame.pack(padx=5, pady=5)

txt = Text(file_frame, width=50, height=3)
txt.pack(side="left", expand=True)
txt.insert(END, "글자를 입력하세요")



btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="추가", command=addList)
btn_add_file.pack(side="left")
#
# btn_fin_file = Button(file_frame, padx=5, pady=5, width=12, text="완료", command=finishList)
# btn_fin_file.pack(side="right")
#
# btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="삭제", command=deleteList)
# btn_del_file.pack(side="right")

# To DO list 프레임


win.resizable(False, False)
win.mainloop()