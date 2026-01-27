import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def get_fingers():
    success, frame = cap.read()
    if not success:
        return None, None, None

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    cv2.imshow("Hand Tracking", frame)
    cv2.waitKey(1)

    if not result.multi_hand_landmarks:
        return None, None, None

    hand = result.multi_hand_landmarks[0]

    thumb = hand.landmark[4]
    index = hand.landmark[8]
    middle = hand.landmark[12]

    return thumb, index, middle

