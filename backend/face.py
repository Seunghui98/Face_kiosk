import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import base64
import io
from flask import Flask, request, jsonify
import pandas as pd
import pymysql
import recommendation
from sklearn.metrics.pairwise import cosine_similarity



app = Flask(__name__)


def reg(face):
    # This is an example of running face recognition on a single image
    # and drawing a box around each person that was identified.

    # Load a sample picture and learn how to recognize it.
    iu_image = face_recognition.load_image_file("knowns/IU.jpg")
    iu_face_encoding = face_recognition.face_encodings(iu_image)[0]

    # Load a sample picture and learn how to recognize it.
    seok_image = face_recognition.load_image_file("knowns/1seok.png")
    seok_face_encoding = face_recognition.face_encodings(seok_image)[0]

    # Load a sample picture and learn how to recognize it.
    baewoo_image = face_recognition.load_image_file("knowns/baewoo.jpg")
    baewoo_face_encoding = face_recognition.face_encodings(baewoo_image)[0]

    # Load a sample picture and learn how to recognize it.
    seong_image = face_recognition.load_image_file("knowns/seong.png")
    seong_face_encoding = face_recognition.face_encodings(seong_image)[0]

    # Load a sample picture and learn how to recognize it.
    susu_image = face_recognition.load_image_file("knowns/susu.jpg")
    susu_face_encoding = face_recognition.face_encodings(susu_image)[0]

    # Load a sample picture and learn how to recognize it.
    suzy_image = face_recognition.load_image_file("knowns/suzy.jpg")
    suzy_face_encoding = face_recognition.face_encodings(suzy_image)[0]

    # Load a sample picture and learn how to recognize it.
    taetae_image = face_recognition.load_image_file("knowns/taetae.jpg")
    taetae_face_encoding = face_recognition.face_encodings(taetae_image)[0]

    # Load a sample picture and learn how to recognize it.
    Ujae_image = face_recognition.load_image_file("knowns/Ujae.jpg")
    Ujae_face_encoding = face_recognition.face_encodings(Ujae_image)[0]


    # Load a sample picture and learn how to recognize it.
    gong_image = face_recognition.load_image_file("knowns/gong.png")
    gong_face_encoding = face_recognition.face_encodings(gong_image)[0]

    # Load a second sample picture and learn how to recognize it.
    lsh_image = face_recognition.load_image_file("knowns/lsh.jpeg")
    lsh_face_encoding = face_recognition.face_encodings(lsh_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        iu_face_encoding,
        gong_face_encoding,
        lsh_face_encoding,
        seok_face_encoding,
        seong_face_encoding,
        susu_face_encoding,
        suzy_face_encoding,
        taetae_face_encoding,
        baewoo_face_encoding,
        Ujae_face_encoding
    ]
    known_face_names = [
        "iu",
        "gong",
        "hithere1012",
        "1seok",
        "seong",
        "susu",
        "suzy",
        "taetae",
        "baewoo",
        "Ujae"
    ]

    # Load an image with an unknown face
    unknown_image = face_recognition.load_image_file(face)

    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    # Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
    # See http://pillow.readthedocs.io/ for more about PIL/Pillow
    pil_image = Image.fromarray(unknown_image)
    # Create a Pillow ImageDraw Draw instance to draw with
    draw = ImageDraw.Draw(pil_image)

    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]


        return name

#     # Draw a box around the face using the Pillow module
#     draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
#
#     # Draw a label with a name below the face
#     text_width, text_height = draw.textsize(name)
#     draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
#     draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
#
#
# # Remove the drawing library from memory as per the Pillow docs
# del draw
#
# # Display the resulting image
# pil_image.show()
#
# # You can also save a copy of the new image to disk if you want by uncommenting this line
# # pil_image.save("image_with_boxes.jpg")

def who_id(id):
    # MySQL Connection 연결
    conn = pymysql.connect(host='localhost', user='root', password='1003126017a',
                           db='facekiosk', charset='utf8')

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()

    # SQL문 실행
    sql = "select * from member where id=%s"
    curs.execute(sql, id)

    # 데이타 Fetch
    rows = curs.fetchall()
    for row in rows:
        # print(row)
        # 출력 : {'category': 1, 'id': 1, 'region': '서울', 'name': '김정수'}
        # print(row['id'], row['name'], row['best'])
        # 1 김정수 서울
        conn.close()
        return row[3]

def rere(best_menu):
    data = pd.read_csv("log.csv", sep=",")
    new_menu = pd.DataFrame(columns=["menu", "new_menu"])
    new_menu["menu"] = data.menu.unique()
    new_menu["new_menu"] = range(data.menu.nunique())
    data = data.merge(new_menu, on="menu")

    data2 = data.sort_values(["id"])
    train = data2[:int(len(data)*0.7)]
    test = data2[int(len(data)*0.7):]

    score = np.zeros((train.id.nunique(), data2.new_menu.nunique()))
    traim_item_list = train.groupby("id").new_menu.apply(list)

    score = np.zeros((train.id.nunique(), data2.new_menu.nunique()))
    traim_item_list = train.groupby("id").new_menu.apply(list)

    print(traim_item_list)
    train_item_lst = traim_item_list


    train_item_lst = train_item_lst.tolist()
    for ix, item_lst in enumerate(train_item_lst):
        for item in item_lst:
            score[ix, item] = 1.0

    score_t = score.T
    cosine_sim = cosine_similarity(score_t, score_t)
    # 자기자신에 대한 유사도는 1.0 가끔 0.99997이 있기 때문에 사전 처리
    for i in range(data2.new_menu.nunique()):
        cosine_sim[i,i] = 1.0
    cosine_sim_data = pd.DataFrame(cosine_sim)

    print(cosine_sim_data)


    rec_lst = list(cosine_sim_data[best_menu].sort_values(ascending=False)[1:4+1].index)
    return rec_lst


@app.route('/upload', methods=['POST'])
def upload_file():

    payload = request.form.to_dict(flat=False)

    im_b64 = payload['image'][0]  # remember that now each key corresponds to list.
    # see https://jdhao.github.io/2020/03/17/base64_opencv_pil_image_conversion/
    # for more info on how to convert base64 image to PIL Image object.
    im_binary = base64.b64decode(im_b64)
    buf = io.BytesIO(im_binary)
    img = Image.open(buf)
    face_nana = reg(buf)
    best = who_id(face_nana)



    return jsonify({'아이디': face_nana, 'size': [img.width, img.height], 'best' : rere(best-1)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
