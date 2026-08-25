class Browser:
    def __init__(self, name: str, version: float, current_url: str):
        self.name = name
        self.version = version
        self.current_url = current_url

    def display_info(self):
        return f"Browser: {self.name}, version: {self.version}, Current URL: {self.current_url}"

    def get_url(self, new_url: str):
        self.current_url = new_url
        return self.current_url


myBrowser = Browser("CNN", 2.22, "https://edition.cnn.com/")
print(myBrowser.name, "\n", myBrowser.current_url, "\n", myBrowser.version)
