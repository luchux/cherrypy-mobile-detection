#is_mobile
#request: (cherrypie.request) and check the User-Agent, returns True if its a mobile, False otherwise.
import re

def is_mobile(request):
    ismobile = False

    if request.headers.has_key('User-Agent'):
        user_agent = request.headers['User-Agent']

        # Test common mobile values.
        patterns = "(xoom|up.browser|up.link|mmp|symbian|smartphone|phone|tablet|midp|wap|windows ce|pda|mobile|mini|palm|netfront|nokia)"

        patt_compiled = re.compile(patterns, re.IGNORECASE)
        match = patt_compiled.search(user_agent)

        if match:
           ismobile = True

    return ismobile

if __name__ == '__main__':
    #Lets test with cherrypy requests
    import cherrypy
    request = cherrypy.request

    #Emulating an Android browser
    request.headers = {'User-Agent': '[14/Jun/2013:13:07:54] "GET / HTTP/1.1" 200 12 "" "Mozilla/5.0 (Linux; U; Android 2.2; en-au; GT-I5510T Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"'}

    print is_mobile(request)