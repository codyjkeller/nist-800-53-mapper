import json
import argparse
import sys

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: Mapping file not found.")
        sys.exit(1)

def query_control(control_id, data):
    for control in data:
        if control['control_id'].upper() == control_id.upper():
            return control
    return None

def main():
    """
    CLI Tool to look up CJIS/TX-RAMP requirements by NIST Control ID.
    Usage: python lookup_control.py --id AC-2
    """
    parser = argparse.ArgumentParser(description='NIST 800-53 Control Mapper')
    parser.add_argument('--id', type=str, required=True, help='The NIST Control ID (e.g., AC-2)')
    args = parser.parse_args()

    # Load the dataset
    data = load_data('../data/nist_cjis_mapping.json')
    
    # Find the control
    result = query_control(args.id, data)
    
    if result:
        print(f"\n--- {result['control_id']}: {result['title']} ---")
        print(f"NIST Baseline:   {result['nist_baseline']}")
        print(f"CJIS Ref:        {result['cjis_policy_ref']}")
        print(f"TX-RAMP:         {result['tx_ramp_level']}")
        print(f"Guidance:        {result['implementation_guidance']}\n")
    else:
        print(f"\n[!] Control {args.id} not found in current mapping.\n")

if __name__ == "__main__":
    main()
