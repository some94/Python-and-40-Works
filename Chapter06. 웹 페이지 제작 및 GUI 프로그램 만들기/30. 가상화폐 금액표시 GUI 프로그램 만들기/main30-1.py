import tkinter

window = tkinter.Tk() # window 객체 생성
window.title("가상화폐 금액표시") # 타이틀 정의
window.geometry("400x200") # GUI 사이즈 설정
window.resizable(False,False) # 가로세로의 크기 조절 불가

label=tkinter.Label(window, text="hello")
label.pack()

window.mainloop() # GUI를 계속 실행하기 위해 mainloop 실행