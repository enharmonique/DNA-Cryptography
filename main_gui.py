from test.run_all_tests import run_all_tests
import PySimpleGUI as sg
from dna_cryptography.encode_basic import encode_to_dna, decode_from_dna
from utils import text_to_binary

def spawnMainWindow():

    raw_decode = ""

    file_list_column = [
        [
            sg.Text("",size=(40, 1),key="-NOTIF-"),
        ],
        [
            sg.Text("Key",size=(5, 1)),
            sg.In(size=(25, 1), enable_events=True, key="-KEY-"),
            sg.Button(size=(10, 1),button_text="Generate",enable_events=True, key="-GENERATE-KEY-"),
        ],
        [
            sg.Text("File",size=(5,1)),
            sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
            sg.FileBrowse(size=(10, 1), enable_events = True)
        ],
        [
            sg.Button("Decode bases", key="-DECODE-",size=(40//3-1, 1),enable_events=True),
            sg.Button("Encode bases", key="-ENCODE-",size=(40//3-1, 1),enable_events=True),
            #fixes mild bug
            sg.Button("Save decoded", key="-SAVE-",size=(40//3-1, 1),visible=False,enable_events=True),
            sg.FileSaveAs("Save decoded", key="-SAVE-0-",size=(40//3-1, 1),enable_events=True)
        ],
        [
            sg.Column([[
                sg.Text(raw_decode,size=(40,10),background_color="#8FCEE0",text_color="#000000",key="-DISPLAY-")
            ]],background_color = '#283B5B'),
        ]
    ]
    window = sg.Window(title="Encrypt/Decrypt", layout=[file_list_column], margins=(100, 50))
    def notify(txt,warn=False,err=False):
        #TODO: pick better colors
        clr     = "#FF0000" if err else ("#FFFF00" if warn else "#64778D")
        clr_txt = "#FFFFFF" if err else ("#000000" if warn else "#FFFFFF")
        window.Find("-NOTIF-").update(txt,text_color=clr_txt,background_color=clr)
        pass
    while True:
        try:
            event, values = window.read()
            # End program if user closes window or
            # presses the OK button
            print(event, values)
            if event == "-GENERATE-KEY-":
                #TODO: GENERATE KEY
                generated_key = "TODO: GENERATE KEY"
                window.Find("-KEY-").update(generated_key)
                del generated_key
                notify("Key generated.") 
            if event == "-DECODE-":
                # decode from file
                # TODO: use specific function so binary files work as well
                # and error handling too
                with open(window.Find("-FILE-").get()) as f:
                    bases = f.read()
                    raw_decode = decode_from_dna(bases,window.Find("-KEY-").get())
                    raw_decode = ''.join([chr(int(raw_decode[i:i+8], 2)) for i in range(0, len(raw_decode), 8)])
                    window.Find("-DISPLAY-").update(str(raw_decode))#TODO: handle displaying binary file data.
                    del bases
                notify("Decoded.") 
            if event == "-ENCODE-":
                # encode from file
                # TODO: use specific function so binary files work as well
                # and error handling too
                with open(window.Find("-FILE-").get()) as f:
                    txt = f.read()
                    raw_decode = encode_to_dna(text_to_binary(txt),window.Find("-KEY-").get())
                    window.Find("-DISPLAY-").update(raw_decode)
                    del txt
                notify("Encoded.") 
            if event == "-SAVE-" or event == "-SAVE-0-":
                # save to file
                # TODO: use specific function so saving binary files works as well.
                path = values['-SAVE-0-']
                with open(path,"w") as f:
                    f.write(raw_decode)
                del path
                notify("Saved.") 
            if event == "OK" or event == sg.WIN_CLOSED:
                break
        except Exception as ex:
            notify(str(ex),err=True) 
    window.close()
    pass


if __name__ == "__main__":
    run_all_tests()
    spawnMainWindow()