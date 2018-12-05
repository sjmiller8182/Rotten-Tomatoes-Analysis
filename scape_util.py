import time
import datetime

def build_url(year):
    """Builds url for wikipedia 'year in film'

    Parameters
    ----------
    year : str
        year to scrape movie titles from

    Returns
    -------
    str
        formatted url
    """
    
    current_year = datetime.datetime.now().year
    base_url = 'https://en.wikipedia.org/wiki/'
    
    if int(year) >= 1960 and int(year) <= current_year:
        url = base_url + year + '_in_film'
    else:
        raise Exception('Input year must be later than 1960 and not later than the current year')
    return url
            
def make_soup(url, crawl_rate = 1.5):
    """Request url and get content of page as html soup

    Parameters
    ----------
    url : str
        The url to scrape from RT
    crawl_rate : float
        Time in seconds between secessive requests
        This should be considered the minimum time
        
    Returns
    -------
    bs4 object
        html content from bs4 html parser
    """
    
    time.sleep(crawl_rate)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup