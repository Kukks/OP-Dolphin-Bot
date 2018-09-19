import logging

import op_dolphin_bot.dolphin_bot as dolphin
from op_dolphin_bot.constants import PROGRAM_NAME, PROGRAM_VERSION

# CONFIGURATION START
# ---
# Copy and paste the URL from Slack's "Incoming WebHooks" Integration:
SLACK_INCOMING_HOOK_URL = os.environ.get('SLACK_INCOMING_HOOK_URL')

# Your base URL:
OP_BASE_URL = os.environ.get('OP_BASE_URL')

# The ID of the project which activities are tracked. Use util/op_project_list.py if you aren't sure:
OP_PROJECT_ID = os.environ.get('OP_PROJECT_ID')

# Your RSS API Key. See "Account Settings -> Tokens" in OpenProject.
OP_RSS_KEY = os.environ.get('OP_RSS_KEY')

# Specify elements you want to track. Recognizes everything except "cost_objects" and "time_entries" by default:
OP_RSS_FILTER = ('work_packages', 'wiki_edits', 'news', 'documents', 'meetings')
# ---
# CONFIGURATION END


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
logging.info("Started %s. Current version: %s", PROGRAM_NAME, PROGRAM_VERSION)

bot = dolphin.DolphinBot(SLACK_INCOMING_HOOK_URL, OP_BASE_URL, OP_PROJECT_ID, OP_RSS_KEY, OP_RSS_FILTER,
                         refresh_rate=150, max_links=15, smart_summary_limit=2)
bot.run()
