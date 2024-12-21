#short description of how to use the pytest command line to execute the tests created:

command line:

pytest                          - runs all the test cases
-v                              - means verbose
-s                              - prints
-m                              - executes tests marked with different names
-m "Smoke or UI"                - executes tests marked with smoke or ui markers
--mark                          - show the available markes
ctrl + c                        - break the execution (infinite loading / stuck or different issues)
-rx                             - prints the xfail message for tests marked as expected fails
-rs                             - prints the skip message for test marked as skipped
-rxs                            - prints both skipped and expected failed marked tests
-n                              - <number of browsers to open> for testing in parallel

examples:
pytest -s -v -m Smoke           - executes all the test cases / classes marked with the Smoke marker
pytest -s -v -m "Smoke or UI"   - executes all the test cases / classes marked with the Smoke and UI marker
pytest -s -v -m "not UI"        - executes all the test excluding the UI ones


examples for marking tests:

@pytest.mark.Smoke                                                       - marks test as smoke test
@pytest.mark.custom_my_name                                              - marks test with a custom name
@pytest.mark.skip                                                        - marks the test as skipped
@pytest.mark.skip(reason="this is a skipped message")                    - adds a skip message to the marked test
@pytest.mark.xfail(reason="expected fail message")                       - adds an expected fail message to the marked test


# Make sure when you use markers to put them in the pytest.ini file
# to implement automatically the css in the html report put the following command in the pytest.ini > addopts=--self-contained-html
#NOTE:
when working with DDT files / JSON makes sure to have the correct relative path set otherwise it may not run the test script itself

to make the html file responsive use this command in pytest.ini addopts = --self-contained-html
