from tiny_url import Tiny,Get


url = "https://www.google.com"

m = Tiny.make_url(url)

o = Get.get_original('q93in5fshoo')

t = Get.get_tiny('https://example.com')

print(m,o,t)