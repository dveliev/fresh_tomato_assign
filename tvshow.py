from video import Video

class TvShow(Video):
    def __init__(self, title, storyline, image):
        Video.__init__(self, title, storyline, image)
