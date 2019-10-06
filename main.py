
from flask import Flask
app = Flask('synopsys')


@app.route('/')
def test():
    return "synopsys!\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
