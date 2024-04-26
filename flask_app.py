from flask import Flask

@app.route ('/')
def home () :
    return "<p>Website met vallen en opstaan.</p>"


app=Flask(__name__)
if __name__ == '__main__':
    app.run (port=5000,debug=True)