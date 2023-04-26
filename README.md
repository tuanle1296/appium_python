# Appium with Python
This repo is a sample project which is created by Python using Behave BDD framework.

1. Require to install:
- Install Python (>= 3.7): https://www.python.org/
- Install Nodejs: https://nodejs.dev/en/learn/how-to-install-nodejs/
- Install Java JDK: https://www.oracle.com/cis/java/technologies/downloads/
- Install Appium: https://www.npmjs.com/package/appium/v/1.20.2
- Install IDE to code (use one of those): Pycharm CE or Pro - https://www.jetbrains.com/pycharm/download/#section=mac, VSCode - https://code.visualstudio.com/
- Install Appium Inspector (tool use to inspect locator): https://github.com/appium/appium-inspector
- Install Android Studio (to get Android Home): https://developer.android.com/studio
- Install allure report: 
  - MacOS: https://formulae.brew.sh/formula/allure
  - Windows: https://www.programsbuzz.com/article/how-install-allure-windows
2. How to set up environment:
- Set up Java Home: 
  - MacOS: 
    - If you are using bash terminal then run: echo export "JAVA_HOME=\$(/usr/libexec/java_home)" >> ~/.bash_profile
    - If you are using zsh terminal (which from MacOS Catalina or newer) then run: echo export "JAVA_HOME=\$(/usr/libexec/java_home)" >> ~/.zshrc
  - Windows:
    - https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html
- How to set up Android Home:
  - MacOS:
    - If you are using bash terminal:
      - nano ~/.bash_profile (Skip this step if already has ~/.bash_profile)
      - Add those lines into above file:
        - export ANDROID_HOME=/YOUR_PATH_TO/android-sdk
        - export PATH=$ANDROID_HOME/platform-tools:$PATH
        - export PATH=$ANDROID_HOME/tools:$PATH
        - export PATH=$ANDROID_HOME/tools/bin:$PATH
      - Then run: source ~/.bash_profile
      - Validate Path: echo $PATH
      - Confirm if everything is okay: adb devices
    - If you are using zsh terminal:
      - nano ~/.zshrc (Skip this step if already has ~/.zshrc)
      - Add those lines into above file:
        - export ANDROID_HOME=/YOUR_PATH_TO/android-sdk
        - export PATH=$ANDROID_HOME/platform-tools:$PATH
        - export PATH=$ANDROID_HOME/tools:$PATH
        - export PATH=$ANDROID_HOME/tools/bin:$PATH
      - Then run: source ~/.bash_profile
      - Validate Path: echo $PATH
      - Confirm if everything is okay: adb devices
  - Windows: 
    - https://www.programsbuzz.com/article/set-androidhome-environment-variable-windows-10
    - Confirm if everything is okay > Open CMD and type command: adb devices
- Set up Appium Inspector to connect with Android device:
  - Real device: should be enable first debug mode in Settings > developer mode
  - Simulator using Android Studio: No need to do anything
  - Plug in device into machine (real device)/ Start emulator (Android Studio)
  - Run command: adb devices
  - Get the udid from above command
  - Run command to start appium server via terminal/CMD: appium
  - Launch Appium Inspector and add following fields:
    - udid: (value is from "adb devices" command)
    - deviceName: (value is name of Android phone)
    - platformName: Android
    - automationName: UiAutomator2
    - platformVersion: (Check Android OS version and enter value here, ex: 12)
  - Save and start session
3. Run project:
- Launch IDE, open project folder then run first command to install all required libraries: pip install -r requirements.txt
- Then run following command: python3 tests/runner.py

4. Project structure:
- "src" folder: store base functions and base assertion functions which reuse through project
- "tests" folder: store feature files (inside features/clock) and steps definitions (inside steps)
- "features" folder also store environment.py file which is the Hooks of current feature files
- "runner.py" file: store command to run scripts then launch browser with allure report
