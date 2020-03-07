from flask import render_template, Flask, jsonify, request, url_for, flash
from flask_restful import Resource, Api, reqparse, abort
import flask 
import configparser
import json
from summarizer import Summarizer

app = Flask(__name__)
api = Api(app)
base_url = '3.133.92.223'



@app.route('/status/<string:keyword>',methods=['GET'])
def getStatus(keyword):
    data = {}
    data['keyword'] = keyword
    data['status'] = ''
    data['error'] = ''
    try:
        if app.mykeyword == "":
            raise NameError("keyword not post yet")
        if app.mystatus == 0:
            data['status'] = 'finished'
        elif app.mystatus == -1:
            data['status'] = 'keyword not exist!'
        else:
            data['status'] = 'not yet'
    except:
        data['error'] = 'not exist!'
    return jsonify(keyword=data['keyword'],
                    status=data['status'],
                    error=data['error'])

@app.route('/video/<string:keyword>',methods=['GET'])
def getVideo(keyword):
    try:
        return flask.send_file(keyword+'.mp4')
    except:
        return abort(404, message="keyword doesn't exist")


@app.route('/', methods=['POST'])
def post():
    data = {}
    data['keyword'] = ''
    data['get_status'] = ''
    data['get_video'] = ''
    try:
        app.mykeyword = request.form['keyword']
        data['keyword'] = app.mykeyword
        oldapi = Summarizer(data['keyword'], data['keyword'],"keys")
        app.mystatus = oldapi.keyToVideo()
        data['get_status'] = base_url + 'status/' + data['keyword']
        data['get_video'] = base_url + 'video/' + data['keyword']
        return jsonify(keyword=data['keyword'],
                    get_status=data['get_status'],
                    get_video=data['get_video'])
    except:
        data['keyword'] = 'breaking'
        Summarizer('breaking', 'breaking',"keys").keyToVideo()
        data['get_status'] = base_url + 'status/' + data['keyword']
        data['get_video'] = base_url + 'video/' + data['keyword']
        return jsonify(keyword=data['keyword'],
                    get_status=data['get_status'],
                    get_video=data['get_video'])

        

if __name__ == '__main__':
    app.mykeyword = ""
    app.mystatus = -1
    app.run(debug=True,host='0.0.0.0',port=8080)