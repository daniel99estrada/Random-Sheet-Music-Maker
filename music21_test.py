from music21 import note, stream
import tkinter as tk
import random
import sys

# --------- [TKINTER] --------
# Set up Tkinter window
root = tk.Tk()
root.configure(background = 'yellow')
root.geometry('300x300')

# -------- [CHECK BUTTONS] --------
# Action to be executed by check buttons
def add_note(chocen_elements,element,var):
    var.get()
    if var.get() == 1:
        chocen_elements.append(element)
    else:
        chocen_elements.pop(element)

# Check Cutton Class
class Check_Button:
    def __init__(self, chocen_elements, element):
        self.var = tk.IntVar()
        self.checkButton = tk.Checkbutton(root, text = element, variable = self.var, command = lambda: add_note(chocen_elements, element, self.var))
 
# Initialize a Check Button object per every note or duration available and pack it into the tkinter window.
def create_check_buttons(available_elements, chocen_elements):
    for element in available_elements:
        buttons = []
        buttons.append(Check_Button(chocen_elements, element))
        buttons[-1].checkButton.pack()

# Initialize Check Button Objects
available_notes = ["C4", "D4","E4","F4","G4"]
chocen_notes = []
available_durations = [1,2,4]
chocen_durations = []

create_check_buttons(available_notes, chocen_notes)
create_check_buttons(available_durations, chocen_durations)

# -------- [TOTAL MEASURES SLIDER] ---------
# The output of the slider will dictate the total number of measures.
slider = tk.Scale(root, from_=1, to=4, orient='horizontal')
slider.pack()

# -------- ["CREATE SHEET MUSIC" BUTTON] -------
# Action assigned to Button
def create_sheet_music(total_measures):
    
    stream1 = stream.Stream()
    beatCounter = 0
    measureCounter = 0

    while measureCounter < total_measures:

        # Random selection of  a notes and  a duration.
        random_note = chocen_notes[random.randint(0,len(chocen_notes) - 1)]
        random_duration = chocen_durations[random.randint(0,len(chocen_durations) - 1)]

        if random_duration + beatCounter % 4 > 4:
            continue
        
        #Initialize a a Music21 Note object with the random note and duration selection.
        newNote = note.Note(random_note)
        newNote.quarterLength = random_duration 

        # Append Note Object to Music21 Stream1
        stream1.append(newNote)

        beatCounter += random_duration
        if beatCounter % 4 == 0:
            measureCounter += 1

    # Create sheet music in Musescore
    stream1.show()

# Create Button.
button = tk.Button(root,text="Create Sheet Music", foreground = 'green', command = lambda: create_sheet_music(slider.get()))
button.pack()

# -------- [MAIN LOOP] ------
root.mainloop()