# get_wp_plugin

Get the latest plugins for wordpress

Wordpress provides a easy way to install and update the plugins inside of the adminstrator dashboard.
But sometime, it is need to download the plugin directly.
If wordpress is running in the docker, ftp is not available and that make it difficult to update plugins 

## Install  

    $ python3 -m venv venv
    $ . ./venv/bin/activate

    $ pip3 install requests BeautifulSoup4

## Credits

Most of the web-scraping code is from http://realpython.com
https://realpython.com/python-web-scraping-practical-introduction/

