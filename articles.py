from tkinter import *
import webbrowser
import random

def articles():
    url =  [
            "https://www.gorillabins.ca/blog/how-to-manage-waste-properly/",
            "https://www.qld.gov.au/environment/pollution/management/waste/recovery/disposal-levy/business/manage-waste",
            "https://www.indiatoday.in/information/story/waste-disposal-and-management-all-you-need-to-know-1718288-2020-09-04",
            "https://www.conserve-energy-future.com/waste-management-and-waste-disposal-methods.php",
            "https://www.nature.org/en-us/about-us/where-we-work/united-states/delaware/stories-in-delaware/delaware-eight-ways-to-reduce-waste/",
            "https://www.ndtv.com/photos/news/waste-management-5-simple-ways-to-reduce-waste-at-home-24337"
            ]

    webbrowser.open(url[random.randint(0,len(url)-1)])
