# 🎵 Song Finder Bot 🕵️‍♂️

## Discover New Music Hassle-Free! 📱🎶

### About
The **Song Finder Bot** is a Python automation script designed to keep you updated on your favorite artists' latest releases. Dive into the world of automation and explore the script's exciting functionalities.

---

## Key Features 🌟

### 1. Web Scraping Magic
This script effortlessly retrieves real-time data from Spotify's New Releases playlist, thanks to some nifty web scraping:

- **Selenium Wizardry**: Uses Selenium for web automation to navigate and extract data from the Spotify web interface.
  
- **Dynamic Scrolling**: Implements dynamic scrolling to load an extensive list of songs without missing a beat.

- **Element Juggling**: Interacts with web elements smoothly, including clicks, waits, and keyboard inputs.

### 2. Data Magic
The script processes and filters the scraped data:

- **Data Organization**: Stores and manipulates song information using dictionaries and lists.

- **Data Precision**: Ensures data accuracy by converting artist names to lowercase and handling multiple artists per track.

- **Time Precision**: Runs the script exclusively on Fridays, aligning with Spotify's playlist updates.

### 3. API Magic
This project integrates seamlessly with Infobip's WhatsApp API for efficient message delivery:

- **API Usage**: Involves making HTTP requests and sending POST requests with JSON data. You can find more information on Infobip's Whatsapp API here: https://www.infobip.com/docs/api/channels/whatsapp.

- **Secure Connections**: Safely handles API authorization with secure token management.

### 4. Task Automation Magic
Experience the convenience of task automation:

- **Scheduled Delights**: You can set up daily execution with PythonAnywhere. You'll need a paid account since Infobip's API isn't whitelisted on free accounts. Otherwise, you could manually run it or use a tool like Windows Task Scheduler or similar.

### 5. Error Magic
The script features robust error handling to ensure smooth, reliable operation.

---

## Getting Started 🚀

1. Clone this repository.

2. Personalize the `FAVORITE_ARTISTS` list with your beloved musical talents.

3. Configure environment variables for Infobip's API and your WhatsApp number.

4. Schedule daily script execution using PythonAnywhere or a similar tool.

---

## Connect with Me on LinkedIn 👋

If you're intrigued by this project or simply want to connect, you can find me on LinkedIn: [Victor Martino](https://www.linkedin.com/in/victor-martino-446765140/)

---

**Experience the magic of automated song discovery with Song Finder Bot! Enjoy the music, and never miss a beat again. 🎧🤖**

