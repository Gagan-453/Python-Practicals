from urlextract import URLExtract

extractor = URLExtract()
urls = extractor.find_urls("meet.google.com Hi")
print(urls) 