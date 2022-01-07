import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to, local_path):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            with open (local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))


def main():
    access_token = '-a75-CHW9KYAAAAAAAAAAWJYv9votIR0M_tTvBvsDwddXA7b_r2ccG442UjICsq7'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer: ')
    relative_path = os.path.relpath(local_path, file_from)
    file_to = input('Enter the full path to upload to Dropbox: ')
    dropbox_path = os.path.join(file_to, relative_path)

    transferData.upload_file(file_from, file_to)
    print('filehasbeenmoved!!!')

main()