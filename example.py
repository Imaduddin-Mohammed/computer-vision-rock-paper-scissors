import cv2
import random
from keras.models import load_model
import numpy as np
import time

def loading_model():
    start_time = time.time()
    print(start_time)
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        get_max_prediction(prediction)
        # Press q to close the window
        print(f'List of probabilities for Rock,Paper,Scissors and Nothing class respectively is: {prediction}')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def get_max_prediction(prediction):
    #a will contain the maximum probability from list of predictions
    choice = np.argmax(prediction)
    print(f'The following is the index of highest probability in the list: {choice}')
    if choice == 0:
        print("User showed Rock")
    elif choice == 1 :
        print("User showed Paper")
    elif choice == 2:
        print("User showed Scissors")
    elif choice == 3:
        print("User did not show anything i.e Nothing")

loading_model()





