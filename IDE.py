filetoedit = input("Select File :")
file = open(filetoedit, 'a')
opened = True
while opened == True:
    cmdtodo = input("Enter command (w, c, nl, v, s, e) :")
    if cmdtodo == "w":
        file.write(input())
    elif cmdtodo == "c":
        file.truncate(0)
    elif cmdtodo == "nl":
        file.write("\n")
    elif cmdtodo == "v":
        lefile = open(filetoedit, 'r')
        print(lefile.read())
    elif cmdtodo == "s":
        file.close()
        file = open(filetoedit, 'a')
    elif cmdtodo == 'e':
        file.close()
        opened = False
    else:
        print("Unknown command. Try checking your caps")