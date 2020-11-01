# Imports:
# use python --version to check what version of python your standard installation is
# if this is 2.x you will have to use pip3 install otherwise pip install
import csv
import requests
# pip install pillow
from PIL import Image
from io import BytesIO


# Define the ArtTate class, with all attributes that you find usefull
class ArtTate:
    # Define the initialise function accordingly
    def __init__(self, id, width, depth, height, imageUrl, artist, creditLine, year, acquisitionYear):
        self.id = id
        self.width = width
        self.depth = depth
        self.height = height
        self.imageUrl = imageUrl
        self.artist = artist
        self.creditLine = creditLine
        self.year = year
        self.acquisitionYear = acquisitionYear
        self.imagePath = ''

    # Define a function that prints a description
    def describe(self):
        print("artist:" + self.artist, "id:" + self.id, "width:" + str(self.width), "depth:" + str(self.depth), "height:" + str(self.height), "creditLine:"+str(self.creditLine), "year"+str(self.year), "acquisitionYear"+str(self.acquisitionYear))

    # implement the get image function that saves the image to the specified folder
    def getImageFile(self):
        if self.imageUrl:
            response = requests.get(self.imageUrl)
            try:
                im = Image.open(BytesIO(response.content))
            except OSError:
                return None
            path = "F:\\UCL 巴莱\\学习\\RC11\\软件学习\\Python\\Wanting-Ding_RC11_Python\\assignment1\\ArtImages\\TATE\\"+self.artist+"_"+self.id+".jpg"
            self.imagePath = path
            im.save(path, "JPEG")


artPieces = []
with open("F:\\UCL 巴莱\\学习\\RC11\\软件学习\\Python\\Wanting-Ding_RC11_Python\\assignment1\\CSVFiles\\artwork_data.csv", encoding='utf-8-sig')as artFile:
    artReader = csv.DictReader(artFile)

    for row in artReader:
        id = row['id']
        width = row['width']
        height = row['height']
        depth = row['depth']
        imageUrl = row['thumbnailUrl']
        artist = row['artist']
        creditLine = row['creditLine']
        year = row['year']
        acquisitionYear = row['acquisitionYear']

        if width or depth or height:
            artPiece = ArtTate(id, width, depth, height, imageUrl, artist, creditLine, year, acquisitionYear)
            artPieces.append(artPiece)

for art in artPieces:
    if "Presented" in art.creditLine:
        art.getImageFile()
