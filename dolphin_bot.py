import logging

import op_dolphin_bot.dolphin_bot as dolphin
from op_dolphin_bot.constants import PROGRAM_NAME, PROGRAM_VERSION

# CONFIGURATION START
# ---

# Get the URL from Slack's "Incoming WebHooks" Integration:
SLACK_INCOMING_HOOK_URL = ""

# The base URL:
OP_BASE_URL = ""

# The ID of the project which activities are tracked. Use util/op_project_list.py if you aren't sure:
OP_PROJECT_ID = 2

# Your RSS API Key. See "Account Settings -> Tokens" in Open Project.
OP_RSS_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Specify elements you want to track. Recognizes everything except "cost_objects" and "time_entries":
OP_RSS_FILTER = ('work_packages', 'wiki_edits', 'news', 'documents', 'meetings')

# ---
# CONFIGURATION END


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
logging.info("Started %s. Current version: %s", PROGRAM_NAME, PROGRAM_VERSION)

bot = dolphin.DolphinBot(SLACK_INCOMING_HOOK_URL, OP_BASE_URL, OP_PROJECT_ID, OP_RSS_KEY, OP_RSS_FILTER,
                         check_sleep=120, max_links=10)
bot.run()
