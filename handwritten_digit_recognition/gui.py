import numpy as np
import pyscreenshot
import tkinter as tk
from PIL import Image
from keras.models import load_model

model = load_model('digit_recognizer.h5')

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg = 'lightgray')
        self.resizable(0, 0)
        self.x = self.y = 0
        self.title('Handwritten digit recognition')

        self.canvas = tk.Canvas(self, width = 300, height = 300, bg = 'white')
        self.canvas.grid(row = 0, column = 0, pady = 2, sticky = 'W')
        self.label = tk.Label(self, text = '', font = ("Helvetica", 40),
            bg = 'lightgray')
        self.label.grid(row = 0, column = 1, pady = 2, padx = 2)

        self.btn_recognize = tk.Button(self, text = 'Recognize', 
            command = self.recognize, bg = 'limegreen')
        self.btn_recognize.grid(row = 1, column = 1, pady = 2, padx = 2)

        self.btn_clear = tk.Button(self, text = "Clear", 
            command = self.clear, bg = 'limegreen')
        self.btn_clear.grid(row = 1, column = 0, pady = 2)

        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        radius = 10
        self.canvas.create_oval(self.x - radius, self.y - radius, 
            self.x + radius, self.y + radius, fill = 'black')

    def clear(self):
        self.canvas.delete("all")  

    def recognize(self):
        filename = f'images/image.png'
    
        img = pyscreenshot.grab(bbox = (x, y + 35, x + 300, 
            y + 35 + 300)).save(filename)
        image = Image.open(filename)
        image = image.resize((28, 28))
        image = image.convert('L')
        image = np.array(image)
        image = image.reshape(1, 28, 28, 1)
        image = image / 255.0
        result = model.predict([image])[0]
        self.label.configure(text = str(int(np.argmax(result))))

window = Window()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws / 2) - (300 / 2)
y = (hs / 2) - (300 / 2)
window.geometry('%dx%d+%d+%d' % (400, 350, x, y))
window.mainloop()
