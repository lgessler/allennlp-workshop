# Introduction

These are materials for an AllenNLP tutorial workshop to be held at Georgetown University on October 30, 2021.

# Setup

1. **Install Anaconda**: It's strongly recommended that you install Anaconda on your local machine. 
   This will make it easy for you to install the Python packages needed.
   You can download Anaconda from the [official website](https://www.anaconda.com/products/individual).
   
2. **Access a command line**: If you are on **Linux/MacOS**, open your favorite terminal emulator,
   or the app Terminal if you are on MacOS. If you are on **Windows**, open the "Anaconda Prompt" app.
   
3. **Create a new environment**: On your command line, type `conda create --name workshop python=3.9` and hit enter.
   Confirm the creation of the environment.
   If everything has gone well, you will now be able to type `conda activate workshop`. 
   You should now see `(workshop)` at the very left side of your command line prompt.

4. **Clone this repository**: Clone this repository using git to a location of your choice.
   You can do this on the command line: `git clone https://github.com/lgessler/allennlp-workshop.git`.
   Once it has been created, type `cd allennlp-workshop` and then `cd simple_classifier` to navigate 
   to the important part of the repository.
   
5. **Install dependencies**: Type `pip install -r requirements.txt` to install all required dependencies.
   This may take a while--make sure your internet connection is strong and stable.
   
6. **Confirm success**: If the previous step completed without error, confirm it works by attempting to run the code.
   If you are on **Windows**, type `allennlp train configs\base.json -s model`. 
   If you are on **MacOS/Linux**, type `allennlp train configs/base.jsonnet -s model`.
   You should see a lot of logger output, and a program should start running that will show a progress bar.
   Once you confirm that you have seen a progress bar, you may exit this process by hitting **CTRL+C**.
   
7. **Confirm notebooks work**: Now, type `jupyter lab` on the command line. 
   You should be prompted to open a new browser tab--if not, look for a URL in the output. 
   Confirm that you can run all cells in the files ending in `.ipynb` by opening them, clicking 
   "Run" in the top toolbar, and then hitting "Run All Cells". 
   Scroll up and down the file after hitting "Run All Cells"--if you do not see any red warnings, you are good to go.
