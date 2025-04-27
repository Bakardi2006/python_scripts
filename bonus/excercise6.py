import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet:")
enter_feet = sg.InputText()

label2 = sg.Text("Enter inches")
enter_inches = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[label1, enter_feet],
                                        [label2, enter_inches],
                                        [button]])

window.read()
window.close()