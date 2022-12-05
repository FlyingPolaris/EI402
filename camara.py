from jetcam.csi_camera import CSICamera
import cv2

#CSI-0
camera0 = CSICamera(capture_device=0, width=224, height=224)
image0 = camera0.read()
print(image0.shape)
print(camera0.value.shape)

#CSI-1
#camera1 = CSICamera(capture_device=1, width=224, height=224)
#image1 = camera1.read()
#print(image1.shape)
#print(camera1.value.shape)

while 1:
    image0 = camera0.read()
    cv2.imshow("CSI Camera0", image0)

    #image1 = camera1.read()
    #cv2.imshow("CSI Camera1", image1)

    kk = cv2.waitKey(1)
    if kk == ord('q'): 
        break 