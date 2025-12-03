import sys
import json

def fill_values(tests_structure, values_dict):
    if isinstance(tests_structure, dict):
        if 'id' in tests_structure:
            test_id = tests_structure['id']
            if test_id in values_dict:
                tests_structure['value'] = values_dict[test_id]
        
        for key, value in tests_structure.items():
            if isinstance(value, list):
                tests_structure[key] = fill_values(value, values_dict)
            elif isinstance(value, dict):
                tests_structure[key] = fill_values(value, values_dict)
    
    elif isinstance(tests_structure, list):
        for i in range(len(tests_structure)):
            tests_structure[i] = fill_values(tests_structure[i], values_dict)
    
    return tests_structure

def main():
    if len(sys.argv) != 4:
        print("Usage: python task3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    
    values_file, tests_file, report_file = sys.argv[1:4]
    
    try:
        with open(values_file, 'r', encoding='utf-8') as f:
            values_data = json.load(f)
        
        with open(tests_file, 'r', encoding='utf-8') as f:
            tests_data = json.load(f)
        
        values_dict = {}
        for item in values_data['values']:
            values_dict[item['id']] = item['value']
        
        report_data = fill_values(tests_data, values_dict)
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
