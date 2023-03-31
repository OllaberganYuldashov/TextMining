import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('uz')
page_py = wiki_wiki.page('Aʼzam_Oʻktam')

print("Title: %s" % page_py.title)
# Page - Title: Python (programming language)

print("Summary: %s" % page_py.summary[0:60])
# Page - Summary: Python is a widely used high-level programming language for

print("text %s" % page_py.text)
print(page_py.links)
