#JDU JSOM MAP MAKE BY Just gemer (SHARE AND LEAK Allowed)
import os 
print("JDU JSON MAP MAKER By Just gemer: ")
mapname = str(input("mapname: "))
lyriccolor = str(input("lyric color without '#': "))
songcolor = str(input("song color without '#': "))
coachcount = str(input("coach count: "))
artist = str(input("artist: "))

# JSON Map Maker
jsonmap = open(mapname.lower() + ".json", "w", encoding="utf-8")
jsonmap.write('''{
  "artist": "''' + artist + '''",
  "assets": {
    "default": {
      "banner_bkgImageUrl": "",
      "coach1ImageUrl": "",
      "coach2ImageUrl": "",
      "coach3ImageUrl": "",
      "coach4ImageUrl": "",
      "coverImageUrl": "",
      "cover_1024ImageUrl": "",
      "cover_smallImageUrl": "",
      "expandBkgImageUrl": "",
      "expandCoachImageUrl": "",
      "phoneCoach1ImageUrl": "",
      "phoneCoach2ImageUrl": "",
      "phoneCoach3ImageUrl": "",
      "phoneCoach4ImageUrl": "",
      "phoneCoverImageUrl": "",
      "videoPreviewVideoURL": ""
    },
    "nx": {
      "banner_bkgImageUrl": "",
      "coach1ImageUrl": "",
      "coach2ImageUrl": "",
      "coverImageUrl": "",
      "cover_1024ImageUrl": "",
      "cover_smallImageUrl": "",
      "expandBkgImageUrl": "",
      "expandCoachImageUrl": "",
      "phoneCoach1ImageUrl": "",
      "phoneCoach2ImageUrl": "",
      "phoneCoverImageUrl": "",
      "videoPreviewVideoURL": "",
      "map_bkgImageUrl": ""
    },
    "wiiu": {
      "banner_bkgImageUrl": "",
      "coach1ImageUrl": "",
      "coverImageUrl": "",
      "cover_1024ImageUrl": "",
      "cover_smallImageUrl": "",
      "expandBkgImageUrl": "",
      "expandCoachImageUrl": "",
      "phoneCoach1ImageUrl": "",
      "phoneCoverImageUrl": "",
      "videoPreviewVideoURL": ""
    }
  },
  "audioPreviewData": "",              
  "coachCount": ''' + coachcount + ''',
  "credits": "",
  "difficulty": 1,
  "doubleScoringType": -1,
  "jdmAttributes": [],
  "lyricsColor": "''' + lyriccolor + '''FF",
  "lyricsType": 0,
  "mainCoach": -1,
  "mapLength": ,
  "mapName": "''' + mapname + '''",
  "mapPreviewMpd": "",
  "mode": 6,
  "originalJDVersion": ,
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
  "sweatDifficulty": 1,
  "tags": [
    "Main"
  ],
  "title": "",
  "urls": {
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_AudioPreview.ogg": "",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_HIGH.vp8.webm": "",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_HIGH.vp9.webm": "",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_LOW.vp8.webm": "",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_LOW.vp9.webm": "",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_MID.vp8.webm": "",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_MID.vp9.webm": "",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_ULTRA.vp8.webm": "",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MapPreviewNoSoundCrop_ULTRA.vp9.webm": ""
  },
  "serverChangelist": 455481,
  "skupackages": {
    "orbis": {
      "md5": "",
      "storageType": 0,
      "url": "",
      "version": 0
    },
    "nx": {
      "md5": "",
      "storageType": 0,
      "url": "",
      "version": 0
    },
    "pc": {
      "md5": "",
      "storageType": 0,
      "url": "",
      "version": 0
    },
    "wiiu": {
      "md5": "",
      "storageType": 0,
      "url": "",
      "version": 0
    }
  },
  "mapType": "jdu"

  }''')
jsonmap.close()
