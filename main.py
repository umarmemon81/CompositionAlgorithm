from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import sys
from io import StringIO
import Algorithm17102025
app = FastAPI()


#     uvicorn main:app --reload

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/execute")
async def execute_composition(files: List[UploadFile] = File(...)):
    try:
        if len(files) != 3:
            return {
                "success": False,
                "error": f"Expected 3 files, got {len(files)}"
            }
        
        # Read and parse the JSON files
        file_contents = {}
        for file in files:
            content = await file.read()
            file_contents[file.filename] = json.loads(content.decode('utf-8'))
        
        # Get the data
        available_inputs_data = file_contents.get('available_inputs.json', {})
        models_data = file_contents.get('models.json', {})
        compositionRequirements_data = file_contents.get('compositionRequirements.json', [])
        
        # Import the algorithm module

        
        # Update the global variables in the module
        Algorithm17102025.available_inputs = available_inputs_data
        Algorithm17102025.models = models_data
        Algorithm17102025.compositionRequirements = compositionRequirements_data
        
        # Capture stdout
        output_capture = StringIO()
        sys.stdout = output_capture
        
        try:
            # Execute the entire main block (same as running the script directly)
            print("=== QUALITY-AWARE MODEL COMPOSITION SYSTEM ===")
            print()
            
            print("Goal:")
            for req in compositionRequirements_data:
                if "output" in req:
                    goal_name = req["output"]["name"]
                    print(f"   • Output: {goal_name}")
                    break
            print()

            print("Composition Requirements:")
            for req in compositionRequirements_data:
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
            
            # ORIGINAL ALGORITHM (finds first solution)
            print("🔹 ORIGINAL ALGORITHM (First solution only):")
            goal_output_name = Algorithm17102025.get_goal()
            initial_models = Algorithm17102025.First_model(models_data, goal_output_name, compositionRequirements_data)
            
            if not initial_models:
                print("No initial models found!")
            else:
                final_composite_model = None
                
                for initial_model in initial_models:
                    fresh_composite_model = []
                    
                    result_composite = Algorithm17102025.Build_Composite_Model_Recursively(
                        initial_model, fresh_composite_model, models_data, 
                        available_inputs_data, compositionRequirements_data
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
            all_solutions = Algorithm17102025.find_all_compositions()
            
            print(f"\n💡 SUMMARY ")
            print(f"   • Dataset: Extended with 3 new models")
            print(f"   • Multiple valid compositions: {len(all_solutions)} found")
            print(f"   • Algorithm can now find ALL valid options")
            print(f"   • Decision layer can choose optimal composition")
            
            # Restore stdout
            sys.stdout = sys.__stdout__
            
            # Get captured output
            console_output = output_capture.getvalue()
            
            return {
                "success": True,
                "solutions": all_solutions,
                "total_compositions": len(all_solutions),
                "console_output": console_output
            }
        except Exception as e:
            sys.stdout = sys.__stdout__
            raise e
        
    except Exception as e:
        sys.stdout = sys.__stdout__
        import traceback
        return {
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }

@app.get("/")
def read_root():
    return {"message": "Model Composition API is running"}