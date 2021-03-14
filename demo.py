import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import font
import datetime


date = datetime.date.today()

root = Tk()
root.title("tk GUI")

filename = str(date) + '.txt'
# 함수 정의부
def saveFile():
    file = open(filename, "w")
    ts = str(list_file.get(0, END))
    file.write(ts)
    file.close()
    msgbox.showinfo("알림", "정상적으로 저장되었습니다.")

def addList():
    index = txt.get("1.0", END)
    if index == '':
        return
    list_file.insert(END, txt.get("1.0", END))
    txt.delete("1.0", END)

def finishList():
    index = list_file.curselection()
    print(list_file.curselection())
    list_file.itemconfig(index, bg='green')

def deleteList():
    index = list_file.curselection()
    list_file.delete(index)

# def openFile():
#     file = askopenfilename(initialdir="/", title="파일 선택", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*")))
#     top.title(os.path.basename(file) + " - 메모장")
#     ta.delete(1.0, END)
#     f = open(file, "r")
#     ta.insert(1.0, f.read())
#     f.close()

# 폰트 크기 정의
titleFont = font.Font(family="맑은 고딕", size=15)
listFont = font.Font(family="맑은 고딕", size=15)

# 제목 프레임 ( 날짜이동 버튼 ) 날짜, 저장 버튼
title_frame = Frame(root)
title_frame.pack()

label1 = Label(title_frame, text=date, font=titleFont)
label1.pack()

btn_sav_file = Button(title_frame, padx=5, pady=5, width=12, text="저장", command=saveFile)
btn_sav_file.pack(side="right", fill="both")


# 파일 프레임 (텍스트 입력부, 추가, 완료, 삭제)
file_frame = Frame(root)
file_frame.pack(padx=5, pady=5) # 간격 띄우기

txt = Text(file_frame, width=50, height=3)
txt.pack(side="left", expand=True)
txt.insert(END, "글자를 입력하세요")

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="추가", command=addList)
btn_add_file.pack(side="left")

btn_fin_file = Button(file_frame, padx=5, pady=5, width=12, text="완료", command=finishList)
btn_fin_file.pack(side="right")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="삭제", command=deleteList)
btn_del_file.pack(side="right")


# To DO list 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set, font=listFont)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

root.resizable(False, False)
root.mainloop()