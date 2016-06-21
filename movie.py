from video import Video
import webbrowser

class Movie(Video):
    def __init__(self, title, storyline, image, trailer):
        Video.__init__(self, title, storyline, image)
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
