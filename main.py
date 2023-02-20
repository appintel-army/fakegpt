from flask_cors import CORS
from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import textwrap
import io

app = Flask(__name__)
CORS(app)  # enable CORS


# Define endpoint for generating the image
@app.route('/generate_image', methods=['POST'])
def generate_image():
    # Get the question and answer from the request
    data = request.json
    que = data['que']
    ans = data['ans']

    # Open the image template
    template = Image.open('temp.jpg')

    myfont = ImageFont.truetype('arial.ttf', size=14)
    rect = (170, 167, 100, 50)
    spacing = 10

    # Create a drawing object
    draw = ImageDraw.Draw(template)

    # Add the question to the image
    text_lines1 = textwrap.wrap(que, width=100)
    y_text1 = 80
    for line in text_lines1:
        line_width, line_height = myfont.getsize(line)
        draw.text((170, y_text1), line, font=myfont, fill=(0, 0, 0))
        y_text1 += line_height + spacing

    # Add the answer to the image
    text_lines = textwrap.wrap(ans, width=100)
    y_text = rect[1]
    for line in text_lines:
        line_width, line_height = myfont.getsize(line)
        draw.text((rect[0], y_text), line, font=myfont, fill=(0, 0, 0))
        y_text += line_height + spacing

    # Save the modified image to a file-like object
    img_bytes = io.BytesIO()
    template.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    # Return the modified image as a response
    return send_file(img_bytes, mimetype='image/png')


if __name__ == '__main__':
    app.run()
