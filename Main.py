from tkinter import *
from tkinter import ttk
import random
from Sorting_Algos import *
from threading import Thread

root = Tk()
root.title("Sorting Algorithms in Action")
root.maxsize(1920,1080)
root.config(bg="black")

#variables
selected_algo = StringVar()
data = []
stop = 0

#
def drawDataFn(data, colourArray):
    canvas.delete("all")
    c_height=700
    c_width=1000
    x_width= c_width/(len(data)+1)
    offset=50
    spacing=10

    normalizedData = [i/max(data) for i in data]
    for i,height in enumerate(normalizedData):
        #top left
        x0 = i*x_width + offset + spacing
        y0 = c_height - height * 600
        #bottom right
        x1 = (i+1) * x_width + offset 
        y1 = c_height
        #mean of x for text
        mean_x= (x0+x1)//2
        
        canvas.create_rectangle(x0, y0, x1, y1, fill=colourArray[i])
        canvas.create_text(mean_x, y0, anchor=SW, text=str(data[i]))
    
    #to update the screen every time drawData is called
    root.update_idletasks()     

def Generate():

    global data

    
    print("Algo Selected :" + selected_algo.get())
    
    minValue=int(minEntry.get())
    maxValue=int(maxEntry.get())
    size=int(sizeEntry.get())
    
    data=[]
    for _ in range(size):
        data.append(random.randrange(minValue,maxValue+1))

    drawDataFn(data, ['red' for x in range(len(data))])

def Start():
    global data
    
    if not data: return

    if (algoMenu.get() == 'Quick Sort'):
        quickSort(data,0,len(data)-1, drawDataFn, speedScale.get())
        drawDataFn(data, ['green' for x in range(len(data))])

    elif (algoMenu.get() == 'Bubble Sort'):
        bubbleSort(data, drawDataFn, speedScale.get())
        drawDataFn(data, ['green' for x in range(len(data))])

    elif (algoMenu.get() == 'Selection Sort'):
        selectionSort(data, drawDataFn, speedScale.get())
        drawDataFn(data, ['green' for x in range(len(data))])

    elif (algoMenu.get() == 'Merge Sort'):
        mergeSort(data, drawDataFn, speedScale.get())
        drawDataFn(data, ['green' for x in range(len(data))])

def quit():
    global root
    root.destroy()


#frame / base layout
UI_frame = Frame(root,width=1080,height=100,bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)    

canvas=Canvas(root,width=1080,height=700,bg='white')
canvas.grid(row=1,column=0,padx=10,pady=5)

  
#UI Area


Label(UI_frame,text="Algorithm:",bg="grey").grid(row=0,column=0,padx=0,pady=0,sticky=E)
algoMenu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Bubble Sort','Quick Sort','Merge Sort','Selection Sort'])
algoMenu.grid(row=0,column=2,padx=5, pady=5,sticky=W)
algoMenu.current(0)

Button(UI_frame, text='Generate', command=Generate,bg='Orange').grid(row=1,column=4,padx=5,pady=5)
Button(UI_frame, text='Start', command = Start ,bg='Green').grid(row=2,column=4,padx=5,pady=5)
#Button(UI_frame, text='Stop', command=quit,bg='Red').grid(row=3,column=4,padx=5,pady=5)

speedScale = Scale(UI_frame, from_=0.02, to=5.0, length=300, resolution=0.01, orient=HORIZONTAL, label="Delay:", bg="grey"  )
speedScale.grid(row=1, column=0, padx=5, pady=5)

sizeEntry = Scale(UI_frame, from_=3, to=50, length=300, digits=2, resolution=1, orient=HORIZONTAL, label="Size:", bg="grey"  )
sizeEntry.grid(row=2,column=0,padx=50,pady=5)

minEntry=Scale(UI_frame, from_=1, to=100, length=300, digits=2, resolution=1, orient=HORIZONTAL, label="Min:", bg="grey"  )
minEntry.grid(row=1,column=2,padx=50,pady=5)

maxEntry=Scale(UI_frame, from_=10, to=100, length=300, digits=2, resolution=1, orient=HORIZONTAL, label="Max:", bg="grey"  )
maxEntry.grid(row=2,column=2,padx=50,pady=5,sticky=W)


root.mainloop()

