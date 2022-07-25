from fileinput import filename
import dropbox
import os 
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root, dirs,files in os.walk(file_from):
            for fileName in files:
                local_path=os.path.join(root,fileName)

                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb')as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
       
def main():
    access_token="sl.BMGn2UuVCTMVdcQ9l3tOrT1TxXA2P7jLvKe_wc2q2O7Q9AtEivls9O7gjz3Md_dcELmU9V2RJE85MxeTzgWkPS3971aIET4lwkJcjZAF7RZuOwFJvbFgTSJhmg50Sv5oB8rIuLhrwGkZ"
    transferdata=TransferData(access_token)

    file_from=input("enter the file path to transfer")
    file_to=input("enter the full path to upload to dropbox")
    transferdata.upload_file(file_from,file_to)
    print("the file has been moved")
main()
