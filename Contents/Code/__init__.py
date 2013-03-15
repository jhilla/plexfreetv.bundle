import re
NAME = "plexPTV"

##
def Start():
	ObjectContainer.title1 = NAME
	HTTP.CacheTime = CACHE_1HOUR
	HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:19.0) Gecko/20100101 Firefox/19.0'
	HTTP.Headers['X-Requested-With'] = 'XMLHttpRequest'
##
@handler('/video/plexPTV', NAME)
def MainMenu():

	oc = ObjectContainer()
	html = HTTP.Request("http://www.free-tv-video-online.me/internet/the_walking_dead/")
	match = re.compile('class="mnlcategorylist"><a href="(.+?)"><b>(.+?)[ (]*([0-9]{0,4})[)]*</b></a>(.+?)<').findall(html.content)

	for urllink, category, number, meta in match:
		title = category + " " + number
		description = "test"
		link = urllink
		print title
		oc.add(DirectoryObject(
			key = Callback(Season, title=title),
			title = title,
		))
	return oc