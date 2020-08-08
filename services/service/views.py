from django.shortcuts import render
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
