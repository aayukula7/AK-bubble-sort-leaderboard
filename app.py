import gradio as gr

# Convert user input into a list
def process_input(input_str):
    data = []
    items = input_str.split(",")

    for item in items:
        name, score = item.split(":")
        data.append([name.strip(), int(score.strip())])

    return data

# Bubble sort function
def sort_leaderboard(data):
    steps = []
    comparisons = 0
    swaps = 0
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            steps.append("Comparing " + data[j][0] + " and " + data[j+1][0])

            if data[j][1] < data[j+1][1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                swaps += 1
                steps.append("Swapped")

    return data, steps, comparisons, swaps

# Format the final leaderboard
def make_leaderboard(data):
    result = "Leaderboard (Highest to Lowest)\n\n"
    position = 1

    for player in data:
        name = player[0]
        score = player[1]
        result += str(position) + ". " + name + " - " + str(score) + "\n"
        position += 1

    return result

# Main function for the app
def run_app(input_str):
    try:
        data = process_input(input_str)
        sorted_data, steps, comparisons, swaps = sort_leaderboard(data)

        output = ""
        for step in steps:
            output += step + "\n"

        output += "\n" + make_leaderboard(sorted_data)
        output += "\nTotal comparisons: " + str(comparisons)
        output += "\nTotal swaps: " + str(swaps)

        return output

    except:
        return "Invalid input. Use format like: sam:85, carl:72"


# Gradio interface
interface = gr.Interface(
    fn=run_app,
    inputs=gr.Textbox(label="Enter players and scores (e.g., sam:85, carl:72)"),
    outputs=gr.Textbox(label="Output"),
    title="Leaderboard Sorter (Bubble Sort)",
    description="This app sorts player scores using Bubble Sort."
)

interface.launch()