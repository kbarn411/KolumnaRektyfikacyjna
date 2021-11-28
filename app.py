#import for GUI
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
#import for calculations
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so

class App:
    #Code of this class created with help of https://www.visualtk.com/
    def __init__(self, root):
        #setting title
        root.title("Program do obliczenia liczby półek teoretycznych kolumny rektyfikacyjnej")
        #setting window size
        width=600
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        #wstęp, opis programu
        GLabel_intro=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_intro["font"] = ft
        GLabel_intro["fg"] = "#333333"
        GLabel_intro["justify"] = "center"
        GLabel_intro["text"] = """
        Program do obliczenia liczby półek teoretycznych kolumny rektyfikacyjnej z wykorzystaniem
        3 parametrów opisujących skład molowy surówki (f), cieczy wyczerpanej (w) oraz destylatu (d).
        Surówka jest cieczą wrzącą. Na wynikowym wykresie żółte punkty reprezentują fizykochemię półki.
        """
        GLabel_intro.place(x=20,y=10,width=550,height=50)

        #pola tekstowe opisujące które parametry należy podać
        GLabel_770=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_770["font"] = ft
        GLabel_770["fg"] = "#333333"
        GLabel_770["justify"] = "center"
        GLabel_770["text"] = "Wprowadź parametr f"
        GLabel_770.place(x=80,y=70,width=294,height=30)

        GLabel_71=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_71["font"] = ft
        GLabel_71["fg"] = "#333333"
        GLabel_71["justify"] = "center"
        GLabel_71["text"] = "Wprowadź parametr w"
        GLabel_71.place(x=80,y=110,width=293,height=30)

        GLabel_533=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_533["font"] = ft
        GLabel_533["fg"] = "#333333"
        GLabel_533["justify"] = "center"
        GLabel_533["text"] = "Wprowadź parametr d"
        GLabel_533.place(x=80,y=150,width=292,height=30)

        GLabel_534=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_534["font"] = ft
        GLabel_534["fg"] = "#333333"
        GLabel_534["justify"] = "center"
        GLabel_534["text"] = "Wprowadź stosunek R/Rmin"
        GLabel_534.place(x=80,y=190,width=292,height=30)

        #pola zawierające miejsce dla użytkowanika do wpisania wartości parametrów
        self.f,self.w,self.d,self.rr = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.f.set('0.42');self.w.set('0.02');self.d.set('0.95');self.rr.set('2.2')
        self.GLineEdit_721=tk.Entry(root)
        self.GLineEdit_721["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_721["font"] = ft
        self.GLineEdit_721["fg"] = "#333333"
        self.GLineEdit_721["justify"] = "center"
        self.GLineEdit_721["textvariable"] = self.f
        self.GLineEdit_721.place(x=380,y=70,width=70,height=25)

        self.GLineEdit_471=tk.Entry(root)
        self.GLineEdit_471["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_471["font"] = ft
        self.GLineEdit_471["fg"] = "#333333"
        self.GLineEdit_471["justify"] = "center"
        self.GLineEdit_471["textvariable"] = self.w
        self.GLineEdit_471.place(x=380,y=110,width=70,height=25)

        self.GLineEdit_262=tk.Entry(root)
        self.GLineEdit_262["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_262["font"] = ft
        self.GLineEdit_262["fg"] = "#333333"
        self.GLineEdit_262["justify"] = "center"
        self.GLineEdit_262["textvariable"] = self.d
        self.GLineEdit_262.place(x=380,y=150,width=70,height=25)

        self.GLineEdit_264=tk.Entry(root)
        self.GLineEdit_264["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_264["font"] = ft
        self.GLineEdit_264["fg"] = "#333333"
        self.GLineEdit_264["justify"] = "center"
        self.GLineEdit_264["textvariable"] = self.rr
        self.GLineEdit_264.place(x=380,y=190,width=70,height=25)

        #przycisk do wyboru pliku z parametrami fizykochemicznymi
        self.GButton_941=tk.Button(root)
        self.GButton_941["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_941["font"] = ft
        self.GButton_941["fg"] = "#000000"
        self.GButton_941["justify"] = "center"
        self.GButton_941["text"] = "Wybierz plik z parametrami fizykochemicznymi"
        self.GButton_941.place(x=170,y=260,width=270,height=25)
        self.GButton_941["command"] = self.GButton_941_command
        
        #przycisk do wykonania obliczeń
        GButton_940=tk.Button(root)
        GButton_940["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_940["font"] = ft
        GButton_940["fg"] = "#000000"
        GButton_940["justify"] = "center"
        GButton_940["text"] = "Licz!"
        GButton_940.place(x=270,y=300,width=70,height=25)
        GButton_940["command"] = self.GButton_940_command

        #pole z ewentualną informacją o błędnych danych wejściowych
        self.GLabel_nans=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_nans["font"] = ft
        self.GLabel_nans["fg"] = "#333333"
        self.GLabel_nans["justify"] = "center"
        self.GLabel_nans["text"] = ""
        self.GLabel_nans.place(x=80,y=340,width=294,height=30)


        statusbar = tk.Label(root, text="\t wykonał: Karol Baran, Gdańsk 2021", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.file=r""

    def GButton_940_command(self):
        try:
            self.GLabel_nans["text"] = f""
            param1=float(self.GLineEdit_721.get())
            param2=float(self.GLineEdit_471.get())
            param3=float(self.GLineEdit_262.get())
            param4=float(self.GLineEdit_264.get())
            if param4>1:
                ans = Column.calcColumn(self.file, param1, param2, param3, param4)
                self.GLabel_nans["text"] = f"Liczba półek teoretycznych : {ans}"
                Column.graphColumn(self.file, param1, param2, param3, param4)
            else:
                raise Exception('R/Rmin powinno być większe od 1')
        except:
            self.GLabel_nans["text"] = f"Sprawdź poprawność danych wejściowych"

    def GButton_941_command(self):
        filename=filedialog.askopenfilename(initialdir = "/",
                                            title = "Wybierz plik",
                                            filetypes = (("Text files","*.txt*"),
                                                         ("all files","*.*")))
        self.file=filename


class Column:
    @classmethod
    def liczY(self, e, z): #obliczenie położenia równowagi
        return z[0]*e**6 + z[1]*e**5 + z[2]*e**4 + z[3]*e**3 + z[4]*e**2 + z[5]*e + z[6]
    
    @classmethod
    def GLO(self,x,R,d): #równanie górnej linii operacyjnej
        return R/(R+1)*x + d/(R+1)
    
    @classmethod
    def DLO(self, x,e,w,R,d): #równanie dolnej linii operacyjnej
        dloa = (self.GLO(e,R,d) - w)/(e - w)
        dlob = w - w * dloa
        return dloa * x + dlob

    # 3 funkcje pomocnicze służące do wyznaczenia punktów na wykresie pracy kolumny
    @classmethod
    def funkcja(self, e, f, z):
        return self.liczY(e,z) - f
    
    @classmethod
    def ppion(self, oy, punktY):
        return punktY
    
    @classmethod
    def ppoz(self, ox, z, punktY):
        return self.liczY(punktY,z)

    #właściwa funkcja do rysowania pracy kolumny
    @classmethod
    def calcColumn(self, plik, e, w, d, RR):
        np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
        #wczytanie danych równowagowych x,y do wykresu
        x, y = np.loadtxt(plik, usecols=(0,1), unpack=True)
        #dopasowanie wielomianu do wczytanych danych równowagowych
        z = np.polyfit(x, y, 6)
        oz = z[0]*x**6 + z[1]*x**5 + z[2]*x**4 + z[3]*x**3 + z[4]*x**2 + z[5]*x + z[6]
        Yw = self.liczY(w,z)
        Ye = self.liczY(e,z)
        Yd = self.liczY(d,z)

        #obliczenie wartości powrotu minimalnego Rmin i wyznaczenie równań GLO i DLO
        Bmax = Ye - (d - Ye)/(d - e) * e
        Rmin = d/Bmax - 1
        R = RR * Rmin
        liniaEx = [e, e, e, e, e, e]
        liniaEy = np.arange(e, 1.0, 0.1)

        #algorytm rysowania trójkątów na wykresie opisujących pracę półki    
        punkt = d
        polki = 0
        while punkt > w: #dopóki na osi x nie osiągnięto składu cieczy wyczerpanej
            displ = 0.0005
            punktY = so.fsolve(self.funkcja, punkt+displ, args=(punkt,z)) #stan równowagi dla półki
            if punktY >= e:
                punktX = self.GLO(punktY,R,d) #w górnej części wykresu stosuj równanie GLO
            else:
                punktX = self.DLO(punktY,e,w,R,d) #w dolnej części wykresu stosuj równanie DLO

            #jeśli nie jest to ostatnia półka, należy zwiększyć licznik liczby półek
            if punktX >= w:
                polki += 1
            else:
                polki += (punkt - w)/(punkt - punktX)
            
            #wyznaczenie wartości dla kolejnej iteracji (zejście o półkę niżej)
            if punkt >= e and punktX >= e: #przypadek górnej części wykresu
                punkt = (punkt - d/(R+1))/(R/(R+1))
            else: #przypadek dolnej części wykresu
                dloa = (self.GLO(e,R,d) - w)/(e - w)
                dlob = w - w * dloa
                punkt = (punkt - dlob)/dloa
            
            punkt = punktX
        return round(float(polki),2)

    @classmethod
    def graphColumn(self, plik, e, w, d, RR):
        np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
        #wczytanie danych równowagowych x,y do wykresu
        x, y = np.loadtxt(plik, usecols=(0,1), unpack=True)
        #dopasowanie wielomianu do wczytanych danych równowagowych
        z = np.polyfit(x, y, 6)
        oz = z[0]*x**6 + z[1]*x**5 + z[2]*x**4 + z[3]*x**3 + z[4]*x**2 + z[5]*x + z[6]
        Yw = self.liczY(w,z)
        Ye = self.liczY(e,z)
        Yd = self.liczY(d,z)

        #obliczenie wartości powrotu minimalnego Rmin i wyznaczenie równań GLO i DLO
        Bmax = Ye - (d - Ye)/(d - e) * e
        Rmin = d/Bmax - 1
        R = RR * Rmin
        liniaEx = [e, e, e, e, e, e]
        liniaEy = np.arange(e, 1.0, 0.1)

        #rysowanie wykresów GLO i DLO
        glox = np.arange(e, d+0.05, 0.05)
        gloy = self.GLO(glox,R,d)

        dlox = np.arange(w, e+0.001, 0.001)
        dloy = self.DLO(dlox,e,w,R,d)

        plt.clf()
        plt.plot(x, oz, 'k-', x, x, 'k-')
        plt.plot(liniaEx, liniaEy, 'g--', e, Ye, 'g+', 0, Bmax, 'b+')
        pomx = np.arange(0.0, d+0.05, 0.05)
        pomy = (d - Ye)/(d - e)*pomx + Bmax
        plt.plot(pomx, pomy, 'b--')
        plt.plot(glox, gloy, 'b-')
        plt.plot(dlox, dloy, 'b-')

        #algorytm rysowania trójkątów na wykresie opisujących pracę półki    
        punkt = d
        polki = 0
        while punkt > w: #dopóki na osi x nie osiągnięto składu cieczy wyczerpanej
            displ = 0.0005
            punktY = so.fsolve(self.funkcja, punkt+displ, args=(punkt,z)) #stan równowagi dla półki
            if punktY >= e:
                punktX = self.GLO(punktY,R,d) #w górnej części wykresu stosuj równanie GLO
            else:
                punktX = self.DLO(punktY,e,w,R,d) #w dolnej części wykresu stosuj równanie DLO

            #jeśli nie jest to ostatnia półka, należy zwiększyć licznik liczby półek
            if punktX >= w:
                polki += 1
            else:
                polki += (punkt - w)/(punkt - punktX)
            
            #wyznaczenie wartości dla kolejnej iteracji (zejście o półkę niżej)
            if punkt >= e and punktX >= e: #przypadek górnej części wykresu
                punkt = (punkt - d/(R+1))/(R/(R+1))
            else: #przypadek dolnej części wykresu
                dloa = (self.GLO(e,R,d) - w)/(e - w)
                dlob = w - w * dloa
                punkt = (punkt - dlob)/dloa
                
            #rysowanie zebranych danych na wykresie
            polPionY = np.array([punktX, self.liczY(punktY,z)])
            polPionX = np.array([self.ppion(polPionY,punktY), self.ppion(polPionY,punktY)])
            plt.plot(polPionX, polPionY, 'y+')
            
            punkt = punktX
        plt.show()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
