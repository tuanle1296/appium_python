import os
import shutil
import subprocess

# Optional file

if __name__ == '__main__':
    # check if results folder is existing then clean folder before test execution
    parent_dir = os.getcwd()
    report_dir = os.path.join(parent_dir, "allure_result_folder")
    if os.path.exists(report_dir):
        shutil.rmtree("allure_results")

    """please install allure via command brew install allure (on Mac)/scoop install allure (Windows) before run runner
    file"""

    # command to execute existing tests
    try:
        create_junit_report = subprocess.run('behave --capture -f allure_behave.formatter:AllureFormatter '
                                             '-o allure_results ./tests/features'
                                             , shell=True, check=True)
    except subprocess.CalledProcessError as e:
        pass

    # command to launch allure report via browser
    runner = subprocess.run('allure serve allure_results', shell=True, check=True)
