import requests

htmlfwd = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Headshot Sheet</title>
    <link rel="stylesheet" type="text/css" href="style.css" />
    <link href="https://fonts.googleapis.com/css?family=Poppins:400,600" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Work+Sans" rel="stylesheet">
</head>
<body>
    <div class="container">
      <header>
        <img src="headshot-sheet-logo.jpg" class="logo">
      </header>
      <main>
      """

htmlentryA = """<div class="entry">
          <img src="
          """
#insert image URL
htmlentryB = """" />
          <h2>"""
#insert search term
htmlentryC = """</h2>
          <img src="photo-icon.jpg" class="source" />
          <p class="sourcename">Google Image Search</p>
        </div>
        """
htmlpost = """</main>
      <footer>
        <img src="headshot-sheet-logo.jpg" class="logo">
      </footer>
    </div>
  </body>
</html>"""

headers = {
	'apikey': '9a5db880-f5d4-11e9-8cea-356e7808d493',
}

def generateHeadshotPage(names, outputFileName) :
    f = open((outputFileName + ".html"), "x")
    f.write(htmlfwd)
    for name in names:
        params = (
            ('q', name),
            ('location', 'United States'),
            ('search_engine', 'google.com'),
            ('gl', 'US'),
            ('hl', 'en'),
            ('num', '1'),
            ('tbm', 'isch')
        )
        response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
        imgurl = response.json()["image_results"][0]["sourceUrl"]
        f.write(htmlentryA + str(imgurl) + htmlentryB + str(name) + htmlentryC)
    f.write(htmlpost)
    f.close()

def main():
    filename = input("Enter your HTML Filename: ")
    namelist = []
    currentinput = ''
    while (currentinput != 'q' and currentinput != 'd'):
        currentinput = input("Enter a name to add to the Headshot Sheet (q=quit, d=done): ")
        if (currentinput != 'q' and currentinput != 'd'):
            namelist.append(currentinput)
    if currentinput == 'd':
        print("Generating Headshot Page for the following list:")
        print(namelist)
        generateHeadshotPage(namelist, filename)
        print("File Generated: " + filename + ".html")
    else:
        print("Cancelled.")

if __name__ == "__main__":
    main()


