from first_meeting import firstMeeting
import json


def compileVN():
    # First, run the VN script to gather all states and transitions
    
    # Execute the firstMeeting function to gather all the commands
    script_actions = firstMeeting()
    print(script_actions)
    return convertVN(script_actions)


def convertVN(actions: list[dict]) -> list[dict]:
    updated_actions = []
    actionIndex = 0
    for action in actions:
        if action["type"] != "meta":
            action["id"] = actionIndex
            updated_actions.append(action)
            actionIndex +=1
            if action["type"] == "conditional":
                for subaction in action["actions"]:
                    subaction["id"] = actionIndex
                    actionIndex += 1
                action["end"] = actionIndex
            
    return updated_actions

def save_to_json_file(data: list[dict], file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)







def main():
    print("Compiling VN script to FSM...")
    fsm =compileVN()
    save_to_json_file(fsm,"story.json")
    #     save_fsm_to_file(fsm)
    #     print(f"Successfully compiled and saved FSM to vn_script.json")
    # except Exception as e:
    #     print(f"Error during compilation: {str(e)}")
    # try:
        
    #     # Write the FSM to a JSON file
    #     with open("humu.json", 'w', encoding='utf-8') as f:
    #         json.dump(fsm, f, indent=2, ensure_ascii=False)
        
    #     print(f"Done Bitch")
        
    # except Exception as e:
    #     print(f"Error processing the file: {e}")

if __name__ == "__main__":
    main()