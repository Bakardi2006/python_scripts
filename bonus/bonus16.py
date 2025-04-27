import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
compress_files = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder:")
compress_files2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File compressor",
                   layout=[[label1, compress_files, choose_button1],
                           [label2, compress_files2, choose_button2],
                           [compress_button]])

window.read()
window.close()