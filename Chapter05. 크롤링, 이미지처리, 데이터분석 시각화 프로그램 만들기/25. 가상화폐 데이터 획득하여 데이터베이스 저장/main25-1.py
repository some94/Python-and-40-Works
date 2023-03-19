import pyupbit
# 거래되고 있는 가상화폐 출력
coin_lists = pyupbit.get_tickers(fiat='KRW')
print(coin_lists)
# 비트코인과 이더리움의 한국 시세 출력
price_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
print(price_now)