#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# #See PyCharm help at https://www.jetbrains.com/help/pycharm/
# importing librarys
import cv2
import numpy as npy
import face_recognition as face_rec
# function
def resize(img, size) :
    width = int(img.shape[1]*size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation= cv2.INTER_AREA)


# img declaration
Rishika = face_rec.load_image_file('sampe_images\Rishika.jpg')
Rishika = cv2.cvtColor(Rishika, cv2.COLOR_BGR2RGB)
Rishika = resize(Rishika, 0.50)
RIshika_test = face_rec.load_image_file('sampe_images\Bil Gates.jpg')
RIshika_test = resize(RIshika_test, 0.50)
RIshika_test = cv2.cvtColor(RIshika_test, cv2.COLOR_BGR2RGB)

# finding face location

faceLocation_Rishika = face_rec.face_locations(Rishika)[0]
encode_Rishika = face_rec.face_encodings(Rishika)[0]
cv2.rectangle(Rishika, (faceLocation_Rishika[3], faceLocation_Rishika[0]), (faceLocation_Rishika[1], faceLocation_Rishika[2]), (255, 0, 255), 3)

faceLocation_RIshika_test = face_rec.face_locations(RIshika_test)[0]
encode_RIshika_test = face_rec.face_encodings(RIshika_test)[0]
cv2.rectangle(RIshika_test, (faceLocation_RIshika_test[3], faceLocation_RIshika_test[0]), (faceLocation_RIshika_test[1], faceLocation_RIshika_test[2]), (255, 0, 255), 3)

results = face_rec.compare_faces([encode_Rishika], encode_RIshika_test)
print(results)
cv2.putText(RIshika_test, f'{results}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255), 2 )

cv2.imshow('main_img', Rishika)
cv2.imshow('test_img', RIshika_test)
cv2.waitKey(0)
cv2.destroyAllWindows()