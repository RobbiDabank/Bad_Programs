import sys
from Logic_class_structure_UI import*
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QAction

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

#fin_pyramid = Complected_Pyr().create_pyr()
class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = uic.loadUi(r'C:\Users\User_ASUS\Desktop\Универ\SOLITARE FILES\Dirty maket.ui')
        self.setWindowTitle('piram')
        self.ui.show()
        self.num = 0
        self.card_m = None
        self.bind = {}

        self.lst = [self.ui.label, self.ui.label_5, self.ui.label_4, self.ui.label_6, self.ui.label_7, self.ui.label_8, self.ui.label_12,
               self.ui.label_11,
               self.ui.label_10, self.ui.label_9, self.ui.label_17, self.ui.label_16, self.ui.label_15, self.ui.label_14, self.ui.label_13,
               self.ui.label_23, self.ui.label_21, self.ui.label_22, self.ui.label_19, self.ui.label_20, self.ui.label_18, self.ui.label_24,
               self.ui.label_25, self.ui.label_26, self.ui.label_27, self.ui.label_3, self.ui.label_28, self.ui.label_2]

        z = 0
        while z <= 27:
            pixmap = QPixmap("{0}".format(pyramid_card[z]))
            self.lst[z].setPixmap(pixmap)
            z +=1

        self.startpos_x_y = []
        self.startpos = []
        self.cnt = 0

        for i in self.lst:
            self.startpos_x_y.append([i.x(),i.y()])
            self.startpos.append(i.pos())

        for i in self.lst:
            i.mouseMoveEvent = self.mouseMoveEvent
            i.mouseReleaseEvent = self.mouseReleaseEvent
        self.ui.mousePressEvent = self.mousePressEvent



    def mouseReleaseEvent(self, event):
        if self.card_m.isVisible != False:
            self.card_m.move(self.startpos[self.num])
            for i in fin_pyramid:
                for j in i:
                    if j == pyramid_card[self.num]:
                        v = fin_pyramid.index(i)
                        h = i.index(j)
                        if int(((fin_pyramid[v + 1])[h + 1])[:-2]) == 0 and int(((fin_pyramid[v + 1])[h])[:-2]) == 0:
                            if int(((fin_pyramid[v])[h])[:-2]) == 13:
                                (fin_pyramid[v])[h] = ("0")
                                self.card_m.setVisible(False)

    def mouseMoveEvent(self, event):
        for i in fin_pyramid:
            for j in i:
                if j == pyramid_card[self.num]:
                    v = fin_pyramid.index(i)
                    h = i.index(j)
                    if int(((fin_pyramid[v+1])[h+1])[:-2]) == 0 and int(((fin_pyramid[v+1])[h])[:-2]) == 0:
                        self.card_m.move(self.card_m.mapToParent(event.pos()))
                        self.card_m.raise_()


    def mousePressEvent(self, event):
        count = 0
        for i in self.startpos_x_y:
            if event.x() in range(i[0], i[0]+100) and event.y() in range(i[1], i[1]+100):
                self.card_m = self.lst[count]
                self.num = count
            count += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())

t = 0
while True:
    z = 0
    b = 16
    for i in fin_pyramid:
        if z == 7:
            break
        z += 1
        print("  " * b, i)
        b -= 2
    print('The first card in stack', card_stack[t])

    v = input("Enter first card =  ")
    if v == 'n':
        t += 1
        continue
    if v[-2] == ",":

        h = input()
        if use_card(int(h[0]), int(h[-1]), fin_pyramid, bool) == 0:
            print("Sorry but you can not use this card ")
            continue
        else:
            pass
        if card_compare_2(v, h, fin_pyramid, bool) == 0:
            continue
        t += 1
    else:
        y = int(v[-1])
        x = int(v[0])
        if int(((fin_pyramid[x])[y])[:-2]) == 13:
            del (fin_pyramid[x])[y]
            fin_pyramid[x].insert(y, "0  ")
            continue
        h = input('Enter second card')
        if use_card(int(v[0]), int(v[-1]), fin_pyramid, bool) == 0 or use_card(int(h[0]), int(h[-1]), fin_pyramid, bool) == 0:
            print("Sorry but you can not use this card")
            continue
        else:
            pass
        if card_compare(v, h, fin_pyramid, bool) == 0:
            continue



    bool = 0

