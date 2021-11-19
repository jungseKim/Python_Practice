from TicTacToeDemo import Border
from TicTacToeDemo import Qplayer
from tkinter import *
import tkinter.font as tkFont
from functools import partial
import numpy as np
import pickle

root = Tk()
root.geometry('600x600')
label = Label(root, text='Let fuck tictactoeGame')
label.pack()
contaier = Frame(root, width=500,
                 height=500,)
contaier.pack()
helv36 = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)


border = Border()
border.reset()

buttons = []

with open('qValue.p', 'rb') as f:
    tableData = pickle.load(f)

player = Qplayer(-1)
player.states_value = tableData
player.exp_rate = 0

check = False


def reStart():
    global check
    check = False
    border.reset()
    mapLoad()


def mapLoad():
    state = np.reshape(border.state, [9])
    for index, b in enumerate(buttons):
        if state[index] == np.float(1.0):
            b['text'] = ('O')

        elif state[index] == np.float(-1.0):
            b['text'] = ('X')
        else:
            b['text'] = ('')


def change_label_number(action):
    global check
    position = border.availablePositions()
    if len(border.availablePositions()) == 0:
        check = True
        print('무승부')
        return
    if action not in position or check:
        return

    border.step(action, 1)
    if len(border.availablePositions()) == 0:
        check = True
        print('무승부')
        return
    position = border.availablePositions()

    action = player.chooseAction(position, border.state)

    border.step(action, -1)

    mapLoad()

    if(border.done):
        check = True
        print('게임끝')


for x in range(3):
    for y in range(3):
        b1 = Button(contaier, width=15,
                    height=5, font=helv36,
                    command=partial(change_label_number, (x, y)))
        b1.grid(row=x, column=y)

        buttons.append(b1)

b1 = Button(root, width=15,
            height=2, font=helv36,
            text="다시하기",
            command=partial(reStart),
            )
b1.pack()
root.mainloop()
