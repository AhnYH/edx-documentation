# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

tags.add('Open_edX')
set_audience(OPENEDX, COURSE_TEAMS)

product = 'Open_edX'

def setup(app):
    app.add_config_value('product', '', True)

#project = u'K-MOOC'
project = u'K-MOOC 강좌 개발 및 운영 매뉴얼'
