from django.shortcuts import render
from django.views import View
import json
JSON = 'data_parse/data'
# Create your views here.

new = [
    {"id": 2, "name": "eshmat", "age": 24, "lang": "uz"},
    {"id": 3, "name": "toshmat", "age": 25, "lang": "ru"}
]


class ParserView(View):
    """http://127.0.0.1:8000/parser/data"""

    def parse_data(self, data):
        # data = {'people': []}
        # data['people'].append({
        #     'name': 'Scott',
        #     'website': 'stackabuse.com',
        #     'from': 'Nebraska'
        # })
        with open(JSON + '.json', '+a') as outfile:
            json.dump(data, outfile)
            # _id = load_data[0]['id']
            # data['id'] = _id + 1
            # load_data.append(data)
            # return load_data

    template_name = "parser.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = {
            "id": 0,
            "name": request.POST['name'],
            "age": request.POST['age'],
            "lang": request.POST['lang']
        }
        result = self.parse_data(data=data)
        print("Rs...", result, type(result))
        return render(request, self.template_name)


