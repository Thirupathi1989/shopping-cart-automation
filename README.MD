This is a sample BDD automation framework developed on Selenium and Python Behave. github url - https://github.com/Thirupathi1989/shopping-cart-automation

Page Object Model is followed in this framework

pages folder contains the elements and corresponding actions of the pages

features folder contains steps folder which has all the test files and also the feature files.

configuration directory contains the configuration and data

drivers directory contains the chrome driver

python packages needed to run this framework
allure-behave
allure-python-commons
behave
pytest
selenium

reports directory contains the json files generated with allure reports

Comments to run the test
To run the test with allure report behave -f allure_behave.formatter:AllureFormatter -o reports/ features/

To generate the html allure report from the json files inside reports folder allure serve reports/