from bs4 import BeautifulSoup
import urllib.request
import re
import json

def parse_url(url):
    print("Parsing: {}".format(url))
    racquets = []

    # pull type of racquet from the url
    if "tennis" in url:
        racquet_type = "tennis"
    elif "racquetball" in url:
        racquet_type = "racquetball"
    elif "squash" in url:
        racquet_type = "squash"
    elif "badminton" in url:
        racquet_type = "badminton"

    manufacturer  = url.split("/")[-1]
    manufacturer  = "-".join(manufacturer.split("-")[:-3])

    with urllib.request.urlopen(url) as response:

        html_doc = response.read()
        soup = BeautifulSoup(html_doc, features="html.parser")

        table = soup.find('table')

        for row in table.find_all('tr')[1:]:
            columns = row.find_all(['td'])
            #data = {
            #    'Racquet Name': columns[0].text,
            #    'Tension': columns[1].text,
            #    'Length': columns[2].text,
            #    'Pattern': columns[3].text,
            #    'Skip M Holes': columns[4].text,
            #    'Tie Off M': columns[5].text,
            #    'Start C': columns[6].text,
            #    'Tie Off C': columns[7].text
            #    }

            # tension ex: 50 - 60
            # Dunlop ADRENALINE RUSH 108: 50 -65
            #   hence the ugly regex
            tension = re.split("\W{2,3}", columns[1].text)
            if len(tension) < 2:
                tension.append(0)
            # length ex: 20'M - 18'C
            length = re.findall("\d+", columns[2].text)
            # pattern ex: 20'M - 18'C
            # Dunlop REVELATION DP SUPER & SELECT PRO has no crosses and mains listed
            pattern = re.findall("\d+", columns[3].text)
            if len(pattern) < 2:
                pattern = [0,0]

            data = {
                'racquet_name': columns[0].text,
                'tension_upper': tension[0],
                'tension_lower': tension[1],
                'length_mains': length[0],
                'length_crosses': length[1],
                'num_crosses': pattern[0],
                'num_mains': pattern[1],
                'skip_mains': columns[4].text,
                'tie_mains': columns[5].text,
                'start_crosses': columns[6].text,
                'tie_crosses': columns[7].text,
                'type': racquet_type,
                "manufacturer": manufacturer
                }
            #print(data)
            racquets.append(data)

        return(racquets)

def save_data(filename, data):
    with open(filename, "w") as f:
        f.write(data)


def scraper():

    racquet_data = []

    stubs = [
        "asics-tennis",
        "babolat-tennis",
        "black-knight-badminton",
        "black-knight-squash",
        "carlton-badminton",
        "donnay-tennis",
        "dunlop-squash",
        "dunlop-tennis",
        "e-force-racquetball",
        "ektelon-racquetball",
        "fischer-tennis",
        "gamma-tennis",
        "gearbox-racquetball",
        "head-racquetball",
        "head-squash",
        "head-tennis",
        "prince-badminton",
        "prince-squash",
        "prince-tennis",
        "pro-kennex-racquetball",
        "pro-kennex-tennis",
        "slazenger-tennis",
        "spalding-racquetball",
        "spalding-tennis",
        "tecnifibre-squash",
        "tecnifibre-tennis",
        "transition-racquetball",
        "volkl-tennis",
        "weed-tennis",
        "wilson-badminton",
        "wilson-racquetball",
        "wilson-squash",
        "wilson-tennis",
        "yonex-badminton",
        "yonex-tennis",
    ]


    for stub in stubs:
        full_url = "https://klipperusa.com/pages/{}-racquet-patterns".format(stub)

        data = parse_url(full_url)
        racquet_data = racquet_data + data

    save_data("racquet_data.json", json.dumps(racquet_data))


scraper()