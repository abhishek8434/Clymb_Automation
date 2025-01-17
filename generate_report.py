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
                        {"name": "Step 1", "result": {"status": "passed", "duration": 120}},
                        {"name": "Step 2", "result": {"status": "failed", "duration": 100}}
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
                        {"name": "Step 1", "result": {"status": "skipped", "duration": 0}},
                        {"name": "Step 2", "result": {"status": "passed", "duration": 150}}
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
    labels = ['Passed', 'Failed']
    sizes = [passed, failed]
    colors = ['#4CAF50', '#F44336']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'})
    ax.axis('equal')

    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
    plt.close(fig)

    return f"data:image/png;base64,{img_base64}"

# Function to generate the Test Execution Graph (Bar Chart)
def generate_execution_graph(passed, failed, skipped):
    labels = ['Passed', 'Failed', 'Skipped']
    counts = [passed, failed, skipped]
    colors = ['#4CAF50', '#F44336', '#FFC107']

    fig, ax = plt.subplots()
    ax.bar(labels, counts, color=colors)
    ax.set_ylabel('Count')
    ax.set_title('Test Execution Distribution')

    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
    plt.close(fig)

    return f"data:image/png;base64,{img_base64}"

# Function to generate the report
def generate_report():
    passed = 0
    failed = 0
    skipped = 0
    total_duration = 0  # To hold the total execution time of all scenarios
    scenarios = []

    for feature in results:
        for scenario in feature['elements']:
            scenario_name = scenario['name']
            duration = scenario.get('duration', 0)
            if duration == 0:
                duration = sum(step['result']['duration'] for step in scenario.get('steps', []) if 'result' in step and 'duration' in step['result'])

            # Round the duration to 3 decimal places
            duration = round(duration, 3)

            total_duration += duration  # Add to the total execution time

            total_steps = 0
            passed_steps = 0
            failed_steps = 0
            status = 'passed'

            for step in scenario.get('steps', []):
                total_steps += 1
                if 'result' in step:
                    step_status = step['result']['status']
                    if step_status == 'passed':
                        passed_steps += 1
                    elif step_status == 'failed':
                        failed_steps += 1
                        status = 'failed'
            skipped_steps = total_steps - (passed_steps + failed_steps)  # Calculate skipped steps

            scenarios.append({
                "name": scenario_name,
                "status": status.capitalize(),
                "duration": f"{duration} ms" if duration > 0 else "No Duration",
                "total_steps": total_steps,
                "passed_steps": passed_steps,
                "failed_steps": failed_steps,
                "skipped_steps": skipped_steps,
            })

            if status == 'passed':
                passed += 1
            elif status == 'failed':
                failed += 1
            elif status == 'skipped':
                skipped += 1

    pie_chart_image = generate_pie_chart(passed, failed, skipped)
    execution_graph_image = generate_execution_graph(passed, failed, skipped)

    try:
        with open("report_template.html", "r") as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print("Error: 'report_template.html' file is missing.")
        return

    html_report = template_content.replace("{{ total_scenarios }}", str(passed + failed + skipped)) \
                                   .replace("{{ passed }}", str(passed)) \
                                   .replace("{{ failed }}", str(failed)) \
                                   .replace("{{ skipped }}", str(skipped)) \
                                   .replace("{{ total_execution_time }}", f"{round(total_duration, 3)} ms")  # Round total execution time

    scenarios_html = ""
    for scenario in scenarios:
        status_class = f"status-{scenario['status'].lower()}"  # Dynamic CSS class for status
        scenarios_html += f'<tr class="result-{scenario["status"].lower()}">' \
                          f'<td>{scenario["name"]}</td>' \
                          f'<td class="{status_class}">{scenario["status"]}</td>' \
                          f'<td>{scenario["duration"]}</td>' \
                          f'<td>{scenario["total_steps"]}</td>' \
                          f'<td>{scenario["passed_steps"]}</td>' \
                          f'<td>{scenario["failed_steps"]}</td>' \
                          f'<td>{scenario["skipped_steps"]}</td>' \
                          '</tr>'

    html_report = html_report.replace("{{ content }}", scenarios_html) \
                             .replace("{{ test_execution_graph_image }}", execution_graph_image) \
                             .replace("{{ test_summary_pie_chart_image }}", pie_chart_image)

    with open("report.html", "w") as report_file:
        report_file.write(html_report)

    print("Report generated successfully: report.html")

if __name__ == "__main__":
    generate_report()
