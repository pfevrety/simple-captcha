import flask
from captcha import Captcha

app = flask.Flask(__name__)

captchas = []


# Routes
@app.route('/')
def createCaptcha():
    length = len(captchas)
    captcha = Captcha(length)
    captchas.append(captcha)
    return flask.make_response(flask.jsonify({"captcha_index": captcha.index, "image": str(captcha.img)}), 200)


@app.route('/', methods=["POST"])
def captchaVerification():
    index = int(flask.request.args.get('index'))
    data = flask.request.get_json()
    answer = captchas[index].text

    if index is None:
        return flask.make_response(flask.jsonify({"error": "Captcha index not provided"}), 200)

    if data['text'] is None:
        return flask.make_response(flask.jsonify({"error": "Captcha index not provided"}), 200)

    if answer == data['text']:
        return flask.make_response(flask.jsonify({"message": "Captcha success"}), 200)
    return flask.make_response(flask.jsonify({"message": "Invalid captcha"}), 403)


if __name__ == '__main__':
    app.config['DEBUG'] = False
    app.run(host='0.0.0.0', port=8888)
