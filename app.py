from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
        HELLO WORLD!<br>
        #PBW3B1PBL0101<br>
        251080200006<br>
        MOCH SULTAN ZAKY<br>
        Framework Pilihan -> Python[16] -> BlueBream<br>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)