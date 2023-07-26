import PySimpleGUI as sg
import random

def read_lines_from_file(filename):
    
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

def main():
    sg.theme("DarkAmber")  # Optional: Set the PySimpleGUI theme


    # Set the font family and size 
    font = 'Chandas 18'
    # Use the font in the layout
    layout = [
        [sg.Button("Browse", font=font), sg.Button("Show Random Line", font=font)],
        [sg.Text(size=(80, 5), key="-OUTPUT-", font=font)],
    ]

    window = sg.Window("Random Line Viewer", layout)

    while True:
        event, values = window.read() # type: ignore

        if event == sg.WIN_CLOSED:
            break
        elif event == "Browse":
            if file_path := sg.popup_get_file("Select a text file", font=font):
                lines = read_lines_from_file(file_path)
        elif event == "Show Random Line":
            if lines != '': # type: ignore
                random_line = random.choice(lines).strip()
                window["-OUTPUT-"].update(random_line) # type: ignore
            else:
                window["-OUTPUT-"].update("No lines in the file.") # type: ignore

    window.close()

if __name__ == "__main__":
    main()
