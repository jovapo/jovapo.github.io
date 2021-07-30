# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import io, csv

def make_file_contents(title, date, venue, authors, title_single, venue2, title2, date2):
    return f"""---
teaser: "/publications/{date}-{venue}-{title_single}/teaser.jpg"
title: "{title}"
collection: publications
excerpt: 
date: {date}-1
venue: "{venue}"
authors: "{authors}"
permalink: "publications/{date}-{venue}-{title_single}/index"
paperurl: # {date}-{venue}-{title_single}/{date}-{venue}-{title_single}.pdf
supurl: # {date}-{venue}-{title_single}/{date}-{venue}-{title_single}-sup.pdf
posterurl: # {date}-{venue}-{title_single}/{date}-{venue}-{title_single}-poster.pdf
slidesurl: # {date}-{venue}-{title_single}/{date}-{venue}-{title_single}-slides.pdf
codeurl: # {date}-{venue}-{title_single}/{date}-{venue}-{title_single}-code.zip
venue2: "{venue2}"
title2: "{title2}"
authors2: "{authors}"
date2: {date2}-1
paper2url: 
---


"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('/Users/tighej/website/jovapo.github.io/citations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(spamreader):
            if i == 0:
                continue
            title = row[1]
            date = f"{row[4]}-{row[3]}"
            venue = row[2]
            aurthors_raw = row[0]
            aurthor_list = []
            for aurthor in aurthors_raw.split(';'):
                if ',' in aurthor:
                    last, first = aurthor.split(',')
                    aurthor_list.append(f"{first.strip()} {last.strip()}")
            authors = ', '.join(aurthor_list)
            title_single = row[5]
            if len(title_single) < 2:
                title_single = title.split(' ')[0]
            if len(date) == 0 or len(authors) == 0 or len(title) == 0:
                continue
            venue2 = row[6]
            title2 = row[7]
            date2 = f"{row[9]}-{row[8]}"
            out_str = make_file_contents(title, date, venue, authors, title_single, venue2, title2, date2)
            file_name = f"{date}-{venue.replace(' ','-')}-{title_single}"
            print(out_str)
            with open(f'/Users/tighej/website/jovapo.github.io/_publications/{file_name}.md','w') as out_file:
                out_file.write(out_str)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
