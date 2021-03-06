import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
from LivenessDet import LivenessDetectionModel
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from gui import Application

def main():
    #app = Application()
    #app.Run()

    livedet = LivenessDetectionModel()
    #livedet.TrainModel()
    livedet.LoadModel('features.npy', 'classifications.npy')
    livedet.TestModel()

    livedet.PlotWrongPredictions()

if __name__ == '__main__':
    main()
