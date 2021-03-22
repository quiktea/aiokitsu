
class Anime():
    def __init__(self, raw_payload : dict):
        self.__payload = raw_payload
        self.__attrs = self.__payload.get("attributes")

    def __str__(self):
        return self.__payload.get("attributes").get("canonicalTitle")

    
    @property
    def title(self):
        return self.__payload.get("attributes").get("canonicalTitle")
    
    @property
    def id(self):
        return self.__payload.get("id")

    @property
    def type(self):
        return self.__payload.get("type")

    @property
    def ageRating(self):
        return self.__attrs.get("ageRating")

    @property
    def createdAt(self):
        return self.__attrs.get("createdAt")

    @property
    def updatedAt(self):
        return self.__attrs.get("updatedAt")

    @property
    def synopsis(self):
        return self.__attrs.get("synopsis")

    @property
    def slug(self):
        return self.__attrs.get("slug")

    @property
    def title_en(self):
        return self.__attrs.get("titles").get("en")

    @property
    def title_en_jp(self):
        return self.__attrs.get("titles").get("en_jp")

    @property
    def title_jp(self):
        return self.__attrs.get("titles").get("ja_jp")

    @property
    def averageRating(self):
        return self.__attrs.get("averageRating")

    @property
    def abbreviatedTitles(self):
        return self.__attrs.get("abbreviatedTitles")
    
    @property
    def ratingFrequencies(self):
        return self.__attrs.get("ratingFrequencies")

    @property
    def userCount(self):
        return self.__attrs.get("userCount")

    @property
    def favoritesCount(self):
        return self.__attrs.get("favoritesCount")

    @property
    def startDate(self):
        return self.__attrs.get("startDate")

    @property
    def endDate(self):
        return self.__attrs.get("endDate")
    
    @property
    def popularityRank(self):
        return self.__attrs.get("popularityRank")
    
    @property
    def ratingRank(self):
        return self.__attrs.get("ratingRank")

    @property
    def ageRating(self):
        return self.__attrs.get("ageRating")

    @property
    def ageRatingGuide(self):
        return self.__attrs.get("ageRatingGuide")

    @property
    def subtype(self):
        return self.__attrs.get("subtype")

    @property
    def status(self):
        return self.__attrs.get("status")

    @property
    def tba(self):
        return self.__attrs.get("tba")
    
    @property
    def posterImage(self):
        return self.__attrs.get("posterImage")

    @property
    def coverImage(self):
        return self.__attrs.get("coverImage")

    @property
    def episodeCount(self):
        return self.__attrs.get("episodeCount")

    @property
    def episodeLength(self):
        return self.__attrs.get("episodeLength")

    @property
    def youtubeVideoId(self):
        return self.__attrs.get("youtubeVideoId")

    @property
    def showType(self):
        return self.__attrs.get("showType")

    @property
    def nsfw(self):
        return self.__attrs.get("nsfw")
    
    @property
    def relationships(self):
        return self.__attrs.get("relationships")
    
    @property
    def categories(self):
        return self.__attrs.get("categories")

    @property
    def castings(self):
        return self.__attrs.get("castings")

    @property
    def installments(self):
        return self.__attrs.get("installments")
    
    @property
    def mappings(self):
        return self.__attrs.get("mappings")

    @property
    def reviews(self):
        return self.__attrs.get("reviews")

    @property
    def mediaRelationships(self):
        return self.__attrs.get("mediaRelationships")

    @property
    def episodes(self):
        return self.__attrs.get("episodes")

    @property
    def streamingLinks(self):
        return self.__attrs.get("streamingLinks")

    @property
    def animeProductions(self):
        return self.__attrs.get("animeProductions")

    @property
    def animeCharacters(self):
        return self.__attrs.get("animeCharacters")

    @property
    def animeStaff(self):
        return self.__attrs.get("animeStaff")

    @property
    def meta(self):
        return self.__attrs.get("meta")

    @property
    def links(self):
        return self.__attrs.get("links")
        



    



    

