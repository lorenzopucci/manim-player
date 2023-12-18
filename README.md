# Manim player

A tool for presenting any video file like a PowerPoint, specifically designed for
animations made with [Manim](https://github.com/ManimCommunity/manim).

This program lets you configure the video to automatically pause or loop at certain
timestamps and navigate through selected timestamps with your keyboard.

## The player

All you need to play a video is a browser, the mp4 video file, a json configuration
file (like `config.json`) and `manimPlayer.html`. Then you can just open the html
file, select the video and config file and play it.

- The spacebar (or any other key set in the config file) will play/pause the video;
- The left/right arrow keys will jump to the nearest timestamp;
- The up/down arrows will enable/disable the video player's commands;
- If the video is looping, pressing the right arrow will quit the loop;

## The Python utility

`manimPlayer.py` is a script that makes it easier to generate the config file.
You can just import it and use it along with the Manim code for the animation:

```py
from manim import *
import manimPlayer

class SomeAnimation(Scene):

  def construct(self):
    player = manimPlayer.ManimPlayer()
  
    # ...
  
    self.play(Something())
    player.pause(self.renderer.time)
  
    # ...
  
    player.start_loop(self.renderer.time)
    self.play(Something())
    player.end_loop(self.renderer.time)
  
    # ...
  
    player.write_to_file("config.json")
  
```
