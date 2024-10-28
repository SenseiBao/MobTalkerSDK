import json
import vn_dialogue as vn
import cupa
from first_meeting import firstMeeting

def compile_actions(actions):
    compiled_actions = []
    for action in actions:
        if isinstance(action, dict):
            if action.get("action") == "say":
                compiled_action = {
                    "type": "dialogue",
                    "speaker": action.get("label"),
                    "text": action.get("content")
                }
                if action.get("label") is None:
                    compiled_action["type"] = "narration"
                compiled_actions.append(compiled_action)
            
            elif action.get("action") == "show":
                compiled_actions.append({
                    "type": "show",
                    "sprite": action.get("sprite")
                })
            
            elif action.get("action") == "increment_var":
                compiled_actions.append({
                    "type": "var_modify",
                    "var": action.get("var"),
                    "operation": "add",
                    "value": action.get("amount")
                })
            
            elif action.get("action") == "subtract_var":
                compiled_actions.append({
                    "type": "var_modify",
                    "var": action.get("var"),
                    "operation": "subtract",
                    "value": action.get("amount")
                })
            
            elif action.get("action") == "modify_var":
                compiled_actions.append({
                    "type": "var_modify",
                    "var": action.get("var"),
                    "operation": "set",
                    "value": action.get("value")
                })
            
            elif action.get("minecraft") == "giveItem":
                compiled_actions.append({
                    "type": "game_action",
                    "action": "give_item",
                    "item": action.get("id"),
                    "amount": action.get("amount")
                })

    return compiled_actions

def compile_conditions(condition):
    if not isinstance(condition, dict):
        return None
    
    compiled_condition = {
        "type": "",
        "var": condition.get("var"),
        "value": condition.get("value"),
        "actions": compile_actions(condition.get("actions", []))
    }
    
    if condition.get("condition") == "equal":
        compiled_condition["type"] = "equals"
    elif condition.get("condition") == "not_equal":
        compiled_condition["type"] = "not_equals"
    elif condition.get("condition") == "less_than":
        compiled_condition["type"] = "less_than"
    elif condition.get("condition") == "greater_than":
        compiled_condition["type"] = "greater_than"
        
    return compiled_condition

def compile_vn_to_fsm():
    # First, run the VN script to gather all states and transitions
    current_state = {
        "label": "start", 
        "actions": [], 
        "transitions": {}
    }
    states = {}
    variables = []
    
    # Execute the firstMeeting function to gather all the commands
    script_actions = firstMeeting()
    print(script_actions)
    
def main():
    
        print("Compiling VN script to FSM...")
        compile_vn_to_fsm()
    #     save_fsm_to_file(fsm)
    #     print(f"Successfully compiled and saved FSM to vn_script.json")
    # except Exception as e:
    #     print(f"Error during compilation: {str(e)}")

if __name__ == "__main__":
    main()