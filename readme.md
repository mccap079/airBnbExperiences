[AirBnB Experinces](https://www.airbnb.com/s/experiences?refinement_paths%5B%5D=%2Fexperiences)
===

Scraping the following items:

 - `title`: “Paris’ Best Kept Secrets Tour”
 - `kicker_text`: “history walk · Paris”
 - `country`: “France”
 - `picture`: “https://a0.muscache.com/im/pictures/571e0e7b-6867-4c44-bd91-776a5d698fae.jpg”
 - `star_rating`: 5.0
 - `lat`: 48.8674018702
 - `lng`: 2.32934203089

from all AirBnB Experiences posts and posting them to my instagram account. 

`get_airbnb_to_json.py` scrapes the airbnb.com site and prints data in json friendly strings. Pipe this output to a .json file like so:

`python get_airbnb_to_json.py > output.json`

See `output.json` for an example of the output (which was scraped on Feb 12 2018).

`download_images.py` uses [urllib](https://docs.python.org/2/library/urllib.html) to download every image from the `picture` key's url value in `output.json` into a folder called `img` in your working directory.

`post_to_ig.py` uses [instapy-cli](https://github.com/b3nab/instapy-cli) to post all these pics to IG with captions based on some of the other data pulled from airbnb