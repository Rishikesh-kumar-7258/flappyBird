import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def Controller(q1):

    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(max_num_hands=1) as hand: 
        while cap.isOpened():

            _, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False

            results = hand.process(frame)

            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame.flags.writeable = True

            w, h = int(cap.get(3)), int(cap.get(4))
            if results.multi_hand_landmarks:
                for landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

                    y_cord = []
                    for landmark in landmarks.landmark:
                        x,y = landmark.x * w , landmark.y * h
                        y_cord.append(y)

                    mid = sum(y_cord) / 21

                    msg = ""
                    if mid >= h // 2:
                        msg = "Down"
                    else:
                        msg = "Up"
                    
                    q1.put(msg)
                    
            cv2.line(frame, [0, h//2], [w, h//2], (0, 255, 0), 10)
            cv2.imshow("Controller window", cv2.flip(frame, 1))

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()