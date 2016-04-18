import requests
from multiprocessing.dummy import Pool as ThreadPool

localstr="""http://localhost:8000/polls/api?img=iVBORw0KGgoAAAANSUhEUgAAADwAAAAWCAYAAACcy/8iAAADZElEQVRYR+VYW7akIAyENcGaZE24JlwTc4pYEtIi7dz5mDnjT/uAmKRSldi+lFLdf3T4nHPdtu0x5OM4XAjhWoNr3sOv3b96/ifyu+/7x3uf7GI9YvBAWAdzt8kGjDX6Hs5nx8r27wZ/59PMd9yHH9izRPgpkxpJWwG8ZmZ1RfDl+H2TEB3kCmG+1/q1RPgJSe24zu632WelvKkOmzi7l9V2l8glwt43lxzYi6LFb6mdy3jq/e6CC+4415UqeqARiH5XFg5Xav6IMfo0vCfX3EpQB3gkeEFPDrcVWQMN0ZXE6ztt+UCYGUqRQdjfHnT05G53AmlBUuioBCvJ6qvGoCXYnjSuQ9A8kk+DBVpE0OTonbZ8lDRVWtc8kS1FyE7E9gSnnKs1DMjWKhlGRgVx57bs3A4fz4PIIzg6C6TlWg4ij2SlKHZCDk4jyyQkH699uZZ2fkclHVcr6SeVtga8l/IGgkRXl7g4KjTIJbgUZX0+y5weAvWWlBLcHkEGrO+tEUkWRLE3D+cMrIEQpTK2sxJm3YKgLTmMBTGO5bhl6ckzdWUJA1F9zmCR8SMhJRLkjIPRxxZMD3jkLOwRZXJ5pv5aB5YIWy6jzHnYoCXA4PJJBQYMtPUectYi3ytABGwrW0usBCbBW4SlCkpLHI4ZEHw+7cO2z7GcgQw4azmj1boUES1ymPzVJQ2MV2rNCiCHtSrfIUxVprq/UumOY59SWN7kbVf0rr86OM1VbY/cBoc1KmxNuAd0LxpEUXp9r3PYuXAq9azyeH/KYao01JhICmKi0ijrq+00YZKWQmTJJSKMkh776cjhVranKjf7pk9DwJr9WoZ+eyQmovdjnVh7PlVpKV8GIdugvld/vDgqvAFn7w4gyYPIJ7+fQ0poKi22ZXjhtbUFNbZ9d2+oi3324qdg+WzgsJ5sUL5dn2W5nrTGCetzaLjru1rv0actsnY4QRLQh7FOB60Do2Ddze5fcVgb00jbsbJPWXrHyGXNcR0M1JnP2If1pKUtjlzuSFO1rTrr2UH35a+/llZlotXczr5P38mz4Z4O00HNfd1nv7mv3//V9/Bsclkl4W98/iOE7/rc7Pt09l2qkXybIP1++7399H29nKXfOjJbr8uviZ/6u+gn77Acha2nievqw2+58S+v/wVOPqPGzG8yrwAAAABJRU5ErkJggg=="""

pip_die="http://localhost:8080/"
#urls = [
#        'http://www.python.org',
#        'http://www.python.org/about/',
#        'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
#        
#        # etc..
#        ]
urls=[pip_die for i in range(200)]
# Make the Pool of workers
pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
results = pool.map(requests.get, urls)
#close the pool and wait for the work to finish
pool.close()
pool.join()

endof=list(map(lambda x:x.content.decode(),results))
print(endof[0])

# results = []
# for url in urls:
#         result = urllib2.urlopen(url)
#         results.append(result)
 
# # ------- VERSUS ------- #
 
 
# # ------- 4 Pool ------- #
# pool = ThreadPool(4)
# results = pool.map(urllib2.urlopen, urls)
 
# # ------- 8 Pool ------- #
 
# pool = ThreadPool(8)
# results = pool.map(urllib2.urlopen, urls)
 
# # ------- 13 Pool ------- #
 
# pool = ThreadPool(13)
# results = pool.map(urllib2.urlopen, urls)
 
#                            Single thread:  14.4 Seconds
#                                   4 Pool:   3.1 Seconds
#                                   8 Pool:   1.4 Seconds
#                                  13 Pool:   1.3 Seconds
