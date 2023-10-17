import os
import subprocess

# Set the Azure resource group and web app name
resource_group = "your_resource_group"
web_app = "your_web_app"
moduleName = os.environ['MODULE_STACK']
environment = os.environ['ENVIRONMENT']

# Path to the Azure configuration file
azure_config_path = f"service.{moduleName}/deploy/{environment}/az/azure-config.json"

# Check if the Azure configuration file exists
if os.path.exists(azure_config_path):
    # Copy the Azure configuration file to the working directory
    subprocess.run(["cp", azure_config_path, "."], check=True)

# Zip the Python application files
subprocess.run(["zip", "-r", "app.zip", "."], check=True)

# Set Azure App Settings using the Azure CLI
subprocess.run(["az", "webapp", "config", "appsettings", "set", "--resource-group", resource_group, "--name", web_app, "--settings", "@azure-config.json"], check=True)

# Deploy the application source code to Azure
subprocess.run(["az", "webapp", "deployment", "source", "config-zip", "--resource-group", resource_group, "--name", web_app, "--src", "app.zip", "--verbose"], check=True)
