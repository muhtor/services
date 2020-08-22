from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.


class PriceView(View):
    template_name = "price.html"

    def get(self, request):
        if request.method == 'GET':
            context = {}
            try:
                price = int(request.GET['price'])
                count = len(str(price))
                if count > 3:
                    if count == 4:
                        context['data'] = str(price)[:1] + " " + str(price)[1:]
                    elif count == 5:
                        context['data'] = str(price)[:2] + " " + str(price)[2:]
                    elif count == 6:
                        context['data'] = str(price)[:3] + " " + str(price)[3:]
                    elif count == 7:
                        context['data'] = str(price)[:1] + " " + str(price)[-3:] + " " + str(price)[-3:]
                    elif count == 8:
                        context['data'] = str(price)[:2] + " " + str(price)[-3:] + " " + str(price)[-3:]
                    elif count > 8:
                        context['data'] = str(price)[:3] + " " + str(price)[-3:] + " " + str(price)[-3:]
                else:
                    context['data'] = price
                return render(request, self.template_name, context)
            except KeyError:
                return render(request, self.template_name, {'data': '...'})


class Separator(View):
    template_name = "separator.html"

    def get(self, request):
        if request.method == 'GET':
            vowels = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
            consonants = "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", \
                         "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"
            context = {}
            try:
                undefined_str = str(request.GET['str'])
                vowel_letters = ""
                consonant_letters = ""
                for v in undefined_str:
                    if v in vowels:
                        vowel_letters += v
                for c in undefined_str:
                    if c in consonants:
                        consonant_letters += c
                context['count_v'] = len(str(vowel_letters))
                context['count_c'] = len(str(consonant_letters))
                context['vowel'] = vowel_letters
                context['consonant'] = consonant_letters
                return render(request, self.template_name, context)
            except KeyError:
                return render(request, self.template_name, {'data': '...'})