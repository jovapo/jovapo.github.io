# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import io, csv, os

def make_file_contents(title, date, venue, authors, title_single, venue2, title2, date2, authors2):
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
authors2: "{authors2}"
date2: {date2}-1
paper2url: 
---


"""

def make_author_list(authors_raw):
    author_list = []
    for author in authors_raw.split(';'):
        if len(author) < 3:
            continue
        if ',' in author:
            last, first = author.split(',')
            author_list.append(f"{first.strip()} {last.strip()}")
        else:
            author_list.append(author)
        if author_list[-1] == "Joseph Tighe":
            author_list[-1] = "<b>Joseph Tighe</b>"
    if len(author_list) > 1:
        authors = ', '.join(author_list[:-1])
        authors += ' and ' + author_list[-1]
        return authors
    elif len(author_list) == 1:
        return author_list[0]
    else:
        return ''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_dir = '/Users/tighej/website/jovapo.github.io'

    resumeDoc = []
    with open(os.path.join(base_dir, 'citations.csv'), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(spamreader):
            if i == 0:
                continue
            title = row[1]
            print(f'starting {title}')
            date = f"{row[4]}-{row[3]}"
            venue = row[2]
            authors = make_author_list(row[0])

            title_single = row[5]
            if len(title_single) < 2:
                title_single = title.split(' ')[0]
            if len(date) == 0 or len(authors) == 0 or len(title) == 0:
                continue
            venue2 = row[6]
            title2 = row[7]
            date2 = f"{row[9]}-{row[8]}"
            authors2 = make_author_list(row[10])
            if len(authors2) < 2:
                authors2 = authors
            out_str = make_file_contents(title, date, venue, authors, title_single, venue2, title2, date2, authors2)
            file_name = f"{date}-{venue.replace(' ','-')}-{title_single}"
            out_file = os.path.join(base_dir,'_publications',f'{file_name}.md')
            if os.path.isfile(out_file):
                print(f'Skipping {out_file}, already exists')
            else:
                print(out_str)
                with open(out_file,'w') as out_file:
                    out_file.write(out_str)

            resumeDoc.append(f'<p>{authors}, "<i>{title}</i>," {venue}, {date.split("-")[0]}</p>')
    print("\n".join(resumeDoc[::-1]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
