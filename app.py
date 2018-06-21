import os
import subprocess

from bottle import route, run, static_file, template

ROOT = os.path.dirname(os.path.abspath(__file__))
WWW = os.path.join(ROOT, 'www')
STATIC = os.path.join(WWW, 'static')


@route('/')
def index():
    return template('www/index.html')


@route('/start-cmd/<cmd>')
def start_cmd(cmd):
    # Not using cmd for now
    subprocess.Popen(os.path.join(ROOT, 'command.py'))
    return ""  # Not returning anything useful


@route('/get-progress/<cmd>')
def get_progress(cmd):
    try:
        with open('progress.txt') as f:
            progress = f.read()
    except OSError:
        progress = '0'
    return progress


@route('/static/<path:path>')
def callback(path):
    return static_file(path, root=STATIC)


if __name__ == "__main__":
    run(host='0.0.0.0', port=8080, reload=True)
