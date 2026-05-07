from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/alkuluku/<int:luku>")
def tarkista_alkuluku(luku):
    tulos = True

    if luku < 2:
        tulos = False

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            tulos = False

    return jsonify({
        "luku": luku,
        "on_alkuluku": tulos
    })

app.run(host="127.0.0.1", port=3000)