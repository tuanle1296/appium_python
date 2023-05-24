import os
import shutil
import subprocess

if __name__ == '__main__':
    parent_dir = os.getcwd()
    report_dir = os.path.join(parent_dir, "allure_result_folder")
    try:
        os.mkdir(report_dir)
    except FileExistsError:
        shutil.rmtree("allure_result_folder")

    """please install allure via command brew install allure (on Mac)/scoop install allure (Windows) before run runner
    file"""


    try:
        create_junit_report = subprocess.run('behave -f allure_behave.formatter:AllureFormatter '
                                             '-o allure_result_folder ./tests/features'
                                             , shell=True, check=True)
    except subprocess.CalledProcessError as e:
        pass

    runner = subprocess.run('allure serve allure_result_folder', shell=True, check=True)
