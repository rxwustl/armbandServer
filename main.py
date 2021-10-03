from flask import *
app = Flask(__name__)


@app.route('/test', methods=['get'])
def test_api():
    return "<h1>some response</h1>"


@app.route('/demo_api', methods=['post'])
def demo():
    content = request.get_json(force=True)
    PPGdata = content['ppg']
    print(PPGdata)
    response_data = {
        "Sys": 108,
        "Low": 88
    }
    return response_data


if __name__ == '__main__':
    app.run(host='localhost', port=5000)