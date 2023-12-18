import json

class ManimPlayer:
    
    data = {
        "play_key": " ",
        "pause": [],
        "loop": [],
        "keyframes": []
    }
    start_loop_t = None

    def pause(self, time):
        self.data["pause"].append(time)
    
    def start_loop(self, time):
        self.start_loop_t = time
    
    def end_loop(self, time):
        if self.start_loop_t is None or self.start_loop_t >= time:
            return

        self.data["loop"].append([self.start_loop_t, time])
        self.start_loop_t = None
    
    def add_loop(self, start_t, end_t):
        self.data["loop"].append(sorted([start_t, end_t]))
    
    def keyframe(self, time):
        self.data["keyframes"].append(time)

    def set_play_key(self, key):
        self.data["play_key"] = key

    def write_to_file(self, file):
        with open(file, "w+") as fd:
            json.dump(self.data, fd)