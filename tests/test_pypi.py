from errbot.backends.test import FullStackTest, pushMessage, popMessage


class TestCommands(FullStackTest):

    def test_searchpy(self):
        self.assertCommand('!searchpy err', 'err is a plugin based XMPP chatbot designed to be easily deployable, extensible and maintainable.')
