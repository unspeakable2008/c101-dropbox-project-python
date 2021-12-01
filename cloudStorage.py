from os import access
import dropbox

class Box:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb' ) as f:
            dbx.files_upload(f.read(), file_to)

def main():   
    access_Token = "RCGVshM00JEAAAAAAAAAAZVUZbGFpyLOS-XkxSB75dFOwUWy0pFu5wDt2gvNMnaK"
    box = Box(access_Token)

    file_from = input("enter the file name: ")
    file_to = input("enter the file name: ")

    box.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()