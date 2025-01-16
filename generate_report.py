import json
import os
import base64
import matplotlib.pyplot as plt
from io import BytesIO

# Sample results creation function (if 'results.json' is missing)
def create_sample_results_file():
    sample_data = [
        {
            "elements": [
                {
                    "name": "Test Scenario 1",
                    "steps": [
                        {
                            "name": "Step 1",
                            "result": {"status": "passed", "duration": 120}
                        },
                        {
                            "name": "Step 2",
                            "result": {"status": "failed", "duration": 100}
                        }
                    ],
                    "duration": 250
                }
            ]
        },
        {
            "elements": [
                {
                    "name": "Test Scenario 2",
                    "steps": [
                        {
                            "name": "Step 1",
                            "result": {"status": "skipped", "duration": 0}
                        },
                        {
                            "name": "Step 2",
                            "result": {"status": "passed", "duration": 150}
                        }
                    ],
                    "duration": 200
                }
            ]
        }
    ]

    with open("results.json", "w") as json_file:
        json.dump(sample_data, json_file)
    print("Sample 'results.json' file created.")

# Ensure 'results.json' exists
if not os.path.exists("results.json"):
    print("Error: 'results.json' file is missing. Creating a sample results file.")
    create_sample_results_file()

# Load the JSON results
with open("results.json", "r") as json_file:
    results = json.load(json_file)

# Function to generate the pie chart for Test Summary
def generate_pie_chart(passed, failed, skipped):
    # Ensure the total count is not zero to avoid division by zero
    total = passed + failed
    if total == 0:
        return ""  # Return an empty string if no tests are available to display in the pie chart
    
    labels = ['Passed', 'Failed']  # Only include 'Passed' and 'Failed'
    sizes = [passed, failed]  # Only use 'passed' and 'failed' values
    colors = ['#4CAF50', '#F44336']  # Colors for passed and failed

    fig, ax = plt.subplots()
    wedges, texts = ax.pie(sizes, labels=labels, colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'})

    # Adjust text properties
    for text in texts:
        text.set_fontsize(10)
        text.set_color('black')
        
    ax.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.

    # Encode the figure into a base64 string (for embedding in HTML)
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

    return f"data:image/png;base64,{img_base64}"

# New function to generate the Pass/Fail/Skipped Distribution chart (stacked bar chart) for Test Execution Graph
def generate_pass_fail_skipped_distribution_chart(results):
    passed = sum(1 for feature in results for scenario in feature['elements'] if any(step['result']['status'] == 'passed' for step in scenario.get('steps', [])))
    failed = sum(1 for feature in results for scenario in feature['elements'] if any(step['result']['status'] == 'failed' for step in scenario.get('steps', [])))
    skipped = sum(1 for feature in results for scenario in feature['elements'] if any(step['result']['status'] == 'skipped' for step in scenario.get('steps', [])))
    
    fig, ax = plt.subplots()
    ax.bar(['Passed', 'Failed', 'Skipped'], [passed, failed, skipped], color=['green', 'red', 'yellow'])
    ax.set_ylabel('Count')
    ax.set_title('Test Execution Graph: Pass/Fail/Skipped Distribution')

    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
    
    return f"data:image/png;base64,{img_base64}"

# Function to generate the report
def generate_report():
    # Initialize counters for passed, failed, and skipped tests
    passed = 0
    failed = 0
    skipped = 0
    scenarios = []
    
    # Loop through the results to update passed, failed, and skipped
    for feature in results:
        for scenario in feature['elements']:
            scenario_name = scenario['name']
            status = 'passed'  # Default to 'passed' initially
            duration = scenario.get('duration', 0)

            if duration == 0:
                duration = sum(step['result']['duration'] for step in scenario.get('steps', []) if 'result' in step and 'duration' in step['result'])

            scenario_failed = False
            scenario_skipped = False

            for step in scenario.get('steps', []):
                step_status = 'undefined'
                if 'result' in step:
                    if step['result']['status'] == 'passed':
                        step_status = 'passed'
                    elif step['result']['status'] == 'failed':
                        step_status = 'failed'
                        scenario_failed = True
                    elif step['result']['status'] == 'skipped':
                        step_status = 'skipped'
                        scenario_skipped = True

            if scenario_failed:
                status = 'failed'
            elif scenario_skipped:
                status = 'skipped'

            scenarios.append({
                "name": scenario_name,
                "status": status.capitalize(),
                "duration": f"{duration} ms" if duration > 0 else "No Duration",
            })

            if status == 'passed':
                passed += 1
            elif status == 'failed':
                failed += 1
            elif status == 'skipped':
                skipped += 1

    # Generate the test summary pie chart (Test Summary Pie Chart)
    pie_chart_image = generate_pie_chart(passed, failed, skipped)
    
    # Generate the pass/fail/skipped distribution chart for Test Execution Graph only
    test_execution_graph_image = generate_pass_fail_skipped_distribution_chart(results)

    # Generate the HTML report using a template
    try:
        with open("report_template.html", "r") as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print("Error: 'report_template.html' file is missing.")
        return

    # Prepare report data
    report_data = {
        "total_scenarios": passed + failed + skipped,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "scenarios": scenarios,
        "test_execution_graph_image": test_execution_graph_image,  # Both Pass/Fail/Skipped distribution for Test Execution Graph
        "test_summary_pie_chart_image": pie_chart_image,  # Image for the Test Summary Pie Chart
    }

    # Replace placeholders with actual data
    html_report = template_content.replace("{{ total_scenarios }}", str(report_data["total_scenarios"])) \
                                   .replace("{{ passed }}", str(report_data["passed"])) \
                                   .replace("{{ failed }}", str(report_data["failed"])) \
                                   .replace("{{ skipped }}", str(report_data["skipped"]))

    scenarios_html = ""
    for scenario in report_data["scenarios"]:
        scenarios_html += f'<tr class="result-{scenario["status"].lower()}">' \
                          f'<td>{scenario["name"]}</td>' \
                          f'<td>{scenario["status"]}</td>' \
                          f'<td>{scenario["duration"]}</td>' \
                          '</tr>'

    html_report = html_report.replace("{{ content }}", scenarios_html)
    html_report = html_report.replace("{{ test_execution_graph_image }}", report_data["test_execution_graph_image"])  # Image for Test Execution Graph
    html_report = html_report.replace("{{ test_summary_pie_chart_image }}", report_data["test_summary_pie_chart_image"])  # Image for Test Summary Pie Chart

    with open("report.html", "w") as report_file:
        report_file.write(html_report)

    print("Report generated successfully: report.html")

if __name__ == "__main__":
    generate_report()
