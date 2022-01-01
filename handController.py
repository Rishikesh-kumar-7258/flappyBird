import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

prev_pos = 0


def Controller(q1):

    global prev_pos

    cap = cv2.VideoCapture(1)
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
                    mp_draw.draw_landmarks(
                        frame, landmarks, mp_hands.HAND_CONNECTIONS)

                    open_fingers = finger_count(landmarks)

                    msg = ""
                    if open_fingers == 2:
                        msg = "Start"
                    elif open_fingers == 0:
                        msg = "Stop"
                    elif open_fingers == 1:
                        msg = "Up"
                    elif open_fingers == 5:
                        msg = "Pause"

                    q1.put(msg)

            cv2.line(frame, [0, h//2], [w, h//2], (0, 255, 0), 10)
            cv2.imshow("Controller window", cv2.flip(frame, 1))

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


def finger_count(landmarks) -> int:
    open_fingers: int = 0
    i: int = 8
    n: int = len(landmarks.landmark)

    if landmarks.landmark[4].y <= landmarks.landmark[5].y:
        open_fingers += 1

    while (i < n):
        if landmarks.landmark[i].y > landmarks.landmark[i-2].y:
            open_fingers += 1
        i += 4
    return open_fingers


# if __name__ == "__main__":
#     Controller(0)
