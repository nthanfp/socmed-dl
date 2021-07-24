from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
from pyquery import PyQuery as pq
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/pinterest')
def pinterest():
    link = request.args.get('url')
    post_request = requests.post(
        'https://www.expertsphp.com/download.php',
        data={'url': link}
    )
    request_content = post_request.content
    str_request_content = str(request_content, 'utf-8')
    download_url = pq(str_request_content)(
        'table.table-condensed')('tbody')('td')('a').attr('href')

    if '.mp4' in str(download_url):
        json = jsonify(error=0, media_url=download_url, type="mp4")
    elif '.jpg' in str(download_url):
        json = jsonify(error=0, media_url=download_url, type="jpg")
    else:
        json = jsonify(error=1, message='Not found')

    return json


@app.route('/tiktok')
def tiktok():
    link = request.args.get('url')
    url = "https://www.mysimplesapps.com/v1/tiktok/video/metadata"
    body = {
        "key": "HFHLHKRP04#B@#GdryPLPR*09#4^7!WABMjY!@OK",
        "name": " ",
        "url": link
    }
    headers = {'Content-Type': 'application/json'}

    # Making http post request
    response = requests.post(url, headers=headers, json=body, verify=False)
    request_content = response.content

    return request_content


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
