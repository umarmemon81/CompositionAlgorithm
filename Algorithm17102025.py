# Your original dataset + some new models to create multiple valid compositions
available_inputs = {
    "current_tank_level_Tank_C": [
        {
            "name": "Accuracy",
            "requirement": {"value": 94, "unit": "%"},
            "criterion": {"operator": "GreaterThanOrEqual", "threshold": 94}
        },
        {
            "name": "Latency",
            "requirement": {"value": 100, "unit": "milliseconds"},
            "criterion": {"operator": "LessThanOrEqual", "threshold": 100}
        }
    ],
    "pipe_diameter_pipe_a": [
        {
            "name": "Accuracy",
            "requirement": {"value": 96, "unit": "%"},
            "criterion": {"operator": "GreaterThanOrEqual", "threshold": 96}
        },
        {
            "name": "Latency",
            "requirement": {"value": 50, "unit": "milliseconds"},
            "criterion": {"operator": "LessThanOrEqual", "threshold": 50}
        }
    ],
    "tank_dimension_Tank_C": [
        {
            "name": "Accuracy",
            "requirement": {"value": 98, "unit": "%"},
            "criterion": {"operator": "GreaterThanOrEqual", "threshold": 98}
        },
        {
            "name": "Latency",
            "requirement": {"value": 80, "unit": "milliseconds"},
            "criterion": {"operator": "LessThanOrEqual", "threshold": 80}
        }
    ],
    "pipe_diameter_b": [
        {
            "name": "Accuracy",
            "requirement": {"value": 95, "unit": "%"},
            "criterion": {"operator": "GreaterThanOrEqual", "threshold": 95}
        },
        {
            "name": "Latency",
            "requirement": {"value": 60, "unit": "milliseconds"},
            "criterion": {"operator": "LessThanOrEqual", "threshold": 60}
        }
    ],
    "valve_position_pipe_a": [
        {
            "name": "Accuracy",
            "requirement": {"value": 96, "unit": "%"},
            "criterion": {"operator": "GreaterThanOrEqual", "threshold": 96}
        },
        {
            "name": "Latency",
            "requirement": {"value": 50, "unit": "milliseconds"},
            "criterion": {"operator": "LessThanOrEqual", "threshold": 50}
        }
    ],
    "valve_position_pipe_b": [
        {
            "name": "Accuracy",
            "requirement": {"value": 96, "unit": "%"},
            "criterion": {"operator": "GreaterThanOrEqual", "threshold": 96}
        },
        {
            "name": "Latency",
            "requirement": {"value": 60, "unit": "milliseconds"},
            "criterion": {"operator": "LessThanOrEqual", "threshold": 60}
        }
    ]
}

# Your original models + 3 new models to create multiple valid compositions
models = {
    "m1": {
        "name": "m1",
        "inputs": ["flow_rate_pipe_a", "flow_rate_pipe_b", "current_tank_level_Tank_C", "tank_dimension_Tank_C"],
        "output": "Predicted_time_to_fill_Tank_C",        
        "inputsqualities": {
            "flow_rate_pipe_a": [
                {"name": "Accuracy", "requirement": {"value": 96, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 96}},
                {"name": "Latency", "requirement": {"value": 100, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 100}}
            ],
            "flow_rate_pipe_b": [
                {"name": "Accuracy", "requirement": {"value": 95, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 95}},
                {"name": "Latency", "requirement": {"value": 120, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 120}}
            ],
            "current_tank_level_Tank_C": [
                {"name": "Accuracy", "requirement": {"value": 94, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 94}},
                {"name": "Latency", "requirement": {"value": 100, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 100}}
            ],
            "tank_dimension_Tank_C": [
                {"name": "Accuracy", "requirement": {"value": 98, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 98}},
                {"name": "Latency", "requirement": {"value": 80, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 80}}
            ]
        },
        "outputqualities": [
            {"name": "Accuracy", "requirement": {"value": 95.75, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 95.75}},
            {"name": "Latency", "requirement": {"value": 400, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 400}}
        ],
        "output_name": "Predicted_time_to_fill_Tank_C"
    },
    "m2": {
        "name": "m2",
        "inputs": ["flow_rate_pipe_a", "flow_rate_pipe_b", "current_tank_level_Tank_C", "tank_dimension_Tank_C"],
        "output": "Predicted_time_to_fill_Tank_C",
        "inputsqualities": {
            "flow_rate_pipe_a": [
                {"name": "Accuracy", "requirement": {"value": 94, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 94}},
                {"name": "Latency", "requirement": {"value": 120, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 120}}
            ],
            "flow_rate_pipe_b": [
                {"name": "Accuracy", "requirement": {"value": 92, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 92}},
                {"name": "Latency", "requirement": {"value": 120, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 120}}
            ],
            "current_tank_level_Tank_C": [
                {"name": "Accuracy", "requirement": {"value": 93, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 93}},
                {"name": "Latency", "requirement": {"value": 140, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 140}}
            ],
            "tank_dimension_Tank_C": [
                {"name": "Accuracy", "requirement": {"value": 92, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 92}},
                {"name": "Latency", "requirement": {"value": 120, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 120}}
            ]
        },
        "outputqualities": [
            {"name": "Accuracy", "requirement": {"value": 92.75, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 92.75}},
            {"name": "Latency", "requirement": {"value": 500, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 500}}
        ],
        "output_name": "Predicted_time_to_fill_Tank_C"
    },
    "m3": {
        "name": "m3",
        "inputs": ["pipe_diameter_pipe_a", "valve_position_pipe_a"],
        "output": "flow_rate_pipe_a",       
        "inputsqualities": {
            "pipe_diameter_pipe_a": [
                {"name": "Accuracy", "requirement": {"value": 96, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 96}},
                {"name": "Latency", "requirement": {"value": 50, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 50}}
            ],
            "valve_position_pipe_a": [
                {"name": "Accuracy", "requirement": {"value": 96, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 95}},
                {"name": "Latency", "requirement": {"value": 50, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 50}}
            ]
        },
        "outputqualities": [
            {"name": "Accuracy", "requirement": {"value": 96, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 96}},
            {"name": "Latency", "requirement": {"value": 100, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 100}}
        ],
        "output_name": "flow_rate_pipe_a"
    }, 
    "m4": {
        "name": "m4",
        "inputs": ["pipe_diameter_b", "valve_position_pipe_b"],
        "output": "flow_rate_pipe_b",
        "inputsqualities": {
            "pipe_diameter_b": [
                {"name": "Accuracy", "requirement": {"value": 96, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 96}},
                {"name": "Latency", "requirement": {"value": 100, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 110}}
            ],
            "valve_position_pipe_b": [
                {"name": "Accuracy", "requirement": {"value": 96, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 96}},
                {"name": "Latency", "requirement": {"value": 50, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 50}}
            ]
        },
        "outputqualities": [
            {"name": "Accuracy", "requirement": {"value": 95, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 95}},
            {"name": "Latency", "requirement": {"value": 110, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 110}}
        ],
        "output_name": "flow_rate_pipe_b"
    },
    "m5": {
        "name": "m5",
        "inputs": ["pipe_diameter_b", "valve_position_pipe_b"],
        "output": "flow_rate_pipe_b",
        "inputsqualities": {
            "pipe_diameter_b": [
                {"name": "Accuracy", "requirement": {"value": 96, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 95}},
                {"name": "Latency", "requirement": {"value": 59, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 60}}
            ],
            "valve_position_pipe_b": [
                {"name": "Accuracy", "requirement": {"value": 96, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 96}},
                {"name": "Latency", "requirement": {"value": 53, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 60}}
            ]
        },
        "outputqualities": [
            {"name": "Accuracy", "requirement": {"value": 95, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 95}},
            {"name": "Latency", "requirement": {"value": 117, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 120}}
        ],
        "output_name": "flow_rate_pipe_b"
    },
    
    # NEW: Just 3 additional models to create multiple valid compositions
    "m6": {
        "name": "m6",
        "inputs": ["current_tank_level_Tank_C", "tank_dimension_Tank_C"],
        "output": "Predicted_time_to_fill_Tank_C",
        "inputsqualities": {
            "current_tank_level_Tank_C": [
                {"name": "Accuracy", "requirement": {"value": 90, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 90}},
                {"name": "Latency", "requirement": {"value": 120, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 120}}
            ],
            "tank_dimension_Tank_C": [
                {"name": "Accuracy", "requirement": {"value": 95, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 95}},
                {"name": "Latency", "requirement": {"value": 100, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 100}}
            ]
        },
        "outputqualities": [
            {"name": "Accuracy", "requirement": {"value": 88, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 88}},
            {"name": "Latency", "requirement": {"value": 250, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 250}}
        ],
        "output_name": "Predicted_time_to_fill_Tank_C"
    },
    "m7": {
        "name": "m7",
        "inputs": ["pipe_diameter_pipe_a", "pipe_diameter_b"],
        "output": "flow_rate_pipe_a",
        "inputsqualities": {
            "pipe_diameter_pipe_a": [
                {"name": "Accuracy", "requirement": {"value": 94, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 94}},
                {"name": "Latency", "requirement": {"value": 60, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 60}}
            ],
            "pipe_diameter_b": [
                {"name": "Accuracy", "requirement": {"value": 92, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 92}},
                {"name": "Latency", "requirement": {"value": 70, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 70}}
            ]
        },
        "outputqualities": [
            {"name": "Accuracy", "requirement": {"value": 93, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 93}},
            {"name": "Latency", "requirement": {"value": 90, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 90}}
        ],
        "output_name": "flow_rate_pipe_a"
    },
    "m8": {
        "name": "m8",
        "inputs": ["pipe_diameter_b", "current_tank_level_Tank_C"],
        "output": "flow_rate_pipe_b",
        "inputsqualities": {
            "pipe_diameter_b": [
                {"name": "Accuracy", "requirement": {"value": 92, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 92}},
                {"name": "Latency", "requirement": {"value": 80, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 80}}
            ],
            "current_tank_level_Tank_C": [
                {"name": "Accuracy", "requirement": {"value": 90, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 90}},
                {"name": "Latency", "requirement": {"value": 110, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 110}}
            ]
        },
        "outputqualities": [
            {"name": "Accuracy", "requirement": {"value": 91, "unit": "%"}, "criterion": {"operator": "GreaterThanOrEqual", "threshold": 91}},
            {"name": "Latency", "requirement": {"value": 105, "unit": "milliseconds"}, "criterion": {"operator": "LessThanOrEqual", "threshold": 105}}
        ],
        "output_name": "flow_rate_pipe_b"
    }
}

compositionRequirements = [
    {
        "name": "Accuracy",
        "requirement": {"value": 85, "unit": "%"},
        "criterion": {"operator": "GreaterThanOrEqual", "threshold": 85}
    },
    {
        "name": "Latency",
        "requirement": {"value": 600, "unit": "milliseconds"},
        "criterion": {"operator": "LessThanOrEqual", "threshold": 600}
    },
    {
        "output": {"name": "Predicted_time_to_fill_Tank_C"}
    }
]

composite_model = []

# YOUR ORIGINAL FUNCTIONS (unchanged)
def check_quality_requirement(provided_quality, required_quality):
    """Check if provided quality meets required quality for a specific metric"""
    for req_qual in required_quality:
        req_name = req_qual["name"]
        req_operator = req_qual["criterion"]["operator"] 
        req_threshold = req_qual["criterion"]["threshold"] 
        
        provided_value = None
        for prov_qual in provided_quality:
            if prov_qual["name"] == req_name:
                provided_value = prov_qual["requirement"]["value"]
                break
        
        if provided_value is None:
            return False, f"Missing quality metric: {req_name}"
        
        if req_operator == "GreaterThanOrEqual":
            if provided_value < req_threshold:
                return False, f"{req_name}: {provided_value} < {req_threshold} (required)"
        elif req_operator == "LessThanOrEqual":
            if provided_value > req_threshold:
                return False, f"{req_name}: {provided_value} > {req_threshold} (required)"
        elif req_operator == "Equal":
            if provided_value != req_threshold:
                return False, f"{req_name}: {provided_value} != {req_threshold} (required)"
    
    return True, "Quality requirements met"

def checking_model_output_qualities(model, compositionRequirements):
    """Check if model's output qualities meet composition requirements"""
    print(f"Checking model {model['name']} output qualities against composition requirements")
    
    model_output_qualities = model["outputqualities"]
    
    for comp_req in compositionRequirements:
        if "name" in comp_req:
            req_name = comp_req["name"]
            req_operator = comp_req["criterion"]["operator"]
            req_threshold = comp_req["criterion"]["threshold"]
            
            model_output_value = None
            for output_qual in model_output_qualities:
                if output_qual["name"] == req_name:
                    model_output_value = output_qual["requirement"]["value"]
                    break
            
            if model_output_value is None:
                print(f"Model {model['name']} missing {req_name} in output qualities")
                return False
            
            meets_requirement = False
            if req_operator == "GreaterThanOrEqual":
                meets_requirement = model_output_value >= req_threshold
            elif req_operator == "LessThanOrEqual":
                meets_requirement = model_output_value <= req_threshold
            elif req_operator == "Equal":
                meets_requirement = model_output_value == req_threshold
            
            if meets_requirement:
                print(f"{req_name}: {model_output_value} meets {req_operator} {req_threshold}")
            else:
                print(f"{req_name}: {model_output_value} fails {req_operator} {req_threshold}")
                return False
    
    print(f"Model {model['name']} meets all composition requirements")
    return True

def checking_input_qualities(model, available_inputs, composite_model):
    """Check if model's required input qualities can be satisfied"""
    print(f"Checking input qualities for model {model['name']}:")
    
    for input_name in model["inputs"]:
        required_input_qualities = model["inputsqualities"][input_name]
        print(f"  Checking input: {input_name}")
        
        if input_name in available_inputs:
            provided_qualities = available_inputs[input_name]
            is_satisfied, message = check_quality_requirement(provided_qualities, required_input_qualities)
            if is_satisfied:
                print(f"External input satisfies requirements")
            else:
                print(f"External input fails: {message}")
                return False
        else:
            input_provider = None 
            for other_model in composite_model:
                if other_model['output'] == input_name:
                    input_provider = other_model
                    break
            
            if input_provider:
                provided_qualities = input_provider["outputqualities"]
                is_satisfied, message = check_quality_requirement(provided_qualities, required_input_qualities)
                if is_satisfied:
                    print(f"Provided by {input_provider['name']} - quality satisfied")
                else:
                    print(f"Provided by {input_provider['name']} - quality fails: {message}")
                    return False
            else:
                print(f"Input {input_name} not available and no provider found")
                return False
    
    return True

def First_model(models, goal_output_name, compositionRequirements):
    """Function for the model having required output"""
    print("Candidate models that can generate required goal of composition")
    candidates = []
    
    for key, model in models.items():
        if model["output"] == goal_output_name:
            print(f"   • Model {key} generates goal output {goal_output_name}")
            candidates.append(model)

    print()
    print("Checking output quality requirements for each candidate model")
    selected_models = []
    
    for candidate in candidates:
        print(f"\nEvaluating model: {candidate['name']}")
        if checking_model_output_qualities(candidate, compositionRequirements):
            selected_models.append(candidate)
    
    print(f"\nSelected {len(selected_models)} model(s) for initial composition that meet requirements:")
    for model in selected_models:
        print(f"   • {model['name']}")

    return selected_models

# YOUR ORIGINAL ALGORITHM WITH ONLY ONE MINIMAL CHANGE
def Build_Composite_Model_Recursively(model, composite_model, models, available_inputs, compositionRequirements, all_solutions=None):
    """Your original algorithm with minimal change to collect all solutions"""
    print()
    
    if not any(m.get('name') == model['name'] for m in composite_model):
        composite_model.append(model)
        print(f"Added {model['name']} to composite model")
    
    unconnected_inputs = []
    for input_name in model["inputs"]:
        if input_name not in available_inputs:
            if not any(m['output'] == input_name for m in composite_model):
                unconnected_inputs.append(input_name)
                print(f"input {input_name} needs to be connected")
    
    print(f"model {model['name']} needs models for {unconnected_inputs}")
    
    for needed_input in unconnected_inputs:
        print(f"Search for models in Library to provide: {needed_input}")
        
        provider_candidates = []
        for key, candidate_model in models.items():
            if candidate_model["output"] == needed_input:
                if not any(m.get('name') == candidate_model['name'] for m in composite_model):
                    provider_candidates.append(candidate_model)
        
        print(f"Found {len(provider_candidates)} potential providers")
        
        provider_found = False
        for candidate in provider_candidates:
            print(f"\n   Trying model candidate: {candidate['name']}")
            
            if not checking_model_output_qualities(candidate, compositionRequirements):
                print(f"{candidate['name']} doesn't meet composition requirements, trying next candidate...")
                continue 
            
            composite_backup = composite_model.copy()
            
            print(f"{candidate['name']} meets composition requirements, attempting to add...")
            
            result = Build_Composite_Model_Recursively(candidate, composite_model, models, available_inputs, compositionRequirements, all_solutions)
            
            if result is not None:
                print(f"Successfully added {candidate['name']} and its dependencies")
                provider_found = True
                
                # MINIMAL CHANGE: If collecting all solutions, don't break
                if all_solutions is None:
                    break  # Original behavior
                else:
                    # Continue searching for more solutions
                    composite_model.clear()
                    composite_model.extend(composite_backup)
                    continue
            else:
                print(f"{candidate['name']} failed quality requirements, removing and trying next candidate...")
                composite_model.clear()
                composite_model.extend(composite_backup)
                print(f"Restored composite model back to previous state, continuing with next candidate...")
        
        if not provider_found:
            print(f"CRITICAL: No qualified models found for: {needed_input}")
            return None
    
    print(f"\nFinal quality check for model {model['name']} after building dependencies:")
    if not checking_input_qualities(model, available_inputs, composite_model):
        print(f"Model {model['name']} input quality requirements cannot be satisfied even after building dependencies")
        return None
    
    # MINIMAL CHANGE: Store solution if collecting all
    if all_solutions is not None:
        solution_copy = [m.copy() for m in composite_model]
        all_solutions.append(solution_copy)
        print(f"✅ FOUND VALID COMPOSITION #{len(all_solutions)}: {[m['name'] for m in solution_copy]}")
    
    return composite_model

def get_goal():
    """Your original function"""
    for req in compositionRequirements:
        if "output" in req:
            goal_output_name = req["output"]["name"]
            break
    return goal_output_name

# NEW FUNCTION: Find all compositions
def find_all_compositions():
    """Find all valid compositions"""
    print("=== FINDING ALL VALID COMPOSITIONS ===")
    
    goal_output_name = get_goal()
    initial_models = First_model(models, goal_output_name, compositionRequirements)
    
    if not initial_models:
        return []
    
    all_solutions = []
    
    for initial_model in initial_models:
        print(f"\n🔍 Exploring all compositions starting with: {initial_model['name']}")
        fresh_composite_model = []
        
        Build_Composite_Model_Recursively(
            initial_model, fresh_composite_model, models, 
            available_inputs, compositionRequirements, all_solutions
        )
    
    print(f"\n📊 TOTAL VALID COMPOSITIONS FOUND: {len(all_solutions)}")
    for i, solution in enumerate(all_solutions, 1):
        model_names = [m['name'] for m in solution]
        print(f"   {i}. {' → '.join(model_names)}")
    
    return all_solutions

if __name__ == "__main__":
    print("=== QUALITY-AWARE MODEL COMPOSITION SYSTEM ===")
    print()
    
    print("Goal:")
    for req in compositionRequirements:
        if "output" in req:
            goal_name = req["output"]["name"]
            print(f"   • Output: {goal_name}")
            break
    print()

    print("Composition Requirements:")
    for req in compositionRequirements:
        if "name" in req:
            name = req["name"]
            requirement_value = req["requirement"]["value"]
            requirement_unit = req["requirement"]["unit"]
            criterion_operator = req["criterion"]["operator"]
            criterion_threshold = req["criterion"]["threshold"]
            
            print(f"• {name}:")
            print(f"    • Requirement: {requirement_value} {requirement_unit}")
            print(f"    • Criterion: Must be {criterion_operator} {criterion_threshold} {requirement_unit}")
    print()
   
    # YOUR ORIGINAL ALGORITHM (finds first solution)
    print("🔹 ORIGINAL ALGORITHM (First solution only):")
    goal_output_name = get_goal()
    initial_models = First_model(models, goal_output_name, compositionRequirements)
    
    if not initial_models:
        print("No initial models found!")
    else:
        final_composite_model = None
        
        for initial_model in initial_models:
            fresh_composite_model = []
            
            result_composite = Build_Composite_Model_Recursively(
                initial_model, fresh_composite_model, models, 
                available_inputs, compositionRequirements
            )
            
            if result_composite is not None:
                final_composite_model = result_composite
                break
        
        print()
        if final_composite_model:
            print(f"✅ ORIGINAL FOUND: {[m['name'] for m in final_composite_model]}")
        else:
            print("❌ ORIGINAL: COMPOSITION FAILED")
    
    print("\n" + "="*60)
    
    # MODIFIED ALGORITHM (finds all solutions)
    print("🔹 MODIFIED ALGORITHM (All solutions):")
    all_solutions = find_all_compositions()
    
    print(f"\n💡 SUMMARY ")
    print(f"   • Dataset: Extended with 3 new models")
    print(f"   • Multiple valid compositions: {len(all_solutions)} found")
    print(f"   • Algorithm can now find ALL valid options")
    print(f"   • Decision layer can choose optimal composition")