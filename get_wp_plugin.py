from webscrap import *

'''
https://realpython.com/python-web-scraping-practical-introduction/
https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
'''

if __name__ == '__main__':
    plugin_url = [
            { 
                "url":'https://wordpress.org/plugins/jetpack', 
                "ver":True 
            },
            { 
                "url":'https://wordpress.org/plugins/easy-video-player', 
                "ver":False 
            }
        ]


    for plugin_info in plugin_url:
        response = simple_get(plugin_info["url"])
        plugin_ver = None

        if response is not None:
            html = BeautifulSoup(response, 'html.parser')

            for i,l1 in enumerate(html.select('li')):
                if l1.text.strip().find("Version:") == 0:
                    plugin_ver = l1.text.strip().split()[1]
                    break

            if plugin_ver is not None:
                plugin_name = plugin_info["url"].rsplit('/', 1)[-1]
                if plugin_info["ver"] == True:
                    filename = '%s.%s.zip' %(plugin_name, plugin_ver)
                else:
                    filename = '%s.zip' %(plugin_name)

                download_file(plugin_info["url"], filename)
