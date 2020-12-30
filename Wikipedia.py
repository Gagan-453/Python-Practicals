import wikipedia

def get_info(question, lang='en'):
    wikipedia.set_lang(lang)
    print(wikipedia.summary(question))

def search(q):
    print(wikipedia.search(q))

def get_page_info(question):
    ny = wikipedia.page(question)
    print(ny.title)
    print(ny.url)
    print(ny.content)
    print(ny.links[0])
    
question = 'Abstraction'
# get_info(question)
# search('Gagan')
get_page_info(question)
