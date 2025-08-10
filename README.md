# Replacing-Background-AI
The model in which will replace the images of the car and put it into your already prepared background with realistics style

The goal of the project is that you have an image of a car, you have to find the way to replace the background image of a car into the background that you wanted, but make sure the car look realistic without alternating its own details.

# Why this idea?
This idea come from the selling car business, imagine you have a business in which you will buy used car and then re-sell it. However, your customer will take the picture of their car at home, and show you, you want to post those picture of the car on to your own website but you want the car image to be in your own background with brand and logo, therefore this is where the AI will come in, it will help you to do the job of replacing background while still maintaining the state of the car.

# Installing libraries and modules: 
1. os module: https://www.geeksforgeeks.org/python/how-to-install-os-sys-module-in-python/ (you can check out this website to see instruction on how to install and example code for this module)
2. request: https://www.geeksforgeeks.org/python/how-to-install-os-sys-module-in-python/

# API key: 
First of all, API key is like the access or the password for you to work with online services like google maps, runwayml, or other AI tools, but instead of having to go online and work with it, now you can write the script for it to run locally on your computer.

Remove.bg: https://www.remove.bg/api (go to this link and get your own API key. Note: some of the API key would not be shown for the second time, so it is best to copy and save it somewhere safe for the future)

RunwayML: https://runwayml.com/api (go to this website, click get started with API, get your API key. After having access to your api key, make sure to set it up to be active. For this AI model, it will not be free to run its API, therefore you need to go to the billing and pay at least 10.00$ for 1000 credits.)


# Step by Step: 
1. You will collect the set of images of the car (check out the folder named "input")
2. Now that you have your images, the first job is to write the python script to cutout the layer of the car using Remove.bg tool, in order to run this AI locally on your computer, you will have to access to their API key
