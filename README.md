# Retrieval Augmented Generation from a Podcast

The goal of this project is to create a Retrieval Augmented Generation system using content from a podcast. This will involve downloading the audio files, using speach-to-text to generate a podcast transcript for each file, creating a vector store, and build the UI to support RAG-enabled LLM conversation to query the podcast content. 

So far, there is only one script which downloads the podcast .mp3 data using the download_audio.py script. Usage below. 

Usage: python download_audio.py <rss_feed_url> <output_folder>

Example: python download_audio.py https://feeds.acast.com/public/shows/secularbuddhism ./audio


## How to find the rss feed url (acast)
1. Find a podcast you like on their website (i.e., https://play.acast.com/)
2. Get the url (e.g., https://play.acast.com/s/mydadwroteaporno)
3. Edit the url, replacing 'play' with 'feeds' and '/s/' with '/public/shows/' (e.g., https://feeds.acast.com/public/shows/mydadwroteaporno)

