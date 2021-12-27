import cv2
import dropbox
import time
import random

startTime = time.time()
def Take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject  = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        startTime = time.time
        result = False
        return img_name
    print("Screenshot is taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    accessToken = "vzigWLg1fnAAAAAAAAAAAaxUdhLm_Id0UYonuQvBrbV6wxTy49f3i_KUb5ntT3rk"
    file = img_name
    file_from = file
    file_to = "/testFolder"+(img_name)
    dbx = dropbox.Dropbox(accessToken)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=5):
            name = Take_snapshot()
            upload_file(name)

main()