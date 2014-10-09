import os.path, time, datetime
import shutil
import glob
# os.chdir("/path/to/timelapse/renamed")
sortedNames = sorted(glob.glob("./*.jpg"))
idx = 0
for file in sortedNames:
  nicename = "%04d" % idx
  idx += 1
  shutil.move(file,nicename+".jpg")
