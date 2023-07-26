import PySimpleGUI as sg
import random

def read_lines_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

def main():
    sg.theme("DarkAmber")  # Optional: Set the PySimpleGUI theme

    # Define the custom font file path
    font_size = 18  # Adjust the font size as per your preference

    # Set the font for the window and elements
    font = ('Arial', font_size)

    # Use the font in the layout
    layout = [
        [sg.Button("Browse"), sg.Button("Show Random Line")],
        [sg.Text(size=(80, 5), key="-OUTPUT-", font=font)],
    ]

    window = sg.Window("Random Line Viewer", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Browse":
            if file_path := sg.popup_get_file("Select a text file", font=font):
                lines = read_lines_from_file(file_path)
        elif event == "Show Random Line":
            if lines:
                random_line = random.choice(lines).strip()
                window["-OUTPUT-"].update(random_line)
            else:
                window["-OUTPUT-"].update("No lines in the file.")

    window.close()

if __name__ == "__main__":
    main()
