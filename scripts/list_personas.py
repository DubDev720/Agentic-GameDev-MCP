"""
scripts/list_personas.py
Standalone helper to list personas in a personas YAML file.
Supports short list and verbose full definitions.
"""

import argparse
from core.persona_manager import PersonaManager

def main():
    parser = argparse.ArgumentParser(description="List personas in a personas YAML")
    parser.add_argument("--personas", required=True, help="Path to personas YAML file")
    parser.add_argument("--verbose", action="store_true", help="Show full persona definitions")
    args = parser.parse_args()

    pm = PersonaManager(args.personas)
    names = pm.list_personas()
    print(f"Available personas in {args.personas}:")
    for n in names:
        p = pm.get_persona(n)
        short = p.get("short", "")
        print(f" - {n}: {short}")
        if args.verbose:
            print("   Full definition:")
            for k, v in p.items():
                if k == "system_prompt":
                    print("   system_prompt:")
                    for line in v.splitlines():
                        print(f"     {line}")
                else:
                    print(f"   {k}: {v}")
            print("---")

if __name__ == "__main__":
    main()
