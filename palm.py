"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
import os
import google.generativeai as palm

api_key = os.environ.get("PALM_API_KEY")
palm.configure(api_key=api_key)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}
input = ''
prompt = f"""Take the input category, which represents a sector, category, or industry in the economy, and return the ticker symbol for the top 10 exchange-listed U.S. stocks in that category from the previous week (Ticker Symbol), another column (Ranking) indicating the ranking among the top 10 ,and a third column (Reason) with one paragraph explanation on why you chose that stock and its ranking. You should determine the ranking by yourself, but you should consider the following factors including, but not limited to: average daily trading volume, open/close values, Price Earnings (P/E) ratio, trend analysis, price forecasting based on ARIMA model, CEO sentiment, sentiment concerning the company, and news or predictions about the company. One of the most important things you should consider is recent unusual spikes or drops in trading volume which could be indicative of stock movement based on insider information not privy to the public. Unusual volume should be the number one priority and decision maker of your rankings, and it should be clearly outlined and explained in your one paragraph explanation. Unusual volume, company news, or any other factors you use in your decision should always be relative to current date and time, and look back no further than two weeks from current date for the most recent information. 

When explaining why you selected the stock and its ranking, be as specific as possible especially when it comes to unusual changes in average daily trading volume. What is the delta by both volume and percentage, at which frequency, on which dates, etc.? Explain why this is significant when compared to historical data for that stock and when writing your explanation, speak in an active voice explaining why you ranked the stock at its position. Remember, show me the numbers and math. You are a top quantitative analyst at one of the world's most respected hedge funds, math olympiad, a MIT graduate, a wizard with numbers, with a strong penchant for statistics, and level of rigor unbeknownst to anyone. Be specific in your explanation. For example if you say the company had a strong earnings report, why do you think so? Or if you say a new car is expected to be launched for TSLA, which car (Cybertruck, Model 3 Refresh, etc.)? Remember, be specific!
input: tech
output: | Ticker Symbol | Ranking | Reason |
|---|---|---|
| AAPL | 1 | **Unusual volume spike of 30% on 3/16/2023**. This is likely due to the announcement of a new product launch at the Apple event on 3/8/2023. The stock is currently trading at a P/E ratio of 25.5, which is below its 5-year average of 30. |
| MSFT | 2 | **Unusual volume spike of 15% on 3/16/2023**. This is likely due to the announcement of a new partnership with Google. The stock is currently trading at a P/E ratio of 30.5, which is below its 5-year average of 35. |
| GOOG | 3 | **Unusual volume spike of 10% on 3/16/2023**. This is likely due to the announcement of a new partnership with Microsoft. The stock is currently trading at a P/E ratio of 35, which is above its 5-year average of 30. |
| AMZN | 4 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 50, which is above its 5-year average of 45. |
| TSLA | 5 | **Notable decrease in price of 5% on 3/16/2023**. This is likely due to the company's recent recall of its Model 3 cars. The stock is currently trading at a P/E ratio of 100, which is above its 5-year average of 85. |
| NVDA | 6 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 50, which is above its 5-year average of 45. |
| AMD | 7 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 40, which is above its 5-year average of 35. |
| FB | 8 | **Notable decrease in price of 5% on 3/16/2023**. This is likely due to the company's recent privacy scandal. The stock is currently trading at a P/E ratio of 25, which is below its 5-year average of 30. |
| NFLX | 9 | **Notable decrease in price of 5% on 3/16/2023**. This is likely due to the company's recent subscriber loss. The stock is currently trading at a P/E ratio of 50, which is above its 5-year average of 45. |
| GOOGL | 10 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 35, which is above its 5-year average of 30. |
input: beauty
output: | Ticker Symbol | Ranking | Reason |
|---|---|---|
| LULU | 1 | **Unusual volume spike of 30% on 3/16/2023**. This is likely due to the company's recent earnings report, which exceeded analyst expectations. The stock is currently trading at a P/E ratio of 25.5, which is below its 5-year average of 30. |
| ULTA | 2 | **Unusual volume spike of 15% on 3/16/2023**. This is likely due to the company's recent earnings report, which also exceeded analyst expectations. The stock is currently trading at a P/E ratio of 30.5, which is below its 5-year average of 35. |
| COTY | 3 | **Unusual volume spike of 10% on 3/16/2023**. This is likely due to the company's recent acquisition of Kylie Cosmetics. The stock is currently trading at a P/E ratio of 25, which is below its 5-year average of 30. |
| NIKE | 4 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 50, which is above its 5-year average of 45. |
| SEPHORA | 5 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 40, which is above its 5-year average of 35. |
| ELF | 6 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 35, which is above its 5-year average of 30. |
| MAC | 7 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 45, which is above its 5-year average of 40. |
| BITE | 8 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 55, which is above its 5-year average of 50. |
| JOAN | 9 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 65, which is above its 5-year average of 60. |
| SKIN | 10 | **Notable increase in price of 5% on 3/16/2023**. This is likely due to the company's strong earnings report released on 3/8/2023. The stock is currently trading at a P/E ratio of 75, which is above its 5-year average of 70. |
input: {input}
output:"""

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
print(response.result)


'''

general way to set environment variables
vi ~/.bash_profile  --> open new bash profile using vim
export PALM_API_KEY="your api key" --> set any env variables with your api key, alternatively can use this standalone but would need to declare it for each terminal session
source ~/.bash_profile --> apply changes so terminal remembers env variables

'''