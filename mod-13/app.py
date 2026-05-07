from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    on_alkuluku = True

    if luku < 2:
        on_alkuluku = False
    else:
        for i in range(2, luku):
            if luku % i == 0:
                on_alkuluku = False

    vastaus = {
        "Number": luku,
        "isPrime": on_alkuluku
    }

    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)