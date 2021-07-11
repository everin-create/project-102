import dropbox
import os 
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='vtT-bnWoOxsAAAAAAAAAAeylP6JfSLuEaAjGkmJ_FVmMENMzR09lwo7OWzBCiUJ7'
    transferdata=TransferData(access_token)

    path=input("enter a file path to transfer.")

    list_of_files=os.listdir(path)

    for file in list_of_files:
        name,ext=os.path.splitext(file)
        ext=ext[1:]

        if ext==".jpg":
            musicfile=file
   
    file_from=musicfile
    file_to=input("Enter the full path to upload the file to the dropbox")

    transferdata.upload_file(file_from,file_to)
    print("file has been moved")

main()