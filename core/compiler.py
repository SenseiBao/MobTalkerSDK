import json


def compileVN(script):
    # First, run the VN script to gather all states and transitions
    
    # Execute the firstMeeting function to gather all the commands
    script_actions = script
    print(script_actions)
    return convertVN(script_actions)

# Flatten Conditional Statement
def convertVN(actions: list[dict]) -> list[dict]:
    updated_actions = []
    actionIndex = 0
    for action in actions:
        action["id"] = actionIndex
        if action["type"] == "conditional":
            subactions = []
            # actionIndex = actionIndex + len(action["actions"])
            for subaction in action["actions"]:
                actionIndex += 1
                subaction["id"] = actionIndex
                subactions.append(subaction)
                
            action["end"] = actionIndex+1
            updated_actions.append(action)
            updated_actions+=subactions
            actionIndex +=1
        else:
            updated_actions.append(action)
            actionIndex +=1
            
    return updated_actions

def save_to_json_file(data: list[dict], file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def compile(storyname,script):
    print("Compiling VN script to FSM...")
    fsm =compileVN(script)
    save_to_json_file(fsm,storyname+".json")