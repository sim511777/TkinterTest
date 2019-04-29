from tkinter import *

# MyFrame 클래스 (Tk로 부터 상송)
class MyFrame(Tk):
    # 생성자 (인스턴스 함수는 항상 self인자를 갖는다)
    def __init__(self):
        Tk.__init__(self)   # base클래스 생성자 호출

        # 메인 윈도우 속성
        self.title("입출력")
        self.geometry("300x300")

        # 텍스트박스 객체 생성
        self.tbx1 = Entry(self)         # 부모 윈도우를 self로
        self.tbx1.place(x=30, y=30, width=150, height=20)     # 레이아웃
        self.tbx1.insert(0, "input")    # 시작사 텍스트 표시

        # 버튼 객체 생성
        self.btn1 = Button(self)
        self.btn1.place(x=30, y=60, width=150, height=20)
        self.btn1.config(text="OK", command=self.btn1_Click)

        # 라벨 객체 생성
        self.lbl1 = Label(self)
        self.lbl1.place(x=30, y=90, width=150, height=20)
        self.lbl1.config(text="output", borderwidth=1, relief="solid")

    def btn1_Click(self):
        text = self.tbx1.get()
        self.lbl1.config(text=text)

# main 함수
def main():
    myframe = MyFrame() # MyFrame 객체 생성
    myframe.mainloop()  # Widget 실행

if __name__ == '__main__':
    main()