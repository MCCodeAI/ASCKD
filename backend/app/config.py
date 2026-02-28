import yaml
import os
from typing import Any, Dict
from pathlib import Path

class Config:
    _instance = None
    _config: Dict[str, Any] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        # Determine the path to config.yaml
        # Assuming config.yaml is in the same directory as this file (app/)
        config_path = Path(__file__).parent / "config.yaml"
        
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found at {config_path}")

        with open(config_path, "r") as f:
            self._config = yaml.safe_load(f)

    @property
    def search(self) -> Dict[str, Any]:
        return self._config.get("search", {})



# Global instance
config = Config()
