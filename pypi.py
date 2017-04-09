from errbot import botcmd, BotPlugin
from xmlrpc import client

class Pypi(BotPlugin):
    def __init__(self, bot):
        super(Pypi, self).__init__(bot)
        self.client = client.ServerProxy('https://pypi.python.org/pypi')

    @botcmd
    def searchpy(self, mess, args):
        responses = self.client.search({'name': args})
        formatted_answer = '\n'.join('%s-%s: %s' % (e['name'], e['version'], e['summary']) for e in responses)
        return formatted_answer

    @botcmd
    def dlpy(self, mess, args):
        """
        returns the nb of downloads of a package
        """
        args = args.strip()
        if not args:
            return "please give me a Pypi package name"

        total = 0
        response = '\n'
        for version in self.client.package_releases(args, True):
            for name, count in self.client.release_downloads(args, version):
                response += '%5i x %s\n' % (count, name)
                total += count
        return response + "\n%s has been downloaded %i times" % (args, total)
