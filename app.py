import psutil
from shiny import App, ui, render, reactive

# Define the user interface (UI)
app_ui = ui.page_fluid(
    ui.h2("Server CPU and Memory Usage"),
    ui.output_text_verbatim("cpu_usage"),  # Output for CPU usage
    ui.output_text_verbatim("memory_usage")  # Output for memory usage
)

# Define server logic
def server(input, output, session):
    # Define output for CPU usage
    @output
    @render.text
    def cpu_usage():
        cpu_percent = psutil.cpu_percent(interval=1)
        return f"CPU Usage: {cpu_percent}%"
    
    # Define output for memory usage
    @output
    @render.text
    def memory_usage():
        memory_info = psutil.virtual_memory()
        available_memory_gb = memory_info.available / (1024 ** 3)  # Convert to GB
        total_memory_gb = memory_info.total / (1024 ** 3)  # Convert to GB
        memory_percent = memory_info.percent
        return f"Memory Usage: {memory_percent}% - Available: {available_memory_gb:.2f} GB / Total: {total_memory_gb:.2f} GB"

# Create the Shiny app object
app = App(app_ui, server)

# Run the app on the default local server
if __name__ == "__main__":
    app.run()
