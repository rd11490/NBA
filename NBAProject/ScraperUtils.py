from datetime import *

__author__ = 'ryan'


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def convertNameToId(name):
    name_to_id = {'TOR': 28, 'BOS': 2, 'BKN': 3, 'NYK': 20, 'PHI': 23, 'IND': 12, 'CHI': 5, 'CLE': 6, 'DET': 9,
                  'MIL': 17, 'MIA': 16, 'WAS': 30, 'CHA': 4, 'ATL': 1, 'ORL': 22, 'OKC': 21, 'POR': 25, 'MIN': 18,
                  'DEN': 8, 'UTA': 29, 'LAC': 13, 'GSW': 10, 'PHO': 24, 'SAC': 26, 'LAL': 14, 'SAS': 27, 'HOU': 11,
                  'MEM': 15, 'DAL': 7, 'NOP': 19, 'NOH': 19, 'NOK': 19, 'NJN': 3, 'CHO': 4, 'SEA': 21, 'BRK': 3}
    return name_to_id[name]


def boxscoreURLToPlayByPlay(url):
    insert_ind = url.rfind('/')
    return url[:insert_ind] + '/pbp' + url[insert_ind:]

def boxscoreURLToShotChart(url):
    insert_ind = url.rfind('/')
    return url[:insert_ind] + '/shot-chart' + url[insert_ind:]

def dateFormat(date):
    newDate = datetime.strptime(date, '%a, %b %d, %Y')
    return newDate.strftime('%Y-%m-%d')

def currentSeason():
    basedate = datetime.today().replace(month=9, day=1)
    today = datetime.today()
    if today.month > basedate:
        return today.year
    else:
        return today.year-1

def URLtoID(url):
    return url[url.rfind('/') + 1:url.find('.html')]

# Converts a row of a table in HTML into a list
def rowToList(row):
    data_row = []
    data = row.find_all('td')
    for d in data:
        text = d.text
        if isNumber(text):
            text = float(text)
        elif text == '':
            text = 0.0
        else:
            text = text.format('ascii')  #for pickling
        data_row.append(text)
    return data_row

def frameToList(frame):
    return map(list, frame.values)