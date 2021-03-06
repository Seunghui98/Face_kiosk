import base64
import io
from PIL import Image
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():

    payload = request.form.to_dict(flat=False)

    im_b64 = payload['image'][0]  # remember that now each key corresponds to list.
    # see https://jdhao.github.io/2020/03/17/base64_opencv_pil_image_conversion/
    # for more info on how to convert base64 image to PIL Image object.
    im_binary = base64.b64decode(im_b64)
    buf = io.BytesIO(im_binary)
    img = Image.open(buf)

    return jsonify({'msg': 'success', 'size': [img.width, img.height]})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)

