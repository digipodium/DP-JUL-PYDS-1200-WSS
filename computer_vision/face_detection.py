import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def start_camera(cam_id=0):
    cap = cv2.VideoCapture(cam_id)
    with mp_face_detection.FaceDetection(
        model_selection=0, 
        min_detection_confidence=0.5) as face_detection:
        while cap.isOpened():
            _ , image = cap.read()
            image.flags.writeable = False # immutable
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image) # detect faces
            image.flags.writeable = True  # mutable
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)
            cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    start_camera(1)