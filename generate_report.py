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
    labels = []
    sizes = []
    colors = ['#4CAF50', '#F44336', '#FFC107']

    # Conditionally add data to avoid overlap when counts are 0
    if passed > 0:
        labels.append('Passed')
        sizes.append(passed)
    if failed > 0:
        labels.append('Failed')
        sizes.append(failed)
    if skipped > 0:
        labels.append('Skipped')
        sizes.append(skipped)
    
    # Handle case when all counts are zero
    if not labels:
        labels = ['No Data']
        sizes = [1]
        colors = ['#CCCCCC']

    fig, ax = plt.subplots(figsize=(7, 7))  # Adjust the size of the pie chart
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90,
                                      wedgeprops={'edgecolor': 'black'}, labeldistance=1.2)  # Moved labels outward

    # Adjust font size and alignment to improve readability
    for text in texts + autotexts:
        text.set_fontsize(10)
        text.set_horizontalalignment('center')

    # Equal aspect ratio ensures the pie chart is circular.
    ax.axis('equal')

    # Add a legend to help understand the colors
    ax.legend(wedges, labels, title="Test Status", loc="center left", bbox_to_anchor=(1.1, 0, 0.5, 1))  # Legend outside the pie chart

    img_buf = BytesIO()
    plt.savefig(img_buf, format='png', bbox_inches='tight')  # 'tight' to avoid clipping
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
    plt.close(fig)

    return f"data:image/png;base64,{img_base64}"


# Function to generate the Test Execution Graph (Bar Chart)
def generate_execution_graph(passed, failed, skipped):
    labels = ['Passed', 'Failed', 'Skipped']
    counts = [passed, failed, skipped]
    colors = ['#4CAF50', '#F44336', '#FFC107']

    # Increase the size of the figure
    fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted figure size (width, height)
    
    ax.bar(labels, counts, color=colors)
    ax.set_ylabel('Count')
    ax.set_title('Test Execution Distribution')

    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
    plt.close(fig)

    return f"data:image/png;base64,{img_base64}"

# Function to generate the report with correct feature, scenario, and step-level counters
def generate_report():
    # Overall counters
    passed = 0
    failed = 0
    skipped = 0
    total_duration = 0

    # Feature-level counters
    total_features = 0
    total_passed_features = 0
    total_failed_features = 0
    total_skipped_features = 0

    # Step-level counters (for Step Summary)
    total_steps = 0
    total_passed_steps = 0
    total_failed_steps = 0
    total_skipped_steps = 0

    scenarios = []

    # Loop through features and scenarios
    for feature in results:
        feature_passed_count = 0
        feature_failed_count = 0
        feature_skipped_count = 0

        total_features += 1  # Increment total features count

        # Go through scenarios of this feature
        for scenario in feature['elements']:
            scenario_name = scenario['name']
            duration = scenario.get('duration', 0)

            # If duration is zero, calculate based on step durations
            if duration == 0:
                duration = sum(step['result']['duration'] for step in scenario.get('steps', []) if 'result' in step and 'duration' in step['result'])

            # Round the duration to 3 decimal places
            duration = round(duration, 3)
            total_duration += duration

            # Step-level counters for this scenario
            total_steps_in_scenario = 0
            passed_steps = 0
            failed_steps = 0
            skipped_steps = 0
            scenario_status = "passed"  # Default scenario status

            # Process all steps of the scenario
            for step in scenario.get('steps', []):
                total_steps_in_scenario += 1
                if 'result' in step:
                    step_status = step['result']['status']
                    if step_status == 'passed':
                        passed_steps += 1
                    elif step_status == 'failed':
                        failed_steps += 1
                        scenario_status = 'failed'  # If any step fails, mark the scenario as failed
                    elif step_status == 'skipped':
                        skipped_steps += 1
                        scenario_status = 'skipped'  # If any step is skipped, mark the scenario as skipped

            # Calculate skipped steps explicitly
            skipped_steps = total_steps_in_scenario - (passed_steps + failed_steps)

            # Update counters based on scenario status
            if scenario_status == 'passed':
                passed += 1
            elif scenario_status == 'failed':
                failed += 1
            elif scenario_status == 'skipped':
                skipped += 1

            # Append the scenario data
            scenarios.append({
                "name": scenario_name,
                "status": scenario_status.capitalize(),
                "duration": f"{duration} ms" if duration > 0 else "No Duration",
                "total_steps": total_steps_in_scenario,
                "passed_steps": passed_steps,
                "failed_steps": failed_steps,
                "skipped_steps": skipped_steps,
            })

            # Feature-level scenario status aggregation
            if scenario_status == 'passed':
                feature_passed_count += 1
            elif scenario_status == 'failed':
                feature_failed_count += 1
            elif scenario_status == 'skipped':
                feature_skipped_count += 1

            # Add step data to the total step summary
            total_steps += total_steps_in_scenario
            total_passed_steps += passed_steps
            total_failed_steps += failed_steps
            total_skipped_steps += skipped_steps

        # After processing all scenarios of the feature, update feature status and counters
        if feature_passed_count == len(feature['elements']):
            total_passed_features += 1
        elif feature_skipped_count == len(feature['elements']):
            total_skipped_features += 1
        else:
            total_failed_features += 1

    # Generate the pie chart and execution graph
    pie_chart_image = generate_pie_chart(passed, failed, skipped)
    execution_graph_image = generate_execution_graph(passed, failed, skipped)

    # Load HTML template
    try:
        with open("report_template.html", "r") as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print("Error: 'report_template.html' file is missing.")
        return

    # Replace placeholders in template with calculated values
    html_report = template_content.replace("{{ total_scenarios }}", str(passed + failed + skipped)) \
                                   .replace("{{ passed }}", str(passed)) \
                                   .replace("{{ failed }}", str(failed)) \
                                   .replace("{{ skipped }}", str(skipped)) \
                                   .replace("{{ total_execution_time }}", f"{round(total_duration, 3)} ms")

    html_report = html_report.replace("{{ total_features }}", str(total_features)) \
                             .replace("{{ total_steps }}", str(total_steps)) \
                             .replace("{{ total_passed_features }}", str(total_passed_features)) \
                             .replace("{{ total_failed_features }}", str(total_failed_features)) \
                             .replace("{{ total_skipped_features }}", str(total_skipped_features)) \
                             .replace("{{ total_passed_steps }}", str(total_passed_steps)) \
                             .replace("{{ total_failed_steps }}", str(total_failed_steps)) \
                             .replace("{{ total_skipped_steps }}", str(total_skipped_steps))

    # Generate HTML content for the scenarios
    scenarios_html = ""
    for scenario in scenarios:
        status_class = f"status-{scenario['status'].lower()}"
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

    # Write the final HTML report to a file
    with open("report.html", "w") as report_file:
        report_file.write(html_report)

    print("Report generated successfully: report.html")

# Run the report generation
if __name__ == "__main__":
    generate_report()
