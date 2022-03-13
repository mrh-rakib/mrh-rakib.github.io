AUTHOR = 'M Rakibul Hasan (Rakib)'
SITENAME = 'M Rakibul Hasan'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images','extras',]
EXTRA_PATH_METADATA = {
        'extra/favicon.ico': {'path': 'favicon.ico'},
}

TIMEZONE = 'Asia/Dhaka'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('e-mail','mailto:rakibul.hasan@bracu.ac.bd'),
        ('Faculty Profile','https://www.bracu.ac.bd/about/people/md-rakibul-hasan'),
        )


# Social widget
SOCIAL = (('GitHub','https://github.com/mrh-rakib'),
        ('LinkedIn','https://www.linkedin.com/in/rakibul-eeekuet/'),
        ('ORCiD','https://orcid.org/0000-0003-2565-5321'),
        ('ReserchGate','https://www.researchgate.net/profile/Md-Rakibul-Hasan-13'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'