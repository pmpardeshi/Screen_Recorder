import cv2

img = cv2.imread('sof.png') # load a dummy image
while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(0)
    if k==32:    # space key to stop
        break
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    else:
        print(k) # else print its value

cv2.destroyAllWindows()