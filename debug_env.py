# debug_env.py
import os
from pathlib import Path
from dotenv import load_dotenv, dotenv_values

def debug_env():
    print("=== .env FILE DEBUGGING ===")
    
    current_dir = Path.cwd()
    env_file = current_dir / '.env'
    print(f".env file exists: {env_file.exists()}")
    
    if env_file.exists():
        # Read and display RAW content
        print("\n--- RAW FILE CONTENT ---")
        try:
            with open(env_file, 'r') as f:
                content = f.read()
            print(f"File size: {len(content)} characters")
            print(f"Content:\n{repr(content)}")  # repr shows hidden characters
            
            print("\n--- LINE BY LINE ---")
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                print(f"Line {i}: {repr(line)} (length: {len(line)})")
                
        except Exception as e:
            print(f"Error reading file: {e}")
        
        # Try python-dotenv parsing
        print("\n--- PYTHON-DOTENV PARSING ---")
        try:
            env_vars = dotenv_values(env_file)
            print(f"Variables found: {len(env_vars)}")
            for k, v in env_vars.items():
                print(f"  {k}: {repr(v)}")
        except Exception as e:
            print(f"Error parsing: {e}")

if __name__ == '__main__':
    debug_env()