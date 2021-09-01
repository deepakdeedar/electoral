import requests
import json


class captcha_solver:
    def get_captcha_text():
        payload = {'isOverlayRequired': False,
                   'apikey': 'helloworld',
                   'language': 'eng',
                   }
        with open('captcha.png', 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                              files={'captcha.png': f},
                              data=payload,
                              )
        test_file = r.content.decode()
        jsonString = json.loads(test_file)

        try:
            return jsonString['ParsedResults'][0]['ParsedText']
        except:
            return jsonString['ParsedResults'][2]
