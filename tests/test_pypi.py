from errbot.backends.test import FullStackTest, pushMessage, popMessage


class TestCommands(FullStackTest):

    def test_searchpy(self):
        self.assertCommand('!searchpy Werkzeug', 'The Swiss Army knife of Python web development')
