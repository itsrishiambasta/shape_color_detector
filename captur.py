import cv2

# Try index 0 and different backends
# Try these lines one at a time:

# cap = cv2.VideoCapture(0)  # Default
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # DirectShow (Windows)
# cap = cv2.VideoCapture(0, cv2.CAP_MSMF)  # Media Foundation
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # For Linux, some work on Windows too

if not cap.isOpened():
    print("❌ Error: Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow("✅ Live Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

