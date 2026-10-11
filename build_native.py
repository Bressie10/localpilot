from pathlib import Path 
import subprocess 

def build_native():
    native_dir = Path(__file__).parent / "native"

    programs = [
        'pwd',
        'ps'
    ]

    for program in programs:
        source = native_dir / f"{program}.c"
        output = native_dir / program 

        if not source.exists():
            print(f"Source file missing: {source}")
            continue

        result = subprocess.run(
            [
                "cc",
                str(source),
                "-o",
                str(output)
            ],
            capture_output=True,
            text=True
        )

        if result.returncode != 0: 
            print(f"Failed to compile {program}")
            print(result.stderr)
        else:
            print(f"Compiled {program}")