import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from keras.models import load_model

model = load_model('traffic_signs_classifier.h5')

classes = { 
    0: 'Speed limit (20km/h)',
    1: 'Speed limit (30km/h)', 
    2: 'Speed limit (50km/h)', 
    3: 'Speed limit (60km/h)', 
    4: 'Speed limit (70km/h)', 
    5: 'Speed limit (80km/h)', 
    6: 'End of speed limit (80km/h)', 
    7: 'Speed limit (100km/h)', 
    8: 'Speed limit (120km/h)', 
    9: 'No passing', 
    10: 'No passing veh over 3.5 tons', 
    11: 'Right-of-way at intersection', 
    12: 'Priority road', 
    13: 'Yield', 
    14: 'Stop', 
    15: 'No vehicles', 
    16: 'Veh > 3.5 tons prohibited', 
    17: 'No entry', 
    18: 'General caution', 
    19: 'Dangerous curve left', 
    20: 'Dangerous curve right', 
    21: 'Double curve', 
    22: 'Bumpy road', 
    23: 'Slippery road', 
    24: 'Road narrows on the right', 
    25: 'Road work', 
    26: 'Traffic signals', 
    27: 'Pedestrians', 
    28: 'Children crossing', 
    29: 'Bicycles crossing', 
    30: 'Beware of ice/snow',
    31: 'Wild animals crossing', 
    32: 'End speed + passing limits', 
    33: 'Turn right ahead', 
    34: 'Turn left ahead', 
    35: 'Ahead only', 
    36: 'Go straight or right', 
    37: 'Go straight or left', 
    38: 'Keep right', 
    39: 'Keep left', 
    40: 'Roundabout mandatory', 
    41: 'End of no passing', 
    42: 'End no passing veh > 3.5 tons'
}

window = tk.Tk()
window.geometry('600x500')
window.title('Traffic sign classification')
window.configure(background = '#dcdcdc')
label = Label(window, background = '#dcdcdc', 
    font = ('arial', 15, 'bold'))
sign_image = Label(window)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = np.expand_dims(image, axis = 0)
    image = np.array(image)
    pred = np.argmax(model.predict([image])[0])
    sign = classes[pred]
    label.configure(foreground = '#7f0000', text = sign) 

def show_classify_button(file_path):
    classify_button = Button(window, text = 'Classify', command = lambda:   
        classify(file_path), padx = 10, pady = 5)
    classify_button.configure(background = '#7f0000', 
        foreground = 'white',
        font = ('arial', 10, 'bold'))
    classify_button.place(relx = 0.79, rely = 0.46)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)              
        uploaded.thumbnail(((window.winfo_width() / 2.25),
            (window.winfo_height() / 2.25)))
        img = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image = img)
        sign_image.image = img
        label.configure(text = '')
        show_classify_button(file_path)
    except:
        pass

upload = Button(window, text = 'Upload an image',
    command = upload_image, padx = 10, pady = 5)
upload.configure(background = '#7f0000', 
    foreground = 'white', 
    font = ('arial', 10, 'bold'))
upload.pack(side = TOP, pady = 50)

sign_image.pack(side = BOTTOM, expand = True)
label.pack(side = BOTTOM, expand = True)

window.mainloop()

