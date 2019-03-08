import requests
import urllib
from PIL import Image
import os
import datetime

def fetchApod():
    print("This super sexy python script gets the NASA Astronomy Picture Of the Day...")
    print("Press Enter 3 times to get today...")
    day   = input("Enter day: ")
    month = input("Enter month: ")
    year  = input("Enter year: ")

    desiredDate = ""

    try:
        newDate = datetime.datetime(int(year),int(month),int(day))
        if newDate > datetime.datetime.now():
            print("Can't enter dates in the future dummy, try again.")
            return
        else:
            desiredDate = newDate.strftime('%Y-%m-%d')
    except ValueError:
        if (day == "") or (month == "") or (year == ""):
            pass
        else:
            print("Invalid date: " + day + "-" + month + "-" + year)
            print("Enter an actual date you dummy")
            return

    print(desiredDate)
    NASA_APOD_URL = "https://api.nasa.gov/planetary/apod?"
    if desiredDate != "":
        NASA_APOD_URL += "date=" + desiredDate + "&"
    NASA_APOD_URL += "api_key=DEMO_KEY"

    if desiredDate != "":
        print("Fetching photo from " + desiredDate + "...")
    else:
        print("Fetching photo from today...")

    try:
        r = requests.get(url = NASA_APOD_URL)
    except requests.exceptions.RequestException as e:
        print(e)
        return

    data = r.json()

    try:
        imgUrl = data['hdurl']
    except:
        imgUrl = data['url']

    filename = data['date'] + '_' + imgUrl.split("/")[-1]
    try:
        print("Copyright: " + data['copyright'])
    except:
        print("No Available Copyright Data")
    print("Explanation: ")
    print(data['explanation'])
    try:
        print("HD URL: " + data['hdurl'])
    except:
        print("URL: " + data['url'])

    print('Title: ' + data['title'])


    if not os.path.exists("apodImages"):
        os.mkdir("apodImages")
    #     print("Made apodImages")
    # else:
    #     print("apodImages already exists")
    try:
        urllib.request.urlretrieve(imgUrl,"apodImages/" + filename)
        imagy = Image.open("apodImages/" + filename)
        imagy.show()
    except:
        print("Sorry the URL is probably a YouTube video and not a picture. Here is the link:")

    print(imgUrl)

    # print(data)

def main():
    fetchApod()

if __name__ == '__main__':
    main()
