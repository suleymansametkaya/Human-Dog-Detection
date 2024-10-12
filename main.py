from ultralytics import YOLO
import torch
import cv2
import time
import math
from mail import send_email
import datetime
import cvzone

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")  # Modelin GPU mu CPU mu kullandigini gosterir 

receiver_email = "receiver@gmail.com" # Mail gonderilecek e-posta adresi

confidence = 0.7
model = YOLO('dog_best5.pt') # Kullanilan YOLO modelini gosterir

cap = cv2.VideoCapture("dog_kids.mp4") # Kamera icin 0 yaziniz

classNames = ['dog', 'human'] # Modelimizdeki sinif isimleri

detection_count = 0  # Tespit sayac
send_count = 0  # Mail gonderme sayaci
last_email_time = time.time()  # Son e-posta gonderim zamani (Defult: Program calismaya basladigi zaman)
first_email_sent = False  # Ilk e-posta gonderimi durumu

email_cooldown = 10  # E-posta gonderimi için minimum bekleme suresi (saniye)

while cap.isOpened():
    start = time.perf_counter()
    
    success, frame = cap.read()
    
    if not success:
        break

    results = model(frame, device=device, conf=confidence, verbose=False, show=False) # Modeli kullanarak tahmin yapar
    
    both_detected = False  # Hem kopek hem de insan tespiti durumu

    dog_detected = False # Kopek tespiti durumu
    human_detected = False # Insan tespiti durumu

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            
            if conf > confidence:
                if classNames[cls] == 'dog': # Eğer sınıf köpekse `dog_detected` True olur
                    dog_detected = True
                elif classNames[cls] == 'human': # Eğer sınıf insan ise `human_detected` True olur
                    human_detected = True
                    
                color = (0, 255, 0) if classNames[cls] == 'human' else (0, 0, 255)

                cvzone.cornerRect(frame, (x1, y1, w, h), colorC=color, colorR=color)
                cvzone.putTextRect(frame, f'{classNames[cls].upper()} {int(conf * 100)}%', (max(0, x1), max(35, y1)), scale=2, thickness=3, colorR=color, colorB=color)

    # Hem kopek hem de insan tespit edilirse `both_detected` True olur
    if dog_detected and human_detected:
        both_detected = True

    # Eger `both_detected` True ise tespit sayacini arttir
    if both_detected:
        detection_count += 1
        print(f"Tespit Sayısı: {detection_count}")

    # E-posta cooldown'u hesaplar
    current_time = time.time()
    time_since_last_email = current_time - last_email_time

    # Istenen kosullar saglandiginda e-posta gonderir
    if detection_count % 10 == 0 and send_count < 5 and detection_count > 0:
        if not first_email_sent or time_since_last_email >= email_cooldown:
            # Şu anki zamanı al
            now = datetime.datetime.now()
            
            subject = "Birisi Tehlikede Olabilir!"
            body = f"İnsanların yakınında köpek tespit edildi! Zaman: {now.strftime('%Y-%m-%d %H:%M:%S')}"
            
            send_email(subject, body, receiver_email)
    
            last_email_time = current_time  # Son gonderim zamani guncellenir
            detection_count = 0  # Sayac sifiirlanir
            send_count += 1 # Gonderim sayaci arttirilir
            first_email_sent = True # Ilk e-posta gonderimi durumu True yapilir
        
    end = time.perf_counter()
    total_time = end - start
    fps = 1 / total_time

    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Yolov8 Predict", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
