from flask import Flask, render_template, request, redirect, url_for
import stack_data
import database

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
    cleaness = request.args.get('clean')
    built_in = request.args.get('built')
    if cleaness == None : 
        cleaness = False
    else : 
        cleaness = True
    database.save(locations,cleaness,built_in)
    print(locations,cleaness,built_in)
    return render_template('apply_photo.html')

@application.route('/upload_done', methods=['POST'])
def upload_done():
    upload_file = request.files['file']
    upload_file.save(('cojunseo_prac/static/img/{}.jpg').format(database.now_index()))
    return redirect(url_for('index')) # 라우트 함수에 대한 URL 동적 생성 가능

@application.route('/list')
def list():
    house_list = database.load_list()
    print(house_list)
    length = len(house_list)
    return render_template('list.html',house_list = house_list, length = length)

@application.route("/house_info/<int:index>/")
def house_info(index):
    house_info = database.load_house(index)
    location = house_info["location"]
    cleaness = house_info["cleaness"]
    built_in = house_info["built_in"]
    photo = f"img/{index}.jpg"
    return render_template("house_info.html",location=location,
                           cleaness=cleaness,built_in=built_in,
                           photo = photo)

if __name__ == '__main__':
    application.run(debug=True)