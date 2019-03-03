from tkinter import *
from tkinter import ttk
import requests
import sys
import webbrowser
import bs4


def openTabs(*args):
    
# print (webbrowser._browsers)
#     firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
#     webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
#     webbrowser.get('firefox')
#     print (webbrowser._browsers)
    
    
    URL = str(searchQuery.get())

    res = requests.get('http://google.com/search?q=' + URL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    linkElems = soup.select('.r a')

    n_links = int(N_link.get())

    numOpen = min(n_links, len(linkElems))

    webbrowser.open_new('http://google.com/search?q=' + URL)
    for i in range(numOpen):
        webbrowser.open_new_tab('http://google.com' + linkElems[i].get('href'))
    
    msg['text'] = "Top "+ str(numOpen) + " url opened."

    
    

def change(*args):
    N_link.get()
    
    
    
    
    
if __name__ == '__main__': 
    
    root = Tk()
    root.title("N Tab Opener")

    mainframe = ttk.Frame(root, padding="12 12 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.attributes("-topmost", True)
    
    
    searchQuery = StringVar(root)
    
    ttk.Label(mainframe, text="Enter search text").grid(
        row=1, column=1)
    
    searchQueryTextBox = ttk.Entry(mainframe, width=40, textvariable=searchQuery)
    searchQueryTextBox.grid(column=1, row=2, sticky=W)

    ttk.Button(mainframe, text="Search", command=openTabs).grid(
        column=4, row=2, sticky=W)


    # Create a Tkinter variable
    N_link = IntVar(root)

    # Dictionary with options
    choices = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7'}
    N_link.set(list(choices.values())[1])  # set the default option

    # Option menu
    popupMenu = OptionMenu(mainframe, N_link, *list(choices.values()))
    ttk.Label(mainframe, text="Choose Tab Count").grid(row=1, column=3)
    popupMenu.grid(row=2, column=3)

    # link function to change dropdown
    N_link.trace('w',change)
    
    msg = ttk.Label(mainframe, text='')
    msg.grid(row=3, columnspan=3, sticky=W )
    
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    
    searchQueryTextBox.focus()
    
    root.bind('<Return>', openTabs)

    root.mainloop()



