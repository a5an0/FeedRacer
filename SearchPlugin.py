class SearchPlugin:
    """ Abstract class for search plugins. Child classes should implement it's methods to implement the API. """

    def __init__(self):
        """ Create an instance of the searcher. """
        pass

    def searchForShow(self, showName, seasonNumber, episodeNumber):
        """ Search for a show. Results should be stored in some kind of internal data structure """
        pass

    def getResultList(self):
        """ Get a list of the search results. Each result should contain data about the results and a link to the nzb file """
        pass

    
