import os
import sys
from flask import Flask, request, json, send_from_directory, send_file, render_template


def create_app(config_filename='config_file.py'):
    app = Flask(__name__, static_url_path='')
    app.config.from_pyfile(config_filename)
    return app


PATH = './volume'
app = create_app()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/settings.json', methods=['GET'])
def get_settings():
    settings_file_path = os.path.abspath(os.path.join(PATH, 'settings.json'))
    print(settings_file_path)
    return send_file(settings_file_path), 200


@app.route('/settings.json', methods=['POST'])
def update_settings():
    json_data: dict = request.json
    print(json_data)
    settings_path = os.path.abspath(f'{PATH}/settings.json')
    with open(settings_path, 'w') as file:
        json.dump(json_data, file)
    return send_file(settings_path), 200


@app.route('/list')
def get_file_list():
    directory = f'{PATH}/Data'
    print({"Elements": os.listdir(directory)})
    return {"Elements": (os.listdir(directory))}


@app.route('/file/<string:name>/')
def download_file(name):
    print(name)
    print(f'{PATH}/Data/{name}')
    directory = os.path.abspath(f'{PATH}/Data/')
    print(directory)
    try:
        return send_from_directory(directory, name)
    except FileNotFoundError:
        return 404


def save(data, filename):
    with open(filename, 'w') as file:
        print(f'Writing to {data}')
        file.write(data)


if __name__ == '__main__':
    PATH = sys.argv[1]
    PORT = int(sys.argv[2])
    app.run(port=4200)
