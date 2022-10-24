#JDU JSOM MAP MAKE BY Just gemer (SHARE AND LEAK Allowed)
import os 
print("JDU JSON MAP MAKER By Just gemer: ")
mapname = str(input("mapname: "))
lyriccolor = str(input("lyric color (HEX) without '#': "))
songcolor = str(input("song color (HEX) without '#': "))
coachcount = str(input("coach count: "))
artist = str(input("artist: "))
title = str(input("title: "))
length = str(input("map length: "))

# JSON Map Maker
jsonmap = open(mapname.lower() + ".json", "w", encoding="utf-8")
jsonmap.write('''{
  "artist": "''' + artist + '''",
  "assets": {
      "banner_bkgImageUrl": "https://cdn.glitch.me",
      "coach1ImageUrl": "https://cdn.glitch.me",
      "coach2ImageUrl": "https://cdn.glitch.me",
      "coach3ImageUrl": "https://cdn.glitch.me",
      "coach4ImageUrl": "https://cdn.glitch.me",
      "coverImageUrl": "https://cdn.glitch.me",
      "cover_1024ImageUrl": "https://cdn.glitch.me",
      "cover_smallImageUrl": "https://cdn.glitch.me",
      "expandBkgImageUrl": "https://cdn.glitch.me",
      "expandCoachImageUrl": "https://cdn.glitch.me",
      "phoneCoach1ImageUrl": "https://cdn.glitch.me",
      "phoneCoach2ImageUrl": "https://cdn.glitch.me",
      "phoneCoach3ImageUrl": "https://cdn.glitch.me",
      "phoneCoach4ImageUrl": "https://cdn.glitch.me",
      "phoneCoverImageUrl": "https://cdn.glitch.me",
      "videoPreviewVideoURL": "https://cdn.glitch.me"
  },
  "audioPreviewData": "",              
  "coachCount": ''' + coachcount + ''',
  "credits": "",
  "difficulty": 0,
  "doubleScoringType": -1,
  "jdmAttributes": [],
  "lyricsColor": "''' + lyriccolor + '''FF",
  "lyricsType": 0,
  "mainCoach": -1,
  "mapLength": ''' + length + ''',
  "mapName": "''' + mapname + '''",
  "mapPreviewMpd": "",
  "mode": 6,
  "originalJDVersion": 0,
  "packages": {
    "mapContent": "''' + mapname + '''_mapContent"
  },
  "parentMapName": "''' + mapname + '''",
  "skuIds": [],
  "songColors": {
    "songColor_1A": "''' + songcolor + '''FF",
    "songColor_1B": "''' + songcolor + '''FF",
    "songColor_2A": "''' + songcolor + '''FF",
    "songColor_2B": "''' + songcolor + '''FF"
  },
  "status": 3,
  "sweatDifficulty": 0,
  "tags": [
    "Main"
  ],
  "title": "''' + title + '''",
  "urls": {
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_AudioPreview.ogg": "https://cdn.glitch.me",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_HIGH.vp8.webm": "https://cdn.glitch.me",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_HIGH.vp9.webm": "https://cdn.glitch.me",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_LOW.vp8.webm": "https://cdn.glitch.me",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_LOW.vp9.webm": "https://cdn.glitch.me",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_MID.vp8.webm": "https://cdn.glitch.me",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_MID.vp9.webm": "https://cdn.glitch.me",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_ULTRA.vp8.webm": "https://cdn.glitch.me",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_ULTRA.vp9.webm": "https://cdn.glitch.me"
  },
  "serverChangelist": 455481,
  "skupackages": {
    "orbis": {
      "md5": "",
      "storageType": 0,
      "url": "https://cdn.glitch.me",
      "version": 0
    },
    "nx": {
      "md5": "",
      "storageType": 0,
      "url": "https://cdn.glitch.me",
      "version": 0
    },
    "pc": {
      "md5": "",
      "storageType": 0,
      "url": "https://cdn.glitch.me",
      "version": 0
    },
    "wiiu": {
      "md5": "",
      "storageType": 0,
      "url": "https://cdn.glitch.me",
      "version": 0
    }
  },
  "mapType": "jdu"

}''')
jsonmap.close()
