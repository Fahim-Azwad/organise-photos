#This is the code to organize files in the attached directory "Photos".
#This will rearrange the files in the same folder, by making directories
#with the names of the places in the files name
import os

#Makes directory for places
def make_place_directories(places):
    for place in places:
        os.mkdir(place)

#Splits file names into parts and takes only the name of places
def extract_place(filename):
    return filename.split('_')[1]

#Organizes the photos
def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        #Extracts names of places from the places list
        place = extract_place(filename)
        if place not in places:
            places.append(place)
    #Calls for the make directory function
    make_place_directories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))

#Checks to see of the function is called as main
if __name__ == '__main__':
    organize_photos("Photos")
