# hareket_algilama.py
import cv2
yakalama = cv2.VideoCapture(0)

durum1,resim_eski=yakalama.read()
durum2,resim_yeni=yakalama.read()
while True: 
    fark_resmi=cv2.absdiff(resim_yeni,resim_eski)
    gri_resim = cv2.cvtColor(fark_resmi,cv2.COLOR_BGR2GRAY)
    filtreli=cv2.GaussianBlur(gri_resim,(3,3),0)
    t,sb_resim=cv2.threshold(filtreli,20,255,cv2.THRESH_BINARY)
    konturlar,hiyerarsi=cv2.findContours(sb_resim,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for kontur in konturlar:
        alan=cv2.contourArea(kontur)
        if alan>1000:
            x,y,w,h=cv2.boundingRect(kontur)
            cv2.rectangle(resim_eski,(x,y),(x+w,y+h),(0,255,0),1)
            
    cv2.imshow("sonuc",resim_eski)
    
    resim_eski=resim_yeni
    durum,resim_yeni=yakalama.read()
    
    if cv2.waitKey(50)==27 or not(durum):
        break
    
yakalama.release()
cv2.destroyAllWindows()