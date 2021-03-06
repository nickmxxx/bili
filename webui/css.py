# (C) 2019-2020 lifegpc
# This file is part of bili.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from . import web, getEtag
from os.path import exists


class css:
    def GET(self, n):
        web.header('Content-Type', 'text/css; charset=utf-8')
        fn = f'webuihtml/css/{n}'
        if not exists(fn):
            fn = f'webuihtml/csso/{n}'
            if not exists(fn):
                web.HTTPError('404')
                return ''
        et = web.ctx.env.get('HTTP_IF_NONE_MATCH')
        et2 = getEtag(fn)
        if et == et2 and et2 is not None:
            web.HTTPError('304')
            t = ''
        else:
            web.header('Etag', et2)
            f = open(fn, 'r', encoding='utf8')
            t = f.read()
            f.close()
        return t
