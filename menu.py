import helper

while True:
    command = int(input())
    if command == 0:
        break;
    else:
        notebook = helper.Helper('Name')
        print(notebook.__str__())