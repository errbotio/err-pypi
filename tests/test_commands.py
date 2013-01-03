import logging
from errbot.backends.test import FullStackTest, pushMessage, popMessage
from os.path import abspath, sep
pluginpath = sep.join(abspath(__file__).split(sep)[:-2])
import config

class TestCommands(FullStackTest):

    @classmethod
    def setUpClass(cls):
        config.BOT_EXTRA_PLUGIN_DIR = pluginpath
        super().setUpClass()

    def test_searchpy_command(self):
        pushMessage('!searchpy err')
        response = popMessage()
        logging.debug(response)
        self.assertIn('err is a plugin based XMPP chatbot designed to be easily deployable, extensible and maintainable.', response)