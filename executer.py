from toolss import Toolss

def executer(plan):
    output = []
    for step in plan.steps:
        tool_name = step.action
        input_data = step.input
        
        if tool_name not in Toolss:
            output.append({
                "step_id": step.id,
                "tool_name": tool_name,
                "status": "Failed",
                "output": "Tool not found"
            })
        else:
            toolfunction = Toolss[tool_name]
            result =  toolfunction(input_data)
            output.append({
                "step_id": step.id,
                "tool_name": tool_name,
                "status": "Success",
                "output": result
            })
        
    
    return output
        
    
    