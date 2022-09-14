# Video-Processing using moviepy python library
MoviePy is a Python module for editing videos. It can cut and arrange clips, add video effects, and edit audio. It can work like a toolbox, if you only make changes to one clip. If you have to edit lots of clips, MoviePy can automate that process.

## Installing
### Install MoviePy
**Method with pip:** if you have pip installed, just type this in a terminal 
```pip install moviepy```

## Basic editing
The key objects in ```MoviePy``` are ```VideoClips```.
```
from moviepy.editor import *
clip = VideoFileClip("sample-mp4-file.mp4")
```
The module ```moviepy.editor``` contains the objects and methods we’re using. clip is a new VideoFileClip object, initialized with the name (or filepath) of the video file at hand.

##### Trimming video using ```subclip``` method.
```
trim = VideoFileClip("video path").subclip(15, 25)
```
##### Concatenate video clips using ```concatenate_videoclips``` method.
Put these clips together in a list, and chain them together with ```concatenate_videoclips```. Concatenate means “link together”, as we edit the clips into one video.
```
final_clip = concatenate_videoclips([clip, clip2, clip3, clip4])
```
Finally, to get our finished video, we use the ```write_videofile``` method on ```final_clip```. Your final code should look like the code below.
```
from moviepy.editor import *
# clip is the video from 00:56 to 01:06
clip = VideoFileClip("sample-mp4-file.mp4").subclip(56, 66)
clip2 = VideoFileClip("sample-mp4-file.mp4").subclip(70, 76)
clip3 = VideoFileClip("sample-mp4-file.mp4").subclip(50, 52)
clip4 = VideoFileClip("sample-mp4-file.mp4").subclip(30, 35)
final_clip = concatenate_videoclips([clip, clip2, clip3, clip4])
final_clip.write_videofile("output_1.mp4")
```
### Adding Video effects
MoviePy can do more than just cut and rearrange video. The module ```moviepy.editor``` also contains submodules. ```vfx``` holds video effects, and ```afx``` holds audio effects.
To add any effect to a clip, you use the ```fx``` method on the clip, and pass in the effect and any parameters. For convenience, put the entire VideoFileClip in parentheses (). For many effects, put each ```.fx``` call on a new line.
```
clip = (VideoFileClip("sample-mp4-file.mp4").subclip(56, 66)
    .fx(vfx.colorx, 0.7))

# you can also do this with clip_edited = clip.fx(vfx.colorx, 0.7)
```
Our clip is getting called with .fx( vfx.colorx, 1.2). MoviePy reads this as “apply the vfx.colorx effect and with the parameter of 1.2”.
##### Brightness and Contrast
```
clip = (VideoFileClip("sample-mp4-file.mp4").subclip(56, 66)
        .fx(vfx.colorx, 1.2)  # 20% brighter
        .fx(vfx.lum_contrast, 0, 40, 127))  # and increase the contrast
```
### Audio effects
AudioClips in MoviePy work much the same as VideoClips. We create a new AudioFileClip in the same way we created a VideoFileClip.
```
musicclip = AudioFileClip("audio file path").subclip(0, 6)
```
Audio clips can also come from the audio of a video clip. Let’s extract the audio from our first video clip, so we can use the sound on its own:
```
clip = VideoFileClip("sample-mp4-file.mp4")
audioclip = clip.audio
```
MoviePy has plenty of audio effects, and you can stack them like the video effects.
Audio effects are in the ```afx``` submodule:
```
audioclip = (clip.audio).afx(afx.volumex, 1.2).afx(afx.audio_fadein, 1.0)
# Make the sound 20% louder, and fade it in over 1 second
```
The set_audio function replaces a video clip’s audio with a new audio clip. We use this to create a new version of the first clip in our video.
```
musicclip = AudioFileClip("audio file path").subclip(0, 6)
audioclip = (clip.audio).fx(afx.volumex, 1.2).fx(afx.audio_fadein, 1.0)
# Make the sound 20% louder, and fade it in over 1 second
clip_v2 = clip.set_audio(audioclip)  # new first clip

final_clip = concatenate_videoclips([clip_v2, clip2, clip3, clip4])
final_clip.write_videofile("output_3.mp4")
```

### Putting it all together
```
musicclip = AudioFileClip("Study and Relax.mp3").subclip(0, 6)
audioclip = (clip.audio).fx(afx.volumex, 1.2).fx(afx.audio_fadein, 1.0)
# Make the sound 20% louder, and fade it in over 1 second
clip_v2 = clip.set_audio(audioclip)  # new first clip

composite_start_of_video = CompositeVideoClip([clip_v2,
                                               clip4.fx(vfx.resize, 0.6).fx(afx.volumex, 0.0)])
# clip4 is smaller (60% original size), and on top of clip_v2

clip2_audio = (clip2.audio).fx(afx.volumex, 1.5)  # 50% louder, so we can hear over our music
composite_second_clip_audio = CompositeAudioClip([clip2_audio,
                                                  (musicclip).fx(afx.volumex, 0.3)])  # 70% quieter
clip2_v2 = clip2.set_audio(composite_second_clip_audio)

final_clip = concatenate_videoclips([composite_start_of_video, clip2_v2, clip3, clip4])

final_clip.write_videofile("output_4.mp4")
```

### Conclusion
Good job! You’ve just edited and remixed a video, all in a Python program. There are plenty of other things you can do with MoviePy, now that you know the basics.
