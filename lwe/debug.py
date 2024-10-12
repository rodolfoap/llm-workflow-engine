import pprint
import tempfile
from typing import Any, Dict, List
from langchain_core.callbacks import StdOutCallbackHandler

LOG_FILE = "%s/%s" % (tempfile.gettempdir(), "lwe-debug.log")

pp = pprint.PrettyPrinter()
pf = pprint.PrettyPrinter(stream=open(LOG_FILE, "w"))


def console(*args, **kwargs):
    pp.pprint(*args, **kwargs)


def file(*args, **kwargs):
    pf.pprint(*args, **kwargs)


class CallbackHandler(StdOutCallbackHandler):
	def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> None:
		for prompt in prompts:
			print("-"*80)
			print(prompt)
		print("-"*80)

callback=[CallbackHandler()]
