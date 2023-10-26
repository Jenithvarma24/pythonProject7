import pytest

# pytest --junit-xml=junitXMLReport.xml

if __name__ == "__main__":
    pytest.main([
        "-s", "C:/Users/jenith.ravichandran/PycharmProjects/pythonProject7/tests/test_suite.py",
        "--html=report.html"
    ])
