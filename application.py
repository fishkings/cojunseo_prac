from flask import Flask, render_template, request, redirect, url_for
import stack_data

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/apply')
def apply():
    return render_template('apply.html')

@application.route('/applyphoto')
def photo_apply():
    locations = request.args.get('location') # 특정 매개변수의 값을 가져올 때
    claeanes = request.args.get('clean')
    built_in = request.args.get('built')
    print(locations,claeanes,built_in)
    return render_template('apply_photo.html')

@application.route('/upload_done', methods=['POST'])
def upload_done():
    upload_file = request.files['file']
    upload_file.save('static/img/1.jpg')
    return redirect(url_for('index')) # 라우트 함수에 대한 URL 동적 생성 가능

@application.route('/list')
def list():
    return render_template('list.html')



if __name__ == '__main__':
    application.run(debug=True)