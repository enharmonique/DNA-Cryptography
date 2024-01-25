from test.run_all_tests import run_all_tests
import PySimpleGUI as sg
from dna_cryptography.encode_basic import encode_to_dna, decode_from_dna
from dna_cryptography.encode_xor import encode_to_dna_xor, decode_from_dna_xor
from utilities.utils import text_to_binary
from utilities.key_generation import generate_secure_key
from utilities.file_utils import decodeFromFile,encodeFromFile,saveToFile

def spawnMainWindow():

    raw_decode = "Encrypted/Decrypted message previews show up here"
    used_decode=decode_from_dna
    used_encode=encode_to_dna

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
            #fixes bug
            sg.In(key="-SAVE-",size=(40//3-1, 1),visible=False,enable_events=True),
            sg.FileSaveAs("Save", key="-SAVE-0-",size=(40//3-1, 1),enable_events=True)
        ],
        [
            sg.Radio('default (key unused)',  "RADIO1", key = "-TYPE-DEFAULT-", default=True, enable_events=True),
            sg.Radio('xor', "RADIO1", key = "-TYPE-XOR-", enable_events=True),
        ],
        [
            sg.Column([[
                sg.Text(raw_decode,size=(40,10),background_color="#8FCEE0",text_color="#000000",key="-DISPLAY-")
            ]],background_color = '#283B5B'),
        ]
    ]
    window = sg.Window(title="Encrypt/Decrypt", layout=[file_list_column], margins=(100, 50))
    def notify(txt,warn=False,err=False):
        clr     = "#AA0000" if err else ("#AAAA00" if warn else "#64778D")
        clr_txt = "#FFFFFF" if err else ("#000000" if warn else "#FFFFFF")
        window.Find("-NOTIF-").update(txt,text_color=clr_txt,background_color=clr)
        pass
    while True:
        try:
            event, values = window.read()
            print(event,values)
            if event == "-GENERATE-KEY-":
                window.Find("-KEY-").update(generate_secure_key(values["-KEY-"]))
                notify("Key generated.")
                
            if event.startswith("-TYPE-"):
                if(event == "-TYPE-DEFAULT-"):
                    used_decode=decode_from_dna
                    used_encode=encode_to_dna
                elif(event == "-TYPE-XOR-"):
                    used_decode=decode_from_dna_xor
                    used_encode=encode_to_dna_xor


            if event == "-DECODE-":
                # decode from file
                raw_decode = decodeFromFile(values["-FILE-"], values["-KEY-"], used_decode)
                raw_decode = b''.join([bytes([int(raw_decode[i:i+8], 2)]) for i in range(0, len(raw_decode), 8)])
                
                #try to display it as text if it's not binary
                try:
                    window.Find("-DISPLAY-").update(raw_decode.decode('ascii'))
                except:
                    window.Find("-DISPLAY-").update("Binary data:\n" + str(raw_decode))

                window.Find("-SAVE-0-").update("Save decoded")
                notify("Decoded.") 

            if event == "-ENCODE-":
                raw_decode = encodeFromFile(values["-FILE-"], values["-KEY-"],used_encode)
                window.Find("-DISPLAY-").update(raw_decode)
                window.Find("-SAVE-0-").update("Save encoding")
                notify("Encoded.") 

            if event == "-SAVE-" or event == "-SAVE-0-":
                # save to file
                saveToFile(values['-SAVE-0-'],raw_decode)
                notify("Saved.") 

            if event == sg.WIN_CLOSED:
                # End program if user closes window or
                break
        except Exception as ex:
            notify(str(ex),err=True) 
    window.close()
    pass


if __name__ == "__main__":
    run_all_tests()
    spawnMainWindow()