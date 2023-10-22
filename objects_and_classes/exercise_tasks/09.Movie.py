class Movie:
    def __init__(self,name,director):
        self.name=name
        self.director=director
        self.watched=False
    __watched_movies=0
    def change_name(self,new_name):
        self.name=new_name
    def change_director(self,new_director):
        self.director=new_director
    def watch(self):
        if self.watched==False:
            self.watched=True
            self.__watched_movies+=1
    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {self.__watched_movies}"
