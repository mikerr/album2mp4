import gdata.photos.service
import urllib
 
def main():
  "Downloads a Picasa Web Album of the user's choice to the current directory."
  gd_client = gdata.photos.service.PhotosService()
  username = raw_input("Username ")
  password = raw_input("Password ")
  gd_client.ClientLogin(username,password);
  print_album_names(gd_client, username) # Enumerate the albums owned by that account.
  album_id = raw_input("Album ID? ") # Prompt for an album ID.
  download_album(gd_client, username, album_id) # Download the corresponding album!
 
def print_album_names(gd_client, username):
  "Enumerates the albums owned by USERNAME."
  albums = gd_client.GetUserFeed(user = username)
  for album in albums.entry:
    print '%-30s (%3d photos) id = %s' % \
    (album.title.text, int(album.numphotos.text), album.gphoto_id.text)
 
def download_album(gd_client, username, album_id):
  "Downloads all the photos in the album ALBUM_ID owned by USERNAME."
  photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo'
  % (username, album_id))
  for photo in photos.entry:
    download_file(photo.content.src)
 
def download_file(url):
  "Download the data at URL to the current directory."
  basename = url[url.rindex('/') + 1:] # Figure out a good name for the downloaded file.
  print "Downloading %s" % (basename,)
  urllib.urlretrieve(url, basename)
 
if __name__ == '__main__':
  main()
