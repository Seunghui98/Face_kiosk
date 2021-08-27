import face_recognition
import cv2
import camera
import os
import numpy as np

class FaceRecog():

    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.1
        self.camera = camera.VideoCamera()

        self.known_face_encodings = []
        self.known_face_names = []

        # Load sample pictures and learn how to recognize it.

        dirname = 'knowns'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg' or ext == '.png' or ext =='.jpeg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def __del__(self):
        del self.camera

    def get_frame(self, image):

            # Find all the faces and face encodings in the current frame of video

            face_encoding = face_recognition.face_encodings(image)[0]
            face_names = []
            for face_encoding in self.face_encodings:
                # See if the face is a match for the known face(s)
                distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                min_value = min(distances)

                # tolerance: How much distance between faces to consider it a match. Lower is more strict.
                # 0.6 is typical best performance.
                name = "Unknown"
                if min_value < 0.6:
                    index = np.argmin(distances)
                    name = self.known_face_names[index]


                self.face_names.append(name)


            return name
        # # Display the results
        # for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
        # # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        #     top *= 4
        #     right *= 4
        #     bottom *= 4
        #     left *= 4
        #
        #     # Draw a box around the face
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #
        #     # Draw a label with a name below the face
        #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #     x = name

        # return frame

    def get_jpg_bytes(self):
        frame = self.get_frame()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()


if __name__ == '__main__':
    face_recog = FaceRecog()
    face_image = face_recognition.load_image_file("LEE.jpeg")
    print(face_recog.known_face_names)
    # while True:
    name = face_recog.get_frame(face_image)
    print("이름1 = " + name)
        # show the frame

        # key = cv2.waitKey(1) & 0xFF
        #
        # # if the `q` key was pressed, break from the loop
        # if key == ord("1"):
        #     break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')