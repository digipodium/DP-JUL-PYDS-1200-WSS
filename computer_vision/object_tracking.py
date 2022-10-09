import cv2

def start_camera(cam_id=0):
    camera = cv2.VideoCapture(cam_id)
    while camera.isOpened():
        _ , image = camera.read()
        # your code goes here
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_pink = (150, 50, 50)
        upper_pink = (180, 255, 255)
        mask = cv2.inRange(hsv, lower_pink, upper_pink)
        result = cv2.bitwise_and(image, image, mask=mask)
        final = cv2.GaussianBlur(result, (5, 5), 0)
        cv2.imshow('Web Cam Output', image)
        cv2.imshow('Mask', mask)
        cv2.imshow('Result', result)
        cv2.imshow('Final', final)
        if cv2.waitKey(1) == 27: # escape key
            break
    camera.release() # free up the camera
    cv2.destroyAllWindows() # close all windows

start_camera(1)