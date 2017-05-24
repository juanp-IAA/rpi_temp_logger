#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys




# print the HTTP header
def printHTTPheader():
    print "Content-type: text/html\n\n"



# print the HTML head section
# arguments are the page title and the table for the chart
def printHTMLHead(title):
    print "<head>"
    print "    <title>"
    print title
    print "    </title>"
    

    print "</head>"




# print the div that contains the graph
def show_title_1():
    print "<h2>GPIO status</h2>"



# connect to the db and show some stats
# argument option is the number of hours
def show_stats(option):


    print "<hr>"

    print "<h2>El estado actual de los pines es: </h2>"
	
	
	#### Rellenar para saber el estado de los pines que controlan los led y el pulsador

    print "<hr>"







# main function
# This is where the program starts 
def main():


    # print the HTTP header
    printHTTPheader()


    # start printing the page
    print "<html>"
    # print the head section including the table
    # used by the javascript for the chart
    printHTMLHead("Raspberry Pi Monitor & Control")

    # print the page body
    print "<body>"
    print "<h1>Raspberry Pi Monitor & Control</h1>"
    print "<hr>"
    show_title_1()
    show_stats(option)
    print "</body>"
    print "</html>"

    sys.stdout.flush()

if __name__=="__main__":
    main()



