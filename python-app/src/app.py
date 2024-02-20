from prometheus_client import start_http_server, Gauge
import requests
import time

# Prometheusメトリクスを複数定義
xrp_usdt_last_price = Gauge('xrp_usdt_last_price', 'Last price of XRPUSDT')
xrp_usdt_index_price = Gauge('xrp_usdt_index_price', 'Index price of XRPUSDT')
xrp_usdt_mark_price = Gauge('xrp_usdt_mark_price', 'Mark price of XRPUSDT')
xrp_usdt_price_24h_pcnt = Gauge('xrp_usdt_price_24h_pcnt', '24h price percentage change of XRPUSDT')

def fetch_xrp_usdt_data():
    """Bybit APIからXRPUSDTのデータを取得し、複数のPrometheusメトリクスを更新する"""
    url = "https://api-testnet.bybit.com/v5/market/tickers?category=linear&symbol=XRPUSDT"
    response = requests.get(url)
    data = response.json()
    
    # API応答から複数の値を取得
    result = data['result']['list'][0]
    last_price = float(result['lastPrice'])
    index_price = float(result['indexPrice'])
    mark_price = float(result['markPrice'])
    price_24h_pcnt = float(result['price24hPcnt'])

    # Prometheusメトリクスを更新
    xrp_usdt_last_price.set(last_price)
    xrp_usdt_index_price.set(index_price)
    xrp_usdt_mark_price.set(mark_price)
    xrp_usdt_price_24h_pcnt.set(price_24h_pcnt)

if __name__ == '__main__':
    # Prometheusメトリクスサーバーを8000ポートで起動
    start_http_server(8000)
    
    # 無限ループでAPIからデータを定期的に取得
    while True:
        fetch_xrp_usdt_data()
        # 1秒待機
        time.sleep(1)
