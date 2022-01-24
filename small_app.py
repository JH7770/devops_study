from flask import Flask, redirect, request

app = Flask('basic app')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'q' in request.args.keys():
            redirect('http://www.google.com/search?q=%s'%request.args['q'])
        else:
            return '', 403
    else:
        return '<h1>GET request from Flask</h1>'

if __name__ == "__main__":
    app.run()