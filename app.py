import psutil
from shiny import App, reactive, ui, render

# Define the user interface (UI)
app_ui = ui.page_fluid(
    ui.h2("CPU and Memory Usage Monitor"),
    ui.row(
        ui.column(6, ui.output_text_verbatim("cpu_usage")),
        ui.column(6, ui.output_text_verbatim("memory_usage"))
    ),
    ui.row(
        ui.column(6, ui.progress_bar("cpu_bar")),
        ui.column(6, ui.progress_bar("memory_bar"))
    ),
)

# Define the server logic
def server(input, output, session):
    @reactive.Effect
    @reactive.event(input)
    def monitor_system():
        while True:
            # Get CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Get memory information
            memory_info = psutil.virtual_memory()
            memory_percent = memory_info.percent
            available_memory_gb = memory_info.available / (1024 ** 3)

            # Update the output text and progress bars
            output.cpu_usage.set_text(f"CPU Usage: {cpu_percent}%")
            output.memory_usage.set_text(f"Memory Usage: {memory_percent}% - Available: {available_memory_gb:.2f} GB")
            
            # Update progress bars
            ui.update_progress_bar("cpu_bar", value=cpu_percent)
            ui.update_progress_bar("memory_bar", value=memory_percent)

# Create the Shiny app
app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
