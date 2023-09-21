import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from keras.models import load_model
from PIL import Image

def get_path(file_name):
    curr_dir = Path(__file__).resolve().parent
    path = curr_dir / file_name

    return str(path)


def img_to_mnist(file_name):
    path = get_path(file_name)

    # Read from path in grayscale
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    # Resize image
    img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_LINEAR)

    # Invert
    img = cv2.bitwise_not(img)

    # plt.imshow(img, cmap='gray')
    # plt.show()

    return img


class Model:
    def __init__(self):
        model_path = get_path("Model/model.keras")
        self.model = load_model(model_path)
        print("Initialized and loaded model.")

    
    def predict(self, file_name):
        img = img_to_mnist(file_name)
        img = np.resize(img, (28,28,1))
        img_arr = np.array(img).reshape(1,28,28,1)

        print('predicting...')
        y_pred = self.model.predict(img_arr)

        res = y_pred.argmax()
        
        print(y_pred)
        print(f"that's a {res}")

        return y_pred, y_pred.argmax()


if __name__ == "__main__":
    model = Model()

    model.predict("number.png")
