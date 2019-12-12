#!/usr/local/bin/python
import json

with open("eslintresults.json", "r") as f:
    eslint = json.load(f)

severities = {
    0: "info",
    1: "minor",
    2: "major",
    3: "critical",
}
meta = eslint["metadata"]["rulesMeta"]
outputs = []
for file in eslint["results"]:
    for message in file["messages"]:
        docs = meta[message["ruleId"]]["docs"]
        outputs.append({
            "type": "issue",
            "check_name": message["ruleId"],
            "description": message["message"],
            "content": {"body": f"{docs['category']}: {docs['description']}  \n{docs['url']}"},
            "categories": ["Style"],
            "location": {
                "line": message["line"],
                "column": message["column"],
            },
            "severity": severities[message["severity"]]
        })

with open("gl-code-quality-report.json", "w") as f:
    json.dump(outputs, f)
