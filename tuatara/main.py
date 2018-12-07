import json, tempfile, shutil, os


from flask import Flask, send_file, jsonify, redirect, url_for, abort, render_template, send_from_directory

import image_changer
import image_path_finder
import image_info_finder
import cors_workaround

app = Flask(__name__)

crossdomain = cors_workaround.crossdomain

mimetypes = {}
mimetypes["jpg"] = "image/jpeg"
mimetypes["tif"] = "image/tiff"
mimetypes["png"] = "image/png"
mimetypes["gif"] = "image/gif"
mimetypes["jp2"] = "image/jp2"
mimetypes["pdf"] = "application/pdf"
mimetypes["webp"] = "image/webp"

##### Outside of Spec
@app.route("/")
def hello_world():
    return "yoy"

@app.route("/robots.txt")
def go_away():
    return send_file("robots.txt")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/<filename>/file")
def get_image(filename):
    """Provides the original image without the IIIF wrapping"""
    filename = image_path_finder.main(filename)
    return send_file(filename, mimetype="image/jpg")



##### Official Spec
@app.route("/<filename>")
@crossdomain(origin="*")
def direct_to_info(filename):
    """
    From 2.1:
    When the base URI is dereferenced, the interaction should result in the image
    information document. It is recommended that the response be a 303 status
    redirection to the image information document’s URI.
    """
    return redirect(url_for("get_info", filename=filename), code=303)


@app.route("/<filename>/info.json")
@crossdomain(origin="*")
def get_info(filename):
    filepath = image_path_finder.main(filename)
    info = image_info_finder.main(filename, filepath)
    # info = json.dumps(info)
    return jsonify(info)


@app.route("/<filename>/<region>/<size>/<rotation>/<quality>")
@crossdomain(origin="*")
def get_derivative(filename, region, size, rotation, quality):
    filepath = image_path_finder.main(filename)
    quality, format = quality.split(".")
    with tempfile.TemporaryDirectory() as tmpdirname:
        try:
            shutil.copy(filepath, tmpdirname)
        except:
            abort(404)
        newPath = tmpdirname + "/" + filename + ".jpg"
        proceed, path_or_error = image_changer.main(newPath, region, size, rotation, quality, format)
        if proceed:
            if format in mimetypes:
                return send_file(path_or_error, mimetype=mimetypes[format])
            else:
                abort(400, description="File format is unacceptable")
        else:
            print("NOW PRINTING ERROR MESSGAGE")
            print(path_or_error)
            abort(400, description=path_or_error)


#### error handling
@app.errorhandler(400)
@crossdomain(origin="*")
def bad_request(e):
    return render_template('400.html', message=e.description), 400

@app.errorhandler(404)
@crossdomain(origin="*")
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
@crossdomain(origin="*")
def server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
