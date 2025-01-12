import json
from datetime import datetime

def save_report(data, filename="reports/scan_report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def generate_report(module, result):
    report = {
        "module": module,
        "timestamp": datetime.now().isoformat(),
        "result": result,
    }
    save_report(report)
    print(f"Report saved to reports/scan_report.json")
