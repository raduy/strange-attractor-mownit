#!/usr/bin/python3
# coding=utf-8

from Tkinter import *
import base

fields = 'a', 'b', 'c'


def fetch(entries):
    base.showcase(float(entries[0][1].get()), float(entries[1][1].get()), float(entries[2][1].get()))
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))


def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        ent.place(width=10)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries


if __name__ == '__main__':
    root = Tk()
    root.geometry("%dx%d" % (500, 160))
    root.title('Strange Attractor Showcase, Mownit 2014, Lukasz Raduj')

    coefficients_text = StringVar()
    coefficients_label = Label(root, textvariable=coefficients_text)
    coefficients_label.pack()
    coefficients_text.set('Set coefficients for presentation:')
    ents = makeform(root, fields)

    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Show',
                command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()