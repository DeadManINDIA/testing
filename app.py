
from flask import Flask
app = Flask('synopsys')


@app.route('/')
def test():
    return "synopsys!\n"



