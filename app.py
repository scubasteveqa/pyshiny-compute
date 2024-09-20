import psutil
from shiny import App, ui, render, reactive

# Define the user interface
app_ui = ui.page_fluid(
    ui.h2("Server CPU and Memory Usage"),
    ui.output_text_verbatim("cpu_usage"),
    ui.output_text_verbatim("memory_usage")
)

# Define server logic
def server(input, output, session):
    @reactive.Effect
    @reactive.event(input)
    def monitor_system():
        # Get CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)

        # Get memory information
        memory_info = psutil.virtual_memory()
        available_memory_gb = memory_info.available / (1024 ** 3)  # Convert to GB
        total_memory_gb = memory_info.total / (1024 ** 3)  # Convert to GB
        memory_percent = memory_info.percent

        # Update the text outputs
        output.cpu_usage.set_text(f"CPU Usage: {cpu_percent}%")
        output.memory_usage.set_text(f"Memory Usage: {memory_percent}% - Available: {available_memory_gb:.2f} GB / Total: {total_memory_gb:.2f} GB")

# Create the Shiny app object
app = App(app_ui, server)

# Run the app, bind to all interfaces
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
