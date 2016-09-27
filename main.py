from bottle import route, run, static_file, response, template, error
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


@route("/static/img/<filename>")
def server_static(filename):
    return static_file(filename, root="./static/img")


@route("/vk_files/<filename>")
def server_static(filename):
    return static_file(filename, root="./vk_files")


@route("/vk")
def server_static():
    response.content_type = 'text/html; charset=UTF8'
    return static_file("vk.html", root=".")


@route("/love/<i>")
def server_static(i):
    return template("templates/test.tpl", a=int(i))


@error(404)
def error404(error):
    return static_file("error404.html", root=".")

run(host="0.0.0.0", port=os.environ['PORT'])
# run(host="localhost", port="5000")
