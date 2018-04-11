from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import xml.etree.ElementTree

# Future: add checks to see which OS the user is running, and use
# the correct webdriver based on this. Shouldn't be too dificult.

print(sys.argv)
assert len(sys.argv >= 4)

# Extract fields from the command line
email = sys.argv[1]
password = sys.argv[2]
path_to_evernote_file = sys.argv[3]
path_to_chromedriver = "./chromedriver"

# If the user specifies their own chromedriver, use this instead
if len(sys.argv) > 4:
    path_to_chromedriver = sys.argv[4]


def login(email, password, driver):
    # Let the website load
    time.sleep(3)

    # Find the box to enter your email into,
    # enter it in, and press enter
    e = driver.find_element_by_xpath("//input[@type='email']")
    e.clear()
    e.send_keys(email)
    e.send_keys(Keys.RETURN)
    time.sleep(2)

    # Find the box to enter password into, enter
    # it in, and press enter
    e = driver.find_element_by_xpath("//input[@type='password']")
    e.send_keys(password)
    e.send_keys(Keys.RETURN)

    # Should be successfully logged in at this point

def take_note(title, content, driver):
    # Sleep a bit to let the website load
    time.sleep(.01)

    # Find the box to enter the note into
    note_box = driver.find_element_by_xpath("//div[@aria-label='Note' and @role='textbox' and not(@dir='ltr')]")
    note_box.send_keys(content)
    time.sleep(.01)

    # Find the box to enter the title into
    title_box = driver.find_element_by_xpath("//div[@aria-label='Title' and @role='textbox' and not(@dir='ltr')]")
    title_box.send_keys(title)
    time.sleep(.01)

    # Find the "Done" button, and click it
    done_box = driver.find_element_by_xpath("//div[contains(text(),'Done') and @role='button']")
    done_box.click()



def move_evernote_to_keep(path_to_evernote_file,email,password,driver):

    # Log into Google account
    login(email, password, driver)

    # Parse the xml tree of the given evernote xml file
    root = xml.etree.ElementTree.parse(path_to_evernote_file).getroot()

    # Go through each note in the tree
    for note in root.findall('note'):
        # Extract the title and content
        title = note.find('title')
        content = note.find('content')

        # Make a note in Google Keep with this content
        take_note(title, content, driver)



# Initialize the driver
driver = webdriver.Chrome(path_to_chromedriver)

# Go to Google Keep
driver.get("https://keep.google.com/u/0/")

# assert "Python" in driver.title

# Run the main function to move all notes to Google keep
move_evernote_to_keep(path_to_evernote_file,email,password,driver)

# Close the driver when done
driver.close()
