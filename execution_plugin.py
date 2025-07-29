"""
This is where the implementation of the plugin code goes.
The ExecutionPlugin-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('ExecutionPlugin')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class ExecutionPlugin(PluginBase):
  def main(self):
        import os
        import subprocess

        core = self.core
        logger = self.logger
        active_node = self.active_node

        logger.info("🚀 Starting Execution Plugin")

