import json
import sys
import time
from dataclasses import dataclass
from typing import *
import os
import json
from typing import Dict, Any, List
import time
import os

class VisualNovelEngine:
    def __init__(self, game_data: Dict[str, Any]):
        self.game_data = game_data
        self.current_state = game_data["initial_state"]
        self.variables = game_data["variables"].copy()
        self.states = game_data["states"]
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def show_sprite(self, sprite_path: str):
        print(f"\n[Showing sprite: {sprite_path}]\n")
        
    def show_dialogue(self, label: str, content: str):
        print(f"\n{label}: {content}")
        input("\nPress Enter to continue...")
        
    def modify_variable(self, variable: str, operation: str, value: Any):
        if operation == "increment":
            self.variables[variable] += value
        elif operation == "set":
            # Handle special cases like get_gamemode
            if isinstance(value, dict) and value.get("type") == "get_gamemode":
                self.variables[variable] = self.variables.get("gamemode", "normal")
            else:
                self.variables[variable] = value
                
    def give_item(self, item: str, amount: int):
        print(f"\n[Received {amount}x {item}]\n")
        input("Press Enter to continue...")
        
    def process_conditional(self, conditional: Dict[str, Any], actions: List[Dict[str, Any]]) -> str:
        variable_value = self.variables.get(conditional["variable"])
        condition_value = conditional["value"]
        
        if conditional["condition"] == "equal":
            result = variable_value == condition_value
        elif conditional["condition"] == "greater_than":
            result = variable_value > condition_value
        else:
            return ""
            
        if result:
            return self.process_actions(conditional.get("actions", []))
        return ""
            
    def process_actions(self, actions: List[Dict[str, Any]]) -> str:
        for action in actions:
            action_type = action["type"]
            
            if action_type == "show_sprite":
                self.show_sprite(action["sprite"])
            elif action_type == "dialogue":
                self.show_dialogue(action["label"], action["content"])
            elif action_type == "modify_variable":
                self.modify_variable(action["variable"], action["operation"], action["value"])
            elif action_type == "give_item":
                self.give_item(action["item"], action["amount"])
            elif action_type == "conditional":
                next_state = self.process_conditional(action, action.get("actions", []))
                if next_state:  # If conditional returned a transition
                    return next_state
            elif action_type == "transition" and action.get("action") == "jump":
                return action["label"]
            elif action_type == "finish_dialogue":
                return "END"
                
        return ""
        
    def show_choices(self, choices: Dict[str, str]) -> str:
        print("\nChoices:")
        for idx, (key, value) in enumerate(choices.items(), 1):
            print(f"{idx}. {value}")
            
        while True:
            try:
                choice = int(input("\nEnter your choice (number): ")) - 1
                if 0 <= choice < len(choices):
                    return list(choices.keys())[choice]
            except ValueError:
                pass
            print("Invalid choice. Please try again.")
            
    def run(self):
        while True:
            self.clear_screen()
            current_state_data = self.states[self.current_state]
            
            # Process actions
            next_state = self.process_actions(current_state_data.get("actions", []))
            if next_state == "END":
                break
            elif next_state:  # Handle jumps
                self.current_state = next_state
                continue  # Skip choice processing and immediately process the new state
                
            # Handle choices if present
            choices = current_state_data.get("choices")
            if choices:
                self.current_state = self.show_choices(choices)
            else:
                break

def main():
    if len(sys.argv) != 2:
        print("Usage: python vn_engine.py <script.json>")
        sys.exit(1)
        
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            game_data = json.load(f)
            
        print("=== Terminal Visual Novel ===")
        print(f"Loading script: {sys.argv[1]}")
        input("Press Enter to start...")
        
        engine = VisualNovelEngine(game_data)
        engine.run()
        
        print("\nGame finished! Thanks for playing!")
        
    except FileNotFoundError:
        print(f"Error: Could not find file '{sys.argv[1]}'")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{sys.argv[1]}': {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nGame terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()