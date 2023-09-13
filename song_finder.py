from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime as dtt
import os
import requests

# Customize with your own favorite artists
FAVORITE_ARTISTS = ["Miley Cyrus", "Lady Gaga", "Ava Max", "Anne-Marie", "Adam Lambert", "Cardi B", "Olivia Rodrigo"]

# Making them all lowercase to avoid mismatches
FAVORITE_ARTISTS = [artist.lower() for artist in FAVORITE_ARTISTS]

# Create a free account on https://www.infobip.com/ to get your own BASE_URL and API key
MSG_SENDER = "447860099299"  # Not sensitive
MSG_RECEIVER = os.environ.get("RECEIVER")  # Replace this with your phone number
BASE_URL = os.environ.get("BASE_URL")

headers = {
    "Authorization": f"App {os.environ['INFOBIP_API_KEY']}",
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# I made this so only it checks for new songs on fridays (weekday 4), which is when the playlist is updated.
# Feel free to choose any day between Monday (0) to Sunday (6) if you just want to test the code.
if dtt.datetime.today().weekday() == 4:
    # These chrome_options will do everything in the background, if you want to see the process comment the next 5 lines
    # and uncomment the 6th
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    driver.get("https://open.spotify.com/playlist/37i9dQZF1DX4JAvHpjipBk")
    actions = ActionChains(driver)

    wait = WebDriverWait(driver, timeout=10)
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".main-view-container")))
    time.sleep(5)
    song_dict = {}

    # I am adding items to the dictionary multiple times because it seems that songs are "erased" from
    # memory as the browser window scrolls, so by adding them on every iteration I make sure that no song is skipped,
    # but I avoid duplicates since there can't be repeated keys inside the dictionary.
    # The order of songs does change, but it doesn't matter for this script's purpose.

    for i in range(120):
        actions.send_keys(Keys.DOWN)
        actions.perform()
        time.sleep(0.2)
        artist_names = driver.find_elements(By.CSS_SELECTOR,
                                            ".Type__TypeElement-sc-goli3j-0.bDHxRN.rq2VQ5mb9SDAFWbBIUIn.standalone-ellipsis-one-line")
        song_names = driver.find_elements(By.CSS_SELECTOR,
                                          '.Type__TypeElement-sc-goli3j-0.fZDcWX.t_yrXoUO3qGsJS4Y6iXX.standalone-ellipsis-one-line')
        song_links = driver.find_elements(By.CSS_SELECTOR,
                                          'a[data-testid="internal-track-link"]')

        for artist, song, link in zip(artist_names, song_names, song_links):
            song_dict[link.get_attribute("href")] = (artist.text.lower(), song.text)

    matches = {}
    for song in song_dict:
        artists_in_song = song_dict[song][0].split(', ')
        for artist in artists_in_song:
            if artist in FAVORITE_ARTISTS:
                matches[song] = (song_dict[song][0], song_dict[song][1])

    final_match_list = []
    for match in matches:
        final_match_list.append(f'{matches[match][1]} by {str(matches[match][0]).title()}: {match}')
        # Converted artist name back to title case                              ^^^^^^^^
    match_strings = "\n\n".join(final_match_list)

    # After getting the final list of songs, send them to your Whatsapp:
    message_id = 1
    params = {
        "from": MSG_SENDER,
        "to": MSG_RECEIVER,
        "messageId": message_id,
        "content": {
            "text": f'You might want to listen to these new songs:\n\n{match_strings}',
        },
        "previewUrl": False
    }
    response = requests.post(BASE_URL + "/whatsapp/1/message/text", json=params, headers=headers)
    print(response.json())
    driver.quit()
