from bottle import route, run, static_file, response
import os


@route('/')
def hello():
    return static_file(root=".", filename="hello.html")

@route('/nikolay')
def nikolay():
    return "Колян знает тропинки волшебных полян!"

@route('/phishing')
def phishing():
    return static_file(root=".", filename="phishing.html")

@route('/favicon.ico')
def hello():
    return "Hello World!"


@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="./static")

@route("/vk_files/<filename>")
def server_static(filename):
    return static_file(filename, root="./vk_files")

@route("/vk")
def server_static():
    response.content_type = 'text/html; charset=UTF8'
    return static_file("vk.html", root=".")

@route("/testd")
def server_static():
    return static_file("testd.py", root=".")




run(host="0.0.0.0", port=os.environ['PORT'])
# run(host="localhost", port="5000")
