class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for page in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        for r in range(len(self.photos)):
            if len(self.photos[r]) < self.PHOTOS_PER_PAGE:
                self.photos[r].append(label)
                page_number = r + 1
                slot_counter = len(self.photos[r])
                return f'{label} photo added successfully on page {page_number} slot {slot_counter}'
        return 'No more free spots'

    def display(self):
        result = ''
        for row in self.photos:
            result += f'-----------\n'
            if len(row) > 0:
                result += f'{" ".join(["[]" for el in row])}\n'
            else:
                result += '\n'
        result += f'-----------\n'
        return result

'''
Create a class called PhotoAlbum. Upon initialization it should receive pages (int). 
It should also have one more attribute: photos (empty matrix). 
The amount of sub lists must be equal to the number of pages. The class should also have 3 more methods:
•	from_photos_count(photos_count: int) – creates a new instance of PhotoAlbum with pages ¼ of the photos count (each page can contain 4 photos)
•	add_photo(label:str) – add the photo in the next possible page and slot and return 
    "{label} photo added successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}". 
    If there are no free slots left, return "No more free spots"
•	display() – return a string representation of each page and the photos in it. 
    Each photo is marked with "[]" and the page separation is made using 11 dashes (-). For example, if we have 1 page and 2 photos:
-----------
[] []
-----------

and if we have 2 empty pages:
-----------

-----------

-----------

Note: Be aware that there is an empty line after the last page!
Output
baby photo added successfully on page 1 slot 1
first grade photo added successfully on page 1 slot 2
eight grade photo added successfully on page 1 slot 3
party with friends photo added successfully on page 1 slot 4
[['baby', 'first grade', 'eight grade', 'party with friends'], []]
prom photo added successfully on page 2 slot 1
wedding photo added successfully on page 2 slot 2
-----------
[] [] [] []
-----------
[] []
-----------

'''
album = PhotoAlbum(2)
print(album.photos)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
