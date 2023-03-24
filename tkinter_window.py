from tkinter import Tk, BOTH, Canvas

class Window() :

    def __init__(self,ht,wt) :
        self.__root = Tk()
        self.__root.title("MAZE-SOLVER")
        self.__cnvs = Canvas(self.__root,bg = "white",height = ht,weight = wt)
        self.__cnvs.pack(fill=BOTH,expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) :
        self__running = True 
        while self__running :
            self.redraw()
            print("window closed...")

    def close(self) :
        self__running = False
