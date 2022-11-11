import copy


class UrlCreator(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __getattr__(self, item):
        kwa = copy.deepcopy(self.kwargs)
        kwa['path'] = [*self.kwargs.get('path', []), item]
        return UrlCreator(**kwa)

    def _create(self):
        print(self.kwargs)
        return UrlCreator(**self.kwargs)

    def __call__(self, *args, **kwargs):
        self.kwargs['path'] = [*self.kwargs.get('path', []), *args]
        self.kwargs['query'] = {**self.kwargs.get('query', {})}
        self.kwargs['query'].update(kwargs)
        return self

    def __str__(self):
        return str(self._create().kwargs)

    def __eq__(self, other):
        elf = str(self)

        other = str(other)
        diction = {}
        protocol, smth_other = other.split('://')

        diction['scheme'] = protocol
        # print(diction)
        # print(smth_other,22)
        # name, out = smth_other.split('/',1)
        try:
            name, out = smth_other.split('/', 1)
        except ValueError:
            diction['authority'] = smth_other

        else:
            diction['authority'] = name

            if len(out) > 0:
                try:
                    prepath, query = out.split('?')
                except ValueError:
                    path_last = out.split('/')
                    diction['path'] = path_last

                else:

                    path = prepath.split('/')
                    diction['path'] = path

                    last = query.split('&')
                    lstd = {x.split('=')[0]: x.split('=')[1] for x in last}

                    diction['query'] = lstd
        other = str(diction)
        # print(other)

        if elf == other:
            return True
        else:
            return False


#
url_creator = UrlCreator(scheme='https', authority='docs.python.org')

assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'     #+++++++++++++++
assert url_creator('api','v1','list') == 'https://docs.python.org/api/v1/list'
# assert url_creator('api','v1','list', q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'  #+++++++++

# assert url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create()  \
#        == 'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default'