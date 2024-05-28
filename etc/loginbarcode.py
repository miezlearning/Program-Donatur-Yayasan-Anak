import cv2
from pyzbar.pyzbar import decode

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Gagal membaca frame, coba lagi.")
        continue

    # Mengidentifikasi QR code pada frame
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        # Mendapatkan data dari QR code
        qr_data = obj.data.decode('utf-8')
        
        # Menampilkan data QR code
        print("Data QR Code: ", qr_data)
        
        # Menampilkan data QR code pada frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, qr_data, (50, 50), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
        
        # Menandai QR code pada frame dengan kotak pembatas
        rect = obj.rect
        cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 2)

    # Menampilkan frame kamera
    cv2.imshow('QR Code Scanner', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan kamera dan menutup jendela
cap.release()
cv2.destroyAllWindows()
