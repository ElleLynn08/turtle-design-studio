"""
This is where the implementation of the plugin code goes.
The ImportPlugin-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('ImportPlugin')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class ImportPlugin(PluginBase):
  def main(self):
        core = self.core
        logger = self.logger
        active_node = self.active_node

        logger.info("📥 Starting import...")

        # ✅ Read the Python turtle code from the TurtleLang_instance
        code_input = core.get_attribute(active_node, "pythonCode")
        if not code_input:
            logger.error("❌ No 'pythonCode' found in the selected node.")
            return

        # ✅ Load all META node types
        meta_nodes = core.get_all_meta_nodes(self.root_node)
        cmd_map = {
            "forward": "Forward",
            "backward": "Backward",
            "left": "Left",
            "right": "Right",
            "width": "Width",
            "color": "Color",
            "goto": "GoTo",
            "circle": "Circle",
            "penup": "PenUp",
            "pendown": "PenDown",
            "clear": "Clear"
        }

        lines = code_input.strip().splitlines()
        previous = None

        for line in lines:
            line = line.strip()
            if not line.startswith("t."):
                continue
            parts = line[2:].split("(", 1)
            if len(parts) != 2:
                continue
            cmd_raw, arg = parts
            arg = arg.replace(")", "").strip()
            cmd_type = cmd_map.get(cmd_raw.lower())
            if not cmd_type:
                logger.warn(f"⚠️ Skipping unknown command type: {cmd_raw}")
                continue

            base_node = meta_nodes.get(cmd_type)
            if not base_node:
                logger.warn(f"⚠️ No base node found for: {cmd_type}")
                continue

            new_node = core.create_node(parent=active_node, base=base_node)
            core.set_attribute(new_node, "value", arg)

            if previous:
                core.set_pointer(previous, "next", core.get_path(new_node))

            previous = new_node

        logger.info("✅ Import complete!")




