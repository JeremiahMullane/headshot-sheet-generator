# headshot-sheet-generator
A program that generates a "yearbook photos" style HTML page displaying the first google image search result for a list of search terms.
Uses the Zenserp Custom Google Search API (queries limited to 50/month)

Input is handled via the console for now.
First enter the desired filename of the HTML output, then enter search terms one at a time (d when done, q to quit and cancel.)

The resultant HTML file will be linked to the included CSS stylesheet, which references the two logo jpegs included in the project.

I use this to generate a headshot sheet for lists of actors, but it can be used to generate a sheet with photos of any search term.
Since it only uses the URL of the first image search result, accuracy is limited to how lucky you are with Google's search algorithm.

This program uses the SERP API by Zenserp. More info at: https://app.zenserp.com/
The initial version of this program uses a free trial API key that I have registered, and is limited to 50 queries per month.
Program will cease to function if number of queries is exceeded.
For educational/demonstration purposes only. Not for commercial use.
