<h1 align="center">Wave Trader BOT</h1>

# Advice
It's a working in progress project, anything that involves your financial live is your responsability, never invest more than you can afford to lose.
 
# Requirements
```
pip install python-binance
pip install binance
pip install colorama
pip install apscheduler
pip install requests
```

# Objectives and To-Do List
- [X] Read a cryptocurrency informations and filter average prices
- [ ] Create a easy settings file and a reader of thoses informations to be used inside the main.py
- [ ] Automatically calculate the best sell percentage price (optional usage)
- [ ] A average stabilizer to deal with price dumping
- [ ] A average stabilizer to deal with price bump
- [ ] UI visualizer (price candles, sell, buy, average and stop-loss lines)
- [ ] Verify the reason of every error and give to possible users the solution in a error message
- [ ] Create and release OCO or/and Limit orders
- [ ] Previous transaction verifier (if the bot crashes or lose connection), needs to be able to return in the last open transaction (IF True)
- [ ] Ask to generate a new average price if the actual price is lower than the buy price.
- [ ] If a new average has been created and the actual price still lower than the market price, buy the coin (since the price is lower than spected)
- [ ] Confidence system, create points for every transation (Ex.: If the bot decides to buy a coin even under the buy price line, the confidence is low, so if it hits the stop loss later, the bot will stop operating)
- [ ] If a new average has been created and the actual price still lower than the market price, buy the coin (since the price is lower than expected)
- [ ] Make it work in a web panel
