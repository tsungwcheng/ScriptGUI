import Tkinter as tk
from Tkinter import *
import serialCOM
from serialCOM import ScriptStart
import sys
import serial
import time
import threading
#declare global ser
old_stdout = sys.stdout

ssflag = 0

class PFHandler:
    def __init__(self, str):
        self.n = str
    def getstr(self):
        return self.n


class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.update_idletasks()
        self.widget.insert("end", str)
        self.widget.configure(state="disabled")
        self.widget.see("end")


#
# class ScriptHandler():
#     print('testing Handler')
#
#     serialCOM.ScriptStart()

# class PassFailHandler(object):
#     def __init__(self, widget):
#         self.widget = widget
#         var1 = StringVar()
#         var1.set(Fvalue)
        # if var1 == 'Pass':
        #     Label(self, textvariable=var1, column=1, bg=('Green'))
        # else:
        #     Label(self, textvariable=var1, column=2, bg=('Red'))


class ScriptApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master, bg='#384747',height=600 , width=400)
        self.grid()
        self.createWidgets()
        self.OutputPanel()
        # self.Update_labels()
        # self.after_idle(self.Update_Labels(self))

    def OutputPanel(self):
        # def __init(self, master=None):
        def callback():
            self.OutputText = Text(self, bg='#333333', wrap=WORD, fg= "#f1f4f4")
            self.OutputText.grid(row=5, column=4, rowspan=100, columnspan=20, sticky=tk.NE)

            self.Scrolly = tk.Scrollbar(self, command=self.OutputText.yview)
            self.Scrolly.grid(row=5, rowspan=20, column=22, sticky='nsew')
            self.OutputText['yscrollcommand'] = self.Scrolly.set
            # redefine system print/stderr
            sys.stdout = TextRedirector(self.OutputText)
            sys.stderr = TextRedirector(self.OutputText)

            #PLabel = Label(self, textvariable=PFvar, column=1, bg=('Green'))
            #FLabel = Label(self, textvariable=PFvar, column=2, bg=('Red'))
            # var1 = PassFailHandler(serialCOM.flagpasser())
            # self.PFLabel = Label(self, bg('Green', textvariable=var1))



        t = threading.Thread(target=callback())
        t.start()

    # def ScriptHandler(self):
    #     print('test this plserino')
    #     startButton.update_idletasks()
    #     time.sleep(3)
    #     serialCOM.ScriptStart()


    def createWidgets(self):

        self.titleLabel = Label(self, bg='#AED6F1', text='DowKey Microwave \nAutomated Matrix Testing Program', font='courier 20 bold' )
        self.titleLabel.grid(column=5,row=1, sticky= 'E')
        # self.OutputPanel.grid(sticky=E)
        self.startButton = Button(self, bg='#AED6F1',font='courier 10 bold', text='Start Script', command= lambda:ScriptStart())
                                  #command = lambda: serialCOM.ScriptStart())
        self.startButton.grid(row=1, column=0,  ipadx=25, ipady=4 )
        #self.startButton.pack(side=tk.LEFT)


        self.quitButton = Button(self, bg='#AED6F1', font='courier 10 bold', text='Exit Program',
                                    command = self.quit)
        self.quitButton.grid(row=1, column=2,  ipadx=25, ipady=4)


        self.resultsButton = Button(self, bg='#AED6F1', font='courier 10 bold', text='View Test Results', command= lambda:self.Update_labels())
        self.resultsButton.grid(row=1, column=1, ipadx=25, ipady=4)

        self.testnameLabel = Label(self, bg='#7b89a5',font='courier 10 bold', text='SCPI Commands Sent:')
        self.testnameLabel.grid(row=2,column=0, pady=10)

        self.serialLabel = Label(self, bg='#7b89a5',font='courier 10 bold', text='Serial/RS232')
        self.serialLabel.grid(row=2,column=1, pady=10)

        self.ethernetLabel = Label(self, bg='#7b89a5',font='courier 10 bold', text='Ethernet')
        self.ethernetLabel.grid(row=2,column=2, pady=10)


#building test case box
        # PassLabel = []
        # FailLabel = []
        TestCaseLabels = []

        #
        # self.PassLabel = Label(self, text='Pass', bg = ('Green'))
        # self.PassLabel.grid(row=6,column=1)
        # self.FailLabel = Label(self, text='Fail', bg = ('Red'))
        # self.FailLabel.grid(row=6, column=2)
        # self.TestLabel = Label(self, text='Test cases', bg = ("#1e90ff"))
        # self.TestLabel.grid(row=6, column=0)



        TestCases = []
        num_lines = sum(1 for line in open('5440 Harris test.txt'))
        f1 = open('5440 Harris test.txt','r')
        v = 0
        for line in f1:
            v += 1
            TestCases.append("Test #%i: " % v + line)


        for n in range(0,num_lines):
            TestCaseLabels.append(Label(self, text = TestCases[n],bg = ('#000000'), relief='groove', highlightbackground='#ffd736',width = 27, fg=('#ffd736'),
                                        font=('courier 11'), anchor=W, pady=10, justify=LEFT))

        #     passButton.append(Checkbutton(self))
        #     failButton.append(Checkbutton(self))

        for counter in range(0,num_lines):
            TestCaseLabels[counter].grid(row=9+counter, column=0, sticky=S)
            #PassLabel[counter].grid(row=9+counter, column=1)
            #FailLabel[counter].grid(row=9 + counter, column=2)
            # passButton[counter].grid(row=9+counter, column=1)
            # failButton[counter].grid(row=9+counter, column=2)
    def Update_labels(self):
        #check scriptstart flag
        global ssflag

        def callback():
            PassLabel = []
            FailLabel = []
            print('#########################################################')
            print('#########################################################')
            print('#############    Displaying Results      ################')
            print('#########################################################')
            print('#########################################################')
            self.update_idletasks()
            num_lines = sum(1 for line in open('5440 Harris test.txt'))
            # if (ssflag==1):
            f2 = open('Script results.txt','r')
            v = 0
            for n in range(0,num_lines):
                PassLabel.append(Label(self, text='Pass', bg=('Green'),relief='groove'))
                FailLabel.append(Label(self, text='Fail', bg=('Red'),relief='groove'))

            for line in f2:

                print(line)
                # if (line.startswith('Cmd')):
                #     pass
                # if (line.startswith(" ")):
                #     pass
                # if (line.startswith('Cm')):
                #     print line
                #     time.sleep(1)
                if(line.startswith('     Result: ')):
                    time.sleep(1)
                    PassLabel[v-1].grid(row=9 + v, column=1, padx=8)
                    v += 1
                    pass

                if (line.startswith("     Result is")):
                    FailLabel[v-1].grid(row=9 + v, column=1, padx=8, ipadx=3)
                    time.sleep(1)
                    v += 1
                    pass

                    # FailLabel[v-1].update_idletasks()
                    # PassLabel[v-1].update_idletasks()

            f2.close()
            print("Test Results have updated...")
            print('....')
            print('....')
            print('....')
            print("Press Exit Program")

        t = threading.Thread(target=callback())
        t.start()
        # else:
        #     pass
            #check box behavior compared to test case results:
        #if var = PASS,
            #toggle passButton

        #else toggle failButton

#building output box



        #sys.stderr = TextRedirector(self.OutputText, "stderr")

# converts print() and stderr to outputTextbox






app = ScriptApp()
app.master.title('Sample Script Application')
#app.Update_labels()
app.mainloop()

sys.stdout = old_stdout