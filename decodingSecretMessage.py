import requests
from bs4 import BeautifulSoup

def fetchDocContents(docLink):
    print("in fetchDocContents\n") #remove later

    response = requests.get(docLink)

    if response.status_code != 200:
        raise Exception("Could not fetch document")
    return requests.get(docLink)

def decodeMessage(docLink):
    print("in decodeMessage\n") #remove later

    content = fetchDocContents(docLink).text
    soup = BeautifulSoup(content) #fetch doc contents
    x = 0 #0 is an arbitrary default
    y = 0
    allData = [[]]

    #print("row 1 cell 1: ", soup.table.find("span").next, "\n")
    #print("row 1 cell 2", soup.table.tr.td.find_next_sibling().p.span.next, "\n")
    #print("row 2 cell 1", soup.table.tr.find_next_sibling().td.p.span.next, "\n")
    #print("row 2 cell 2", soup.table.tr.find_next_sibling().td.find_next_sibling().p.span.next, "\n")

    currentCell = soup.table.tr.find_next_sibling().td.p.span.next #row 2 col 1
    row = 2
    while currentCell != None:
        singleRowData = []
        x = int(currentCell)
        print("x: ", x, "\n")

        currentCell = soup.table.tr.find_next_sibling().td.find_next_sibling() #move to next col
        shape = str(currentCell.p.span.next)
        print("shape: ", shape, "\n")

        currentCell = currentCell.find_next_sibling() #move to next col
        y = int(currentCell.p.span.next)
        print("y: ", y, "\n")

        singleRowData.append(x)
        singleRowData.append(y)
        singleRowData.append(shape)

        allData.append(singleRowData)
        singleRowData.clear()

        #iterate to next row
        currentCell = soup.table.tr
        for i in range(row):
            currentCell = currentCell.find_next_sibling()
        currentCell = currentCell.td.p.span.next
        row += 1

    for x in allData:
        for y in allData:
            print(allData[x][y])

def main():
    print("in main\n") #remove later
    link = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    decodeMessage(link)

if __name__ == "__main__":
    main()
