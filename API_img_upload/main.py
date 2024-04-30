from flask import Flask, request, send_from_directory, render_template
import os
app = Flask(__name__)
# directory to store uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# route to handle the file upload to folder name uploads
@app.route('/upload', methods=['POST'])
def upload_image():

    image = request.files['image']
    # saving uploaded image to the  folder
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    # Return the filename
    return render_template('result.html', filename=image.filename)


# display uploaded image
@app.route('/uploads/<filename>')
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# HTML page to upload and display image
@app.route('/')
def upload_form():
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
