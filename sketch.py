import cv2
import os
import matplotlib.pyplot as plt

while True:

    root = input(str("Elija la ruta origen: "))

    img = cv2.imread(f'{root}.jpg')

    cv2.imshow(f'{root}.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.imshow(img)
    plt.axis(False)

    plt.imshow(img[:,:,::-1])
    plt.axis(False)

    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(RGB_img)
    plt.axis(False)

    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert_img=cv2.bitwise_not(grey_img)

    blur_img=cv2.GaussianBlur(invert_img, (111,111),0)
    invblur_img=cv2.bitwise_not(blur_img)

    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
    os.makedirs('SKETCHES', exist_ok = True)
    sketch = input(str("Dime con que nombre quieres guardar el sketch: "))
    cv2.imwrite(f'SKETCHES/{sketch}.jpg', sketch_img)

    cv2.imshow(f'SKETCHES/{sketch}.jpg',sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.figure(figsize=(14,8))
    plt.subplot(1,2,1)
    plt.title(f'PHOTOS/{image}.jpg', size=18)
    plt.imshow(RGB_img)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.title(f'SKETCHES/{sketch}.jpg', size=18)
    rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_sketch)
    plt.axis('off')
    plt.show()