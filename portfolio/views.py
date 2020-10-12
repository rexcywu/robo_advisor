from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Stocks
import yfinance as yf

class StocksListView(ListView):
    # stocks_list.html 
    model = Stocks

    def get_queryset(self):
        # only shows owner's stocks
        return self.model.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        tickers = self.model.objects.filter(owner=self.request.user).values("symbol")
        prices = []
        # today's price of stock
        for ticker in tickers:
            symbol = ticker['symbol']
            ticker = yf.Ticker(symbol)
            price = format(ticker.history(period="1d")["Close"][0], '.2f')
            prices.append(price)

        # append today's price to the original context
        context['object_list'] = zip(prices, context['object_list'])
        # check if the user have created the portfolio or not
        if len(prices) == 0:
            context['exist'] = False
        else:
            context['exist'] = True   
        return context


class StocksCreateView(LoginRequiredMixin, CreateView):
    # stocks_form.html 
    model = Stocks
    fields = ['symbol', 'amount']

    def form_valid(self, form):
        # https://aroussi.com/post/python-yahoo-finance
        # retrieve data from yahoo finance API
        ticker = yf.Ticker(form.instance.symbol)
        form.instance.name = ticker.info['shortName']
        day_price = ticker.history(period="1d")["Close"][0]
        form.instance.buying_price = format(day_price, '.2f')
        form.instance.owner = self.request.user
        return super().form_valid(form)







    