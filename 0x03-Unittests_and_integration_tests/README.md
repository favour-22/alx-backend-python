# UNNITEST AND INTERGRATION

## [test_utils.py](./test_utils.py)
~ Pythonn script:<br>
	~ Containing ***TestAccessNestedMap*** class that inherits from ***unittest.TestCase***.<br>
	~ Implement the ***TestAccessNestedMap.test_access_nested_map*** method to test that the method returns what it is supposed to.
	~ Decorates method with ***&parameterized.expand*** to test function forfollowing input.<br>
		<p>nested_map={"a": 1}, path=("a",)<br>
		nested_map={"a": {"b": 2}}, path=("a",)<br>
		nested_map={"a": {"b": 2}}, path=("a", "b")<p><br>
	~ Each input is tested with ***assertEqual*** to ensure the function returns the expected result.<br>
	~ Uses ***assertRaises*** context manager to test that a ***keyError*** is raised for the following inuts:<br>
		<p>nested_map={}, path=("a",)<br>
		nested_map={"a": 1}, path=("a", "b")<p><br>
	~ Define the ***TestGetJson(unittest.TestCase)*** class and implement the ***TestGetJson.test_get_json*** method to test that ***utils.get_json*** returns the expected result.
	~ Uses ***unittest.mock.patch*** to patch ***request.get***.
	~ Makes sure it returns a ***Mock*** object with a json method that returns ***test_payload*** which is paramtrized alongside ***test_url*** that will be pased to ***get_json*** with the following input:
		<p>test_url="http://example.com", test_payload={"payload": True}<br>
		test_url="http://holberton.io", test_payload={"payload": False}<p><b>
	~ Tests that output of ***get_json*** is equal to ***test_payload***
	~ Tests that the mocked ***get*** method was exactly once with ***test_url*** as argument.
	 ~ Implements ***TestMemoize(unittest.TestCase)*** class with a ***test_memoize*** method


## [test_client.py](./test_client.py)
~ Python script that:<br>
	~ Declares the ****TestGithubOrgClient(unittest.TestCase)*** class and implement the ***test_org*** method that tests if ***GithubOrgClient.org*** returns correct value.<br>
	~ ***@patch*** is used as a decorator to make sure ***get_json*** is called once with the expected argument but makes sure it is not executed.<br>
	~ ***@parameterized.expand*** is used as a decorator to parametrize the test with a couple of ***org** examples to pass to ***GithubOrgClient***.<br>
	~ Implement ***test_public_repos_url*** method to unit-test ***GithubOrgClient._public_repos_url***.
	~ Uses ***patch*** as a context manager to patch ***GithubOrgClient.org*** and make it return a known payload.<br>
	~ Test that the result of _public_repos_url is the expected one based on the mocked payload.
	~ Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.

Use @patch as a decorator to mock get_json and make it return a payload of your choice.

Use patch as a context manager to mock GithubOrgClient._public_repos_url and return a value of your choice.

Test that the list of repos is what you expect from the chosen payload.

Test that the mocked property and the mocked get_json was called once.
Implement TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.
Create the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API.

Use @parameterized_class to decorate the class and parameterize it with fixtures found in fixtures.py
The setupClass should mock requests.get to return example payloads found in the fixtures.

Use patch to start a patcher named get_patcher, and use side_effect to make sure the mock of requests.get(url).json() returns the correct fixtures for the various values of url that you anticipate to receive.

Implement the tearDownClass class method to stop the patcher.
