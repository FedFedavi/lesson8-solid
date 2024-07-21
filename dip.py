# class Book():
#     def read(self):
#         print("Чтение интересной истории")
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()


from abc import ABC, abstractmethod

class StorySources(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySources):
    def get_story(self):
        print("Чтение интересной истории")

class AudioBook(StorySources):
    def get_story(self):
        print("Чтение интересной истории вслух")

class StoryReader():
    def __init__(self, story_source: StorySources):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

book = Book()
audioBook = AudioBook()

readerBook = StoryReader(book)
reader_audioBook = StoryReader(audioBook)

readerBook.tell_story()
reader_audioBook.tell_story()