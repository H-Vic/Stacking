# Usage
It can be used for classification, prediction and other analysis。

# Requirements
- Python 3.8 with packages matplotlib (3.7.3), numpy (1.24.3), pandas (1.4.4), mlxtend (0.23.1), installed
- Windows 11 

# Description of Files
-**APO** project consists of the following key Python files, each serving an important role in the implementation of the APO algorithm:
1.APO.py
  This file contains the primary implementation of the APO algorithm, handling the core functionalities such as initialization, iteration processes, and fitness evaluation.
2.Functions_details.py
 This script defines essential functions used throughout the algorithm, including objective functions and fitness evaluation procedures.
3.initialization.py
  Responsible for initializing the population and parameters required by the APO algorithm, ensuring a proper setup before the main optimization begins.
4.Levy.py
  Implements the Levy flight mechanism, which enhances the exploration capabilities of the algorithm by introducing controlled random movements.
5.Main.py
  The main execution script that integrates all components of the APO algorithm, orchestrating the process flow from initialization to final result output.
  
-**Stacking Model** : this model is a two-layer integrated model. Base models consist of the AdaBoost, GTBoost, XGboost, HBGBoost, and CatBoost. The RF model is chosen as the meta-learner or the second-layer model.
- After installing the necessary python packages, users can directly run the *stacking_Model.py* python script.
  
# Instructions 
1. Download the necessary project files, including stacking_Model.py, and place them in a dedicated folder within your file system.
2. Ensure that all required Python packages and libraries are installed. These may include scikit-learn, numpy, pandas, and any others listed in your project requirements.
3. Edit any configuration files (if applicable) to match your system's settings or paths. This could include specifying the data paths or project directories within the script.
4. Run stacking_Model.py in your Python environment. The script performs model stacking using the predefined models and dataset. It can be executed directly in the Python command line. If the script takes arguments, ensure to specify the paths correctly.

e.g. **"python path_to_code/stacking_Model.py"**


