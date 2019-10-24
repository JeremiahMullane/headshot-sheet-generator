import requests

# DECLARE HTML BUILDING BLOCKS -------------------------------------------------------------------
# "htmlfwd" = Begining of final HTML document to be generated
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

# "htmlentryA", "htmlentryB", "htmlentryC" = These HTML blocks are combined with the search term
# and the returned image URL to generate HTML that displays each photo and it's label
htmlentryA = """<div class="entry">
          <img src="
          """
# insert image URL between A & B
htmlentryB = """" />
          <h2>"""
# insert search term between B & C
htmlentryC = """</h2>
          <img src="photo-icon.jpg" class="source" />
          <p class="sourcename">Google Image Search</p>
        </div>
        """

# "htmlpost" = End of final HTML document to be generated
htmlpost = """</main>
      <footer>
        <img src="headshot-sheet-logo.jpg" class="logo">
      </footer>
    </div>
  </body>
</html>"""
# HTML BUILDING BLOCKS COMPLETE --------------------------------------------------------------------

# Save Registered API Key for Zenserp Google Search API
headers = {
    'apikey': '9a5db880-f5d4-11e9-8cea-356e7808d493',
}

# Function that combines HTML blocks with API Search Results to write output HTML file
def generateHeadshotPage(names, outputFileName):
    f = open((outputFileName + ".html"), "x")
    f.write(htmlfwd)        # write first HTML code block to file
    for name in names:
        params = (              # declare Search API parameters
            ('q', name),        # set query term to name from names list
            ('location', 'United States'),
            ('search_engine', 'google.com'),
            ('gl', 'US'),
            ('hl', 'en'),
            ('num', '1'),       # only retrieve 1st result
            ('tbm', 'isch')     # search type "isch" refers to Google Image Search specifically
        )
        response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)    # API Query
        imgurl = response.json()["image_results"][0]["sourceUrl"]   # parse JSON for image URL
        f.write(htmlentryA + str(imgurl) + htmlentryB + str(name) + htmlentryC) # write HTML code block to display item
    f.write(htmlpost)   # write ending HTML code block to complete file
    f.close()

# Main function - retrieves input parameters from the console
def main():
    filename = input("Enter your HTML Filename: ")
    namelist = []
    currentinput = ''
    while currentinput != 'q' and currentinput != 'd':
        currentinput = input("Enter a name to add to the Headshot Sheet (q=quit, d=done): ")
        if currentinput != 'q' and currentinput != 'd':
            namelist.append(currentinput)
    if currentinput == 'd':
        print("Generating Headshot Page for the following list:")
        print(namelist)
        generateHeadshotPage(namelist, filename)
        print("File Generated: " + filename + ".html")
    else:
        print("Cancelled.")

# Run main function upon execution
if __name__ == "__main__":
    main()
