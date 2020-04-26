class Sources:
    '''
    sources class to define sources  Objects
    '''

    def __init__(self,id,name,url,description,category,language,country):
        self.id =id
        self.name =name
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        self.description = description