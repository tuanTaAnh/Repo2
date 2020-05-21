from flask import Flask, render_template, request, redirect, url_for, flash
from core.face_net import CelebModel, CelebModelOperations
import os
import logging
from werkzeug.utils import secure_filename
from threading import Thread
import shutil


UPLOAD_FOLDER = 'static/images/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logger = logging.getLogger('fr.main')
fr_model = None
    

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/setup")
def setup():
    message = None
    if fr_model == None:
        message = 'Setup in progress. Please wait for 5-10 minutes before trying anything.'
        Thread(target=do_setup, args=()).start()
    return redirect(url_for('index', message=message))


def do_setup():
    global fr_model

    if fr_model == None:
        logger.info('start building the model')
        celeb_model = CelebModel()
        logger.info('model build finished')
        fr_model = celeb_model.fr_model


@app.route("/")
@app.route("/<message>")
def index(message=None):
    return render_template('upload.html', message=message)


@app.route("/face_recognition", methods=["POST"])
def face_recognizer():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'image_file' not in request.files:
            return redirect(url_for('index'))
        file = request.files['image_file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(url_for('index'))

        if file and allowed_file(file.filename):
            try:
                shutil.rmtree(os.path.abspath('static/images'))
            except Exception as e:
                logger.warning(e)
            finally:
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=False)

            global fr_model
            if fr_model == None:
                return redirect(url_for('setup'))
      
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            celeb_identity = CelebModelOperations.recognize_celebs(
                file_path, fr_model
            )
            return render_template('result.html', image_path=file_path, celeb_identity=celeb_identity)

    return redirect(url_for('index'))


if __name__ == '__main__':
    # app.debug = True
    app.secret_key = 'many random bytes'
    port = int(os.environ.get('PORT', 5000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
    app.run(host='0.0.0.0', port=port)  #Start listening
