import dotenv, os, requests, datetime, smtplib

dotenv.load_dotenv()

news_api_key = os.environ.get('NEWS_API')
stock_api_key= os.environ.get('STOCK_API')
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
  'function': 'TIME_SERIES_DAILY',
  'symbol': STOCK,
  'outputsize': 'compact',
  'datatype': 'json',
  'apikey': stock_api_key
}

news_params = {
  'q':STOCK,
  'apiKey': news_api_key,
}

def stock_change_of_five_percent_or_more():
  yesterday = str(datetime.datetime.now().date() - datetime.timedelta(days=1))
  two_days_ago = str(datetime.datetime.now().date() - datetime.timedelta(days=2))
  stock_res = requests.get(STOCK_ENDPOINT, params=stock_params)
  stock_res.raise_for_status()
  stock_data = stock_res.json()['Time Series (Daily)']
  yesterday_price = float(stock_data[yesterday]['4. close'])
  two_days_ago_price = float(stock_data[two_days_ago]['4. close'])

  difference = round(yesterday_price - two_days_ago_price , 2)
  change = round(difference/yesterday_price, 3)

  if change <= -.05 or change >= .05:
    return True
  return False

def get_news():
  articles =[]
  news_res = requests.get(NEWS_ENDPOINT, params=news_params)
  news_res.raise_for_status()
  news_data = news_res.json()
  for i in range(3):
    article = {
      'title' :news_data['articles'][i]['title'],
      'brief' : news_data['articles'][i]['description']
    }
    articles.append(article)
  return articles

def sendmail( subject, message):
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
      from_addr=email, 
      to_addrs=email, 
      msg=f"Subject:{subject}\n\n{message}"
      )
    
def create_message(articles):
  message =f'Here is some news relating to {STOCK}:\n\n'
  for article in articles:
    message +=f'{article["title"]}\n\n{article["brief"]}\n\n\n'
  return message

if stock_change_of_five_percent_or_more():
  articles = get_news()
  message = create_message(articles)
  sendmail(f'Significant change in {COMPANY_NAME} stock price', message)