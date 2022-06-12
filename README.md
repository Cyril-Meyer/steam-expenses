# steam-expenses
Calculate how much money you spent on steam.

*Warning : the scripts were developed using the French pages of steam, there may be some minor modifications to make for other languages*

### How to use the data scraping script

#### 1. Using your web browser to save the html file
* login into your steam account
* got the the [purchase history](https://store.steampowered.com/account/history/) page.
* *optional : show more transactions*
* save the file as `account_history.html`
* run the data extractor `python get_account_history_html.py --html account_history.html`

#### 2. Using requests and dev tools
* login into your steam account
* copy the `/account/history` request into `request.txt`
  * open dev tools
  * got to the network tab
  * got the the [purchase history](https://store.steampowered.com/account/history/) page.
  * select the `/account/history` call
  * copy as cURL (bash)
  * convert the the curl command into a python. Example tool [curlconverter.com](https://curlconverter.com/).
  * put the result string into request.txt
  * replace the `response = requests.post ...` with `response1 = requests.post ...`
* *optional : show more transactions*
  * select the `/account/AjaxLoadMoreHistory` call
  * copy as cURL (bash)
  * convert the the curl command into a python.
  * put the result string into request.txt
  * replace the `response = requests.post ...` with `response2 = requests.post ...`
* run the data extractor `python get_account_history_requests.py --requests request.txt`
