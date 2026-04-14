from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Vizitka(BoxLayout):
    pass


class VizitkaApp(App):
    def build(self):
        self.title = "Моя визитка"
        return Vizitka()


if __name__ == "__main__":
    VizitkaApp().run()
