import cv2
import glob
import os
from tqdm import tqdm
import natsort
from PIL import Image
import img2pdf

input_dir = 'Images'
os.mkdir('Cropped')

i = 0

#orginal shape 1366x768
images = []
print("Sortowanie...")
for img in tqdm(glob.glob(input_dir + "/*.png")):
    images.append(img)

images_sorted = natsort.natsorted(images,reverse=False)


print("Obcinanie...")

for img in tqdm(images_sorted):
    image = cv2.imread(img)
    imgCropped = image[0:800, 430:910]
    cv2.imwrite("Cropped/image%0i.png" %i, imgCropped)
    i +=1
    #cv2.imshow('image',imgCropped)
    

    cv2.waitKey(30)
cv2.destroyAllWindows()

def generate_pdf():
    t = os.listdir('.')

    t = natsort.natsorted(t,reverse=False)

    with open("book.pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in tqdm(t) if i.endswith(".png")]))

os.chdir('Cropped')
generate_pdf()
print("Utworzono PDF")

