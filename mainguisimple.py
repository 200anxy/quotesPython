import PySimpleGUI as sg
import plyer


import PySimpleGUI as sg

layout = [[sg.Text("Random Quotes!")],[sg.Text("Time in minutes for reminding")], [sg.Slider(range=(1,60),
         default_value=222,
         size=(20,15),
         orientation='horizontal',
         font=('Helvetica', 12))], [sg.Submit("Submit")]]

# Create the window
window = sg.Window("Random Quotes", layout,)

# Create an event loop
while True:
    event, values = window.read()
    sliderValue = str(values)
    print(sliderValue)
    # End program if user closes window or
    selected_number = int(values['slider'])
    print(f'Selected Number: {selected_number}')
    if event == "Submit" or event == sg.WIN_CLOSED:
        break

start_index = next((i for i, char in enumerate(sliderValue) if char.isdigit()), None)

# Find the last occurrence of a digit in the string
end_index = next((i for i, char in enumerate(sliderValue[::-1]) if char.isdigit()), None)

# Extract the substring containing the number
number_string = sliderValue[start_index:len(sliderValue) - end_index]

# Convert the string to an integer (if needed)


print(number_string)