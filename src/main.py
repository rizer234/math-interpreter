from text_editor import TextEditor


def get_code(ide: TextEditor):
    while(True):
        if ide.run == 0:
            code = ide.code
            return code


def main():
    ide = TextEditor()
    code = get_code(ide)
    
    print (code)
    # process the {code} and show response
    # command proccessing
    # sending command to textbox for showing it
    pass


if __name__ == "__main__":
    main()