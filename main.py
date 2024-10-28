import json
from first_meeting import firstMeeting
import os

def initialize_fsm() -> dict[str, any]:
    """Initialize the basic FSM structure."""
    return {
        "initial_state": "start",
        "variables": {},
        "states": {}
    }

def process_meta_action(action: dict[str, str], fsm: dict[str, any]) -> None:
    """Process meta actions and update the FSM accordingly."""
    if action["action"] == "initialize":
        pass  # FSM is already initialized
    elif action["action"] == "create_var":
        fsm["variables"][action["var"]] =action["init"]

    elif action["action"] == "label":
        if action["label"] not in fsm["states"]:
            fsm["states"][action["label"]] = {"actions": []}

def create_action_dict(script_action: dict[str, any]) -> list[dict[str, any]|None]:
    """Convert a script action into the FSM action format."""
    action_type = script_action["action"]
    
    if action_type == "show":
        return {
            "type": "show_sprite",
            "sprite": script_action["sprite"]
        }
    elif action_type == "say":
        if script_action["label"] == "":
            return {
                "type": "dialogue",
                "speaker": "Narrator",
                "content": script_action["content"]
            }
        return {
            "type": "dialogue",
            "speaker": script_action["label"],
            "content": script_action["content"]
        }
    elif action_type == "choice":
        return {
            "type": "choice",
            "options": script_action["choice"]
        }
    elif action_type == "conditional":
        return {
            "type": "conditional",
            "condition": script_action["condition"],
            "variable":script_action["var"],
            "value":script_action["value"],
            "actions":script_action["actions"]
        }
    elif action_type == "increment_var":
        return {
            "type": "modify_variable",
            "variable": script_action["var"],
            "operation": "increment",
            "value": script_action["amount"],
            
        }
    elif action_type == "modify_var":
        return {
            "type": "modify_variable",
            "variable": script_action["var"],
            "operation": "set",
            "value": script_action["value"]
        }
    elif action_type == "jump":
        return {
            "type": "transition",
            "action": "jump",
            "label": script_action["label"]
        }
    elif action_type == "give_player":
        return {
            "type": "give_item",
            "item": script_action["item_id"],
            "amount": script_action["amount"]
        }
    elif action_type == "get_gamemode":
        return {
            "type": "get_gamemode",
            "variable": "gamemode"
        }
    elif action_type == "finish_dialogue":
        return {
            "type": "finish_dialogue"
        }
    return None

def process_script_action(action: dict[str, any], current_state: str, fsm: dict[str, any]) -> None:
    """Process script actions and update the FSM accordingly."""
    if "type" in action and action["type"] == "meta":
        process_meta_action(action, fsm)
        return

    action_dict = create_action_dict(action)
    if action_dict is None:
        return

    if action_dict["type"] == "choice":
        fsm["states"][current_state]["choices"] = action_dict["options"]
    # elif action_dict["type"] == "jump":
    #     fsm["states"][current_state]["next"] = action_dict["target"]
    else:
        if "actions" not in fsm["states"][current_state]:
            fsm["states"][current_state]["actions"] = []
        fsm["states"][current_state]["actions"].append(action_dict)

def convert_vn_to_fsm(vn_script: list[dict[str, any]]) -> dict[str, any]:
    print("""Convert VN script to FSM format.""")
    fsm = initialize_fsm()
    current_state = None

    for action in vn_script:
        # Process meta actions regardless of current state
        if "type" in action and action["type"] == "meta":
            process_meta_action(action, fsm)
            # Update current state if it's a label action
            if action["action"] == "label":
                current_state = action["label"]
        # Process other actions only if we have a current state
        elif current_state is not None:
            process_script_action(action, current_state, fsm)

    return fsm


def compile_vn_to_fsm():
    # First, run the VN script to gather all states and transitions
    
    # Execute the firstMeeting function to gather all the commands
    script_actions = firstMeeting()
    print(script_actions)
    return convert_vn_to_fsm(script_actions)
    
    
def main():
    
    print("Compiling VN script to FSM...")
    fsm = compile_vn_to_fsm()
    #     save_fsm_to_file(fsm)
    #     print(f"Successfully compiled and saved FSM to vn_script.json")
    # except Exception as e:
    #     print(f"Error during compilation: {str(e)}")
    try:
        
        # Write the FSM to a JSON file
        with open("humu.json", 'w', encoding='utf-8') as f:
            json.dump(fsm, f, indent=2, ensure_ascii=False)
        
        print(f"Done Bitch")
        
    except Exception as e:
        print(f"Error processing the file: {e}")

if __name__ == "__main__":
    main()