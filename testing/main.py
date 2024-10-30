import json
import sys
from typing import *
import os
import json
import os

class VisualNovelEngine:
    def __init__(self, game_data: list[dict]):
        self.game_data = game_data
        self.min_id = min(game_data, key=lambda x: x.get("id", float("inf")))["id"]
        self.max_id = max(game_data, key=lambda x: x.get("id", float("-inf")))["id"]
        self.current_state = 0
        self.variables = {}

        # Assuming each action dict always has an "id" key

    def find_label_id(self,var: str) -> int:
        for action in self.game_data:
            if action.get("type") == "label" and action.get("label") == var:
                return action.get("id")
        return None
    
    def get_dict_by_id(self,target_id: int) -> dict:
        for action in self.game_data:
            if action.get("id") == target_id:
                return action
        return None

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def show_sprite(self, sprite_path: str):
        print(f"\n[Showing sprite: {sprite_path}]\n")
        self.current_state +=1
        
    def show_dialogue(self, label: str, content: str):
        print(f"\n{label}: {content}")
        self.current_state +=1

    def process_command(self,value):
        if value["action"] == "get_gamemode":
            return "Survival"
        elif value["action"] == "custom_command":
            return "Nothing for now"
        else:
            return "Nothing for now"
        
    def modify_variable(self, variable: str, operation: str, value: Any):
        if isinstance(value,dict):

            value = self.process_command(value)
        if operation == "increment_var":
            self.variables[variable] += value
        elif operation == "substract_var":
            self.variables[variable] -= value
        else:
            self.variables[variable] = value
        self.current_state +=1

    def give_item(self, item: str, amount: int):
        print(f"\n[Received {amount}x {item}]\n")
        input("Press Enter to continue...")
        self.current_state +=1

    def process_jump(self, action):
        self.current_state = self.find_label_id(action["label"])
        

    def process_conditional(self, condition: dict):
        var = self.variables[condition["var"]]
        value = condition["value"]
        end = condition["end"]
        if value is dict:
            value = self.process_command(value)
        print(value)
        print(var)
        match condition["condition"]:
            case "equal":
                if var == value:
                    self.current_state += 1
                else:
                    self.current_state = end
            case "not_equal":
                if var != value:
                    self.current_state += 1
                else:
                    self.current_state = end
            case "less_than":
                if var < value:
                    self.current_state += 1
                else:
                    self.current_state = end
            case "greater_than":
                if var > value:
                    self.current_state += 1
                else:
                    self.current_state = end
    
    def show_choices(self, choices: dict[str, str]) -> str:
        print("\nChoices:")
        for number, (key, value) in enumerate(choices.items(), 1):
            print(f"{number}. {value}")
            
        while True:
            try:
                choice = int(input("\nEnter your choice (number): ")) - 1
                if 0 <= choice < len(choices):
                    targetLabel = list(choices.keys())[choice]
                    #print("Your choice is"+str(choice) + "and target is"+str(targetLabel))
                    self.current_state = self.find_label_id(targetLabel)
                    break
            except ValueError:
                pass
            print("Invalid choice. Please try again.")

    def create_variable(self,varName,varInit):
        self.variables[varName] = varInit
        self.current_state +=1
    
    def process_meta(self,action:dict[str,any]):
        action_type = action["action"]
        if action_type == "create_var":
            self.create_variable(action["var"],action["init"])
        else:
            self.current_state +=1
    

    def process_action(self, action: dict[str, any]) -> str:
        action_type = action["type"]
        
        if action_type == "show_sprite":
            self.show_sprite(action["sprite"])
        elif action_type == "dialogue":
            self.show_dialogue(action["label"], action["content"])
        elif action_type == "modify_variable":
            self.modify_variable( action["var"], action["action"], action["value"])
        elif action_type == "give_item":
            self.give_item(action["item"], action["amount"])
        elif action_type == "conditional":
            self.process_conditional(action)
        elif action_type == "transition" and action.get("action") == "jump":
            self.process_jump(action)
        elif action_type == "choice":
            self.show_choices(action["choice"])
        elif action_type == "command":
            self.process_command(action)
        elif action_type == "label":
            self.current_state+=1
        elif action_type == "finish_dialogue":
            return True
        else:
            self.current_state +=1
        return False
        
    
            
    def run(self):
        print("HENLO~ \n\n")
        self.clear_screen()
        while True:
            action = self.get_dict_by_id(self.current_state)
            if action["type"]=="meta":
                self.process_meta(action)
            else:
                if self.process_action(action):
                    return "END"
            

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


if __name__ == "__main__":
    main()