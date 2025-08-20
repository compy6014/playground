# IT WILL BE USED FOR SELECTING AI TOOL, NOW FOR TESTING ONLY
from scripts.specific_api import SpecificAPI
import base64
from scripts.template_formatter import Formatter
from scripts.workflow_executor import WorkflowExecutor
from utils.utility_functions import FunctionLibrary
from utils.config_loader import ConfigLoader
from datetime import datetime, timezone
import json
import re
import os,fnmatch
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

#logger = FunctionLibrary.get_module_logger('CodeQL')
# test existing API/existing environment
#github_api = SpecificAPI("graphql", environment="enterprise")

# test non existing API
#github_api = SpecificAPI("graphql_latest", environment="enterprise")
#ValueError: API 'graphql_latest' not found in api_config.json

#test non existing environment
#graphql_api = SpecificAPI("graphql", environment="staging")
#ValueError: Environment 'staging' not found for API 'graphql_new'

#query_file/method/filter/header_type
#graphql_api = SpecificAPI("graphql", environment="enterprise")
#response = graphql_api.make_request("check_pr_merge_status", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", pr_number=160)
#print(response)

#with query/no method/no filter/no header_type
#response = graphql_api.make_request("test_query", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", pr_number=160)


#github_api = SpecificAPI("github", environment="enterprise")
github_api = SpecificAPI("github", environment="emu")

#test get_code_scanning_results - OK
#response = github_api.make_request("get_code_scanning_results", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch="amd/stg/pal", state="open")

#test get_code_scanning_alert - OK
#response = github_api.make_request("get_code_scanning_alert", repo_name="dal", repo_owner="AMD-Radeon-Driver", alert_number=1435)

#test get_file_path_and_base_sha - OK
#response = github_api.make_request("get_file_path_and_base_sha", repo_name="pal", repo_owner="AMD-Radeon-Driver", alert_number=6042)

#test get_file_content - OK
#response = github_api.make_request("get_file_content", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch_sha="d739c826b61d38a934995c4136bfb5b9a52b9200", file_path="src/util/win/winSysUtil.cpp")
#file_content = base64.b64decode(response['content']).decode()
#print("File content:")
#print(file_content)

#test post filter - OK
#response = github_api.make_request("filter_code_scanning_results", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch="amd/stg/pal", state="open")

#test post filter with params - OK
#response = github_api.make_request("filter_test_code_scanning_results", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch="amd/stg/pal", state="open", start_date="2025-03-18T00:00:00Z", end_date="2025-03-18T23:59:59Z")

#test multifilter/date_range start-end - OK
#response = github_api.make_request("test_multifilter_code_scanning_results", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch="amd/stg/pal", state="open", start_date="2025-03-14T00:00:00Z", end_date="2025-03-18T23:59:59Z", severity="note")
# rules = "cpp/comparison-with-wider-type,cpp/memory-may-not-be-freed,cpp/memory-never-freed,cpp/missing-null-test,cpp/inconsistent-null-check,cpp/inconsistent-nullness-testing"
# rules = [rule.strip() for rule in rules.split(',')]
#print(rules)
#response = github_api.make_request("test_multifilter_code_scanning_results", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch="amd-dal", state="open", rules=rules, from_date="2025-03-18T00:00:00Z")
#response = github_api.make_request("test_multifilter_code_scanning_results", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch="amd-dal", state="open", from_date="2025-03-18T00:00:00Z", rules=None)

#test multifilter/date_range start only - OK
# from/to - OK (2 alerts)
#response = github_api.make_request("get_code_scanning_results", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch="amd-dal", state="open", from_date="2025-03-15T00:00:00Z")
# from only - OK (4 alerts)
#response = github_api.make_request("get_code_scanning_results", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch="amd/stg/pal", state="open", from_date="2025-03-18T00:00:00Z", severity="note")
# to only - OK
#response = github_api.make_request("get_code_scanning_results", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch="amd/stg/pal", state="open", to_date="2023-12-31T23:59:59Z", severity="note")
# empty to - OK (4 alerts)
#response = github_api.make_request("get_code_scanning_results", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch="amd/stg/pal", state="open", from_date="2025-03-18T00:00:00Z", to_date="", severity="note")
# empty from - OK
#response = github_api.make_request("get_code_scanning_results", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch="amd/stg/pal", state="open", from_date="", to_date="2023-12-31T23:59:59Z", severity="note")

#test filter match_mode - OK
#response = github_api.make_request("test_multifilter_code_scanning_results", repo_name="pal", repo_owner="AMD-Radeon-Driver", branch="amd/stg/pal", state="open", start_date="2025-03-14T00:00:00Z", end_date="2025-03-18T23:59:59Z", severity="note", match_mode=True)

#test get_last_commiter - OK
#response = github_api.make_request("get_last_committer", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", branch="main", file_path="/.github/workflows/coverity_trigger_test.yml")
#response = github_api.make_request("get_last_committer", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", branch="main", file_path="requirements.txt")

# test check_existing_labels - OK
#response = github_api.make_request("check_existing_labels", repo_name="AICodeReview", repo_owner="AMD-SW-Infra")

#test add_labels_to_pr - OK
#curl -X POST -H "Authorization: Bearer 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" 
# -H "Accept: 'application/vnd.github.v3+json" -d '["bug","enhancement"]' https://github.amd.com/api/v3/repos/AMD-SW-Infra/AICodeReview/issues/160/labels
#RuntimeError: API request failed: 422 Client Error: Unprocessable Entity for url: https://github.amd.com/api/v3/repos/AMD-SW-Infra/AICodeReview/issues/160/labels
#response = github_api.make_request("add_labels_to_pr", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", pr_number=160, labels=["bug","enhancement"])
#response = github_api.make_request("add_labels_to_pr", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", pr_number=160, labels=["test_label"])

# test get_list_of_reviewers - OK (requested_reviewers)
#curl -X POST -H "Authorization: Bearer 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" -H "Accept: 'application/vnd.github.v3+json" https://github.amd.com/api/v3/repos/AMD-SW-Infra/AICodeReview/pulls/160/reviews
#"requested_reviewers":[] from API
#response = github_api.make_request("get_list_of_reviewers", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", pr_number=223)
#response = github_api.make_request("get_list_of_reviewers", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", pr_number=160)

#test add_reviewers_to_pr - OK
#curl -X POST -H "Authorization: Bearer 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" -H "Accept: application/vnd.github.v3+json" -d '{"reviewers": ["imirosav", "vlaantic"]}' https:///github.amd.com/api/v3/repos/AMD-SW-Infra/AICodeReview/pulls/160/requested_reviewers 
#response = github_api.make_request("add_reviewers_to_pr", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", pr_number=160, reviewers=["imirosav"])

#test asign_users_to_pr - OK
#response = github_api.make_request("assign_user_to_pr", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", pr_number=160, assignees=["imirosav"])
#print(response)

#test get_latest_commit_sha - OK
#response = github_api.make_request("get_latest_commit_sha", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", base_branch="test_branch")

#test check_existing_branch - OK
#response = github_api.make_request("check_existing_branch", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", branch_name="testing_branch")


####FIX IT!!!!!
#test delete_existing_branch - Deletes but throws 422 error
#curl -X DELETE -H "Authorization: Bearer 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" -H "Accept: application/vnd.github.v3+json" https://github.amd.com/api/v3/repos/AMD-SW-Infra/AICodeReview/git/refs/heads/test_branch2
#response = github_api.make_request("delete_existing_branch", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", branch_name="testing_branch")
# try:
#     response = github_api.make_request("delete_existing_branch", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", branch_name="testing_branch")
#     print(f"Branch deleted")
# except RuntimeError as e:
#     if "422" in str(e):
#         print("Delete happened but 422 throwed")
#     else:
#         raise
#response = github_api.make_request("delete_existing_branch", repo_name="AMD-Radeon-Driver", repo_owner="dal", branch_name="amd/dev/swjenci/SWDEV-5/codeql-fix-1435")
#https://github.amd.com/AMD-Radeon-Driver/dal/tree/amd/dev/swjenci/SWDEV-5/codeql-fix-1435
#curl -X DELETE -H "Authorization: Bearer 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" -H "Accept: application/vnd.github.v3+json" https://github.amd.com/api/v3/repos/AMD-Radeon-Driver/dal/git/refs/heads/amd/dev/swjenci/SWDEV-5/codeql-fix-1435


#test create_branch - OK
#response2 = github_api.make_request("create_branch", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", ref="refs/heads/testing_branch", sha=response)

#test check_file_sha - OK
#response = github_api.make_request("check_file_sha", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", new_branch="test_branch", file_path="queries/issues.json")
#response = github_api.make_request("check_file_sha", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", new_branch="test_branch", file_path="queries/new_test_file.txt")

#test create_new_file - OK
#file_content = "This is only a test, new file creation"
#encoded_content = base64.b64encode(file_content.encode()).decode()
#response = github_api.make_request("create_new_file", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", file_path="queries/new_test_file.txt", message="New create file test", content=encoded_content, branch="test_branch")

#test update_existing_file - Ok
#file_content = "This is only a test, new file creation"
#file_content = "This is only a test, new file creation.File update test"
#encoded_content = base64.b64encode(file_content.encode()).decode()
#response2 = github_api.make_request("update_existing_file", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", file_path="queries/new_test_file.txt", message="Update file new test", content=encoded_content, branch="test_branch", sha=response)

#test create_pull_request - OK
#response = github_api.make_request("create_pull_request", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", title="Test PR via template", body="This is created via template", head="test_branch", base="main", draft=True)
#response = github_api.make_request("create_pull_request", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", title="Test PR via template", body="This is created via template", head="test_branch2", base="main", draft=False)

#test get_user_details
#curl -X GET -H "Authorization: Bearer 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" -H "Accept: 'application/vnd.github.v3+json" https://github.amd.com/api/v3/user
#response = github_api.make_request("get_user_details")


#response = github_api.make_request("get_code_scanning_results", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch="amd-dal", state="")

# get all alert instances - OK
#response = github_api.make_request("get_code_scanning_alert_instances", repo_name="drivers", repo_owner="AMD-Radeon-Driver", alert_number=765)

#print("API response message:")
#print(response)

#response = github_api.make_request("get_code_scanning_results", repo_name="drivers", repo_owner="AMD-Radeon-Driver", state="open")
#print("API response message:")
#print(response)
# get all alerts from repo
#response = github_api.make_request("get_code_scanning_all_ids", repo_name="dal", repo_owner="AMD-Radeon-Driver", state="open")

# get commit by id
#response = github_api.make_request("get_commit_by_id", repo_name="ai-pr-platform", repo_owner="SW-Infra-EMU", commit_id="1124c24f9d6a8de3e3d1f7f4324f6c3325a2b3c3")

coverity_server_api = SpecificAPI("coverity_server", environment="prod")
 
# $env:COVERITY_SERVER_PASS = 'jdakX*%adobwi_w'

# get list of columns - OK
#response = coverity_server_api.make_request("list_columns")

# get issues - 
#curl -X POST -u a1_code_gen:jdakX*%adobwi_w -H 'Content-Type: application/json' --data-raw '{"filters": [{"columnKey": "project","matchMode": "oneOrMoreMatch","matchers": [{"class": "Project","name": "AGESA V10 FW PFO","type": "nameMatcher"}]}],"columns": ["cid","displayType","displayFile","firstDetected","status","severity","action","classification"]}' -L "http://coverity.amd.com:8080/api/v2/issues/search?includeColumnLabels=true&locale=en_us&offset=0&queryType=bySnapshot&rowCount=200&sortOrder=asc"
#response = coverity_server_api.make_request("get_issues", filters=[[{"columnKey": "project","matchMode": "oneOrMoreMatch","matchers": [{"class": "Project","name": "AGESA V10 FW PFO","type": "nameMatcher"}]}]], columns=["cid","displayType","displayFile","firstDetected","status","severity","action","classification"])
#response = coverity_server_api.make_request("get_issues", filters=[[{"columnKey": "project","matchMode": "oneOrMoreMatch","matchers": [{"class": "Project","name": "AGESA V10 FW PFO","type": "nameMatcher"}]}]], columns=["cid"])
#response = coverity_server_api.make_request("coverity_search_issues")

# OK
# response = coverity_server_api.make_request(
#     "get_issues",
#     filters=[
#         {
#             "columnKey": "project",
#             "matchMode": "oneOrMoreMatch",
#             "matchers": [
#                 {
#                     "class": "Project",
#                     "name": "AGESA V10 FW PFO",
#                     "type": "nameMatcher"
#                 }
#             ]
#         }
#     ],
#     columns=[
#         "cid",
#         "displayType",
#         "displayFile",
#         "firstDetected",
#         "status",
#         "severity",
#         "action",
#         "classification"
#     ]
# )

# OK
# project_name = "AGESA V10 FW PFO"
# filters = [
#     {
#         "columnKey": "project",
#         "matchMode": "oneOrMoreMatch",
#         "matchers": [
#             {
#                 "class": "Project",
#                 "name": project_name,
#                 "type": "nameMatcher"
#             }
#         ]
#     }
# ]
# response = coverity_server_api.make_request(
#     "get_issues",
#     filters=filters,
#     columns=[
#         "cid",
#         "displayType",
#         "displayFile",
#         "firstDetected",
#         "status",
#         "severity",
#         "action",
#         "classification"
#     ]
# )
project_name = "AGESA V10 FW PFO"
cid = "5996791"

# response = coverity_server_api.make_request("get_all_projects", project_name=project_name)
# print("API response message:")
# print(response)


# filters = [
#     {
#         "columnKey": "project",
#         "matchMode": "oneOrMoreMatch",
#         "matchers": [
#             {
#                 "class": "Project",
#                 "name": project_name,
#                 "type": "nameMatcher"
#             }
#         ]
#     },
#     {
#         "columnKey": "cid",
#         "matchMode": "exactMatch",
#         "value": str(cid)
#     }
# ]
# response = coverity_server_api.make_request(
#     "get_issues",
#     filters=filters,
#     columns=[
#         "cid",
#         "displayType",
#         "displayFile",
#         "firstDetected",
#         "status",
#         "severity",
#         "action",
#         "classification"
#     ]
# )

# print("API response message:")
# print(response)


#FORMATTER TEST
#formatter = Formatter("github_templates")
#formatted = Formatter("github_templates").format("issue_comment",title="New Feature", body="Added support for X", status="Pending")
#formatted = Formatter("email_templates").format("delivery_email",subject="New Feature", body="Added support for X", sender="Pera", recipient="Marko")
#formatted = Formatter("codeql_option_2", team_name="team_1").format("generate_branch_name", alert_number="ALRT_00023", ticket_id="ID_001_test", rule_header="CustomRuleTest")
#formatted = Formatter("codeql_option_2", team_name="default").format("generate_commit_header", alert_number="ALRT_00023", ticket_id="ID_001_test", rule_header="CustomRuleTest")
#test external
#formatted = Formatter("codeql_option_2", team_name="team_3").format("generate_commit_header", alert_number="ALRT_00023", ticket_id="ID_001_test", rule_header="CustomRuleTest")
#
# team_name = "demo"
# formatter_context = {
#     "owner": "AMD-SW-Infra",
#     "repo": "AICodeReview",
#     "branch": "test_branch",
#     "date_sentence": "22-23.03.2025", 
#     "detected_fp_section": "List of detected FPs", 
#     "created_prs_section": "List of created PRs"
# }
# formatter = Formatter("codeql_templates", team_name, formatter_context)
# formatted = formatter.format("email_body")
# #print(formatted)

# label_list = formatter.format("label_list")
# logger.info("LABEL LIST")
# logger.info(label_list)
# reviewer_list = formatter.format("reviewer_list")
# logger.info("REVIEWER LIST")
# logger.info(reviewer_list)

# if '#last_committer' in reviewer_list:
#     last_committer = "someone"
#     if last_committer:
#         # Replace the placeholder with the actual committer's username
#         reviewer_list = reviewer_list.replace('#last_committer', last_committer)
#         print(f"Replaced '#last_committer' in reviewers list with {last_committer}.")
#         print(f"Updated reviewer_list: {reviewer_list}")
#     else:
#         # If no committer is found, remove the placeholder
#         reviewer_list = reviewer_list.replace('#last_committer', '')
#         print(f"Updated reviewer_list: {reviewer_list}")
#     #add_reviewer = github_api.make_request("add_reviewers_to_pr", repo_name=repo, repo_owner=owner, pr_number=pr_number, reviewers=reviewer_list)
#     print(f"Adding reviewers {reviewer_list} to PR: #")

# ERRORHANDLER TEST
#test = ErrorHandler("")


# WORKFLOW EXECUTOR TEST
#executor = WorkflowExecutor("test_workflow", "default")
#executor.execute(input_var="AAAAA")
#executor = WorkflowExecutor("test_workflow", "team_1")
#executor.execute(input_var="BBBBB")

#executor = WorkflowExecutor(workflow_name="test_workflow_structure", team_name="team_1")
#executor.execute()

#test context
# context = {
#     "var_1": 'context_var_1_value',
#     "var_2": "context_var_2_value",
#     "var_3": 123,
#     "var_4": True,
#     "var_5": 'context_var_5_value'
# }
# executor = WorkflowExecutor("test_workflow_structure_imports", "team_2")
# executor.execute(context)

# test codeql_fix - OK
#OK
#curl -X POST 'http://mkdcvllmapp09.amd.com:8000/fix_from_alert_num?alert_num=1435&include_explanation=true&github_instance=on-prem&owner=AMD-Radeon-Driver&repo_name=dal&detect_fp=true&pr_platform=true' -H 'x-api-key: d091642z7483910264758'
#OK
#curl -X POST -H 'x-api-key: d091642z7483910264758' 'http://mkdcvllmapp09.amd.com:8000/fix_from_alert_num?alert_num=1435&include_explanation=true&github_instance=on-prem&owner=AMD-Radeon-Driver&repo_name=dal&detect_fp=true&pr_platform=true'
#codeql_api = SpecificAPI("codeql", environment="prod")
#codeql_api = SpecificAPI("codeql", environment="dev")
#fix = codeql_api.make_request("codeql_fix", alert_num=1435, include_explanation=True, github_instance="on-prem", owner="AMD-Radeon-Driver", repo_name="dal", detect_fp=True, pr_platform=True)
#print(fix)
#http://mkdcvllmapp09.amd.com:8000/fix_from_alert_num
#{'x-api-key': 'd091642z7483910264758'}
#{'alert_num': 1435, 'include_explanation': True, 'github_instance': 'on-prem', 'owner': 'AMD-Radeon-Driver', 'repo_name': 'dal', 'detect_fp': True, 'pr_platform': True}
#RuntimeError: API request failed: 422 Client Error: Unprocessable Entity for url: http://mkdcvllmapp09.amd.com:8000/fix_from_alert_num

#https://github.amd.com/api/v3/repos/AMD-Radeon-Driver/pal/code-scanning/alerts/6042
#{'Authorization': 'Bearer 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', 'Accept': 'application/vnd.github.v3+json'}
#


####DEMO
# context = {
#     "alert_numbers": [1435, 1440, 1441],
#     "owner": "AMD-Radeon-Driver",
#     "repo": "dal",
#     "git_environment": "enterprise",
#     "branch": "amd-dal",
#     "state": "open",
#     "codeql_environment": "dev",
#     "include_explanation": True,
#     "detect_fp": True,
#     "pr_platform": True,
#     "branch_delete": False,
#     "draft_pr": True,
#     "team_name": "demo"
# }
# executor = WorkflowExecutor(workflow_name="demo_codeql", team_name="demo")
# executor.execute(context)

#"endpoint": "/repos/{owner}/{repo}/code-scanning/alerts?ref={branch}&per_page=200&state={state}&sort=created&order=desc"

rules = "cpp/comparison-with-wider-type,cpp/memory-may-not-be-freed,cpp/memory-never-freed,cpp/missing-null-test,cpp/inconsistent-null-check,cpp/inconsistent-nullness-testing"
#rules = "cpp/memory-may-not-be-freed"
rules = [rule.strip() for rule in rules.split(',')]

alert_numbers = [1435]
owner = "AMD-Radeon-Driver"
repo = "dal"
git_environment = "emu"
branch = "amd-dal"
state = ""
from_date = "2024-04-16T00:00:00Z"
to_date = "2024-04-16T23:59:59Z"
#from_date = ""
#to_date =""
include_explanation = True
detect_fp = True
pr_platform = True
codeql_environment = "dev"
team_name = "demo"
branch_delete = False
draft_pr = True

#from_date = globals().get('from_date', None)
#to_date = globals().get('to_date', None)
#get alerts in last 24h
#response = github_api.make_request("get_code_scanning_results", repo_name=repo, repo_owner=owner, branch=branch, state=state, rules=rules, from_date=from_date, to_date=to_date, page=1)
#response = github_api.make_request("get_code_scanning_results", repo_name=repo, repo_owner=owner, branch=branch, state=state, rules=rules, from_date=from_date, to_date=to_date)
#response = github_api.make_request("get_code_scanning_alert", repo_name=repo, repo_owner=owner, alert_number=alert_numbers)
#response = github_api.make_request("get_code_scanning_results", custom_endpoint="/repos/AMD-Radeon-Driver/dal/code-scanning/alerts?ref=amd-dal&per_page=100&state=&sort=created&order=desc&page=2", repo_name=repo, repo_owner=owner, branch=branch, state=state, rules=rules, from_date=from_date, to_date=to_date)
#response = github_api.make_request("get_code_scanning_all", repo_name=repo, repo_owner=owner, branch=branch, state=state)

# github_api.make_request(  
#         "get_code_scanning_results",  
#         repo_name=repo,  
#         repo_owner=owner,  
#         branch=branch,  
#         state=state,  
#         rules=rules,  
#         from_date=from_date,  
#         to_date=to_date  
#     ) 


def multi_page_alert_response(request_name, repo_name, repo_owner, branch, state):
    alerts= []
    page = 1
    while True:
        response = github_api.make_request(request_name, repo_name=repo_name, repo_owner=repo_owner, branch=branch, state=state, page=page)
        if not response:
            break 
        alerts.extend(response)
        page +=1
    return alerts

#response = multi_page_alert_response("get_code_scanning_results", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch="amd-dal", state="")


# print("API response message:")
# print(response)


# def paginated_request(api_name, request_name, execution_params):    
#     # Load the request template using ConfigLoader    
#     request_template = ConfigLoader.load_request_template("github", request_name)    
    
#     alerts = []    
#     page = 1    
    
#     while True:    
#         # Extract the endpoint from the template  
#         endpoint = request_template['endpoint']    
            
#         # Create a combined dictionary of variables from the template and execution_params    
#         combined_params = {**request_template['variables'], 'page': str(page)}    
    
#         # Replace placeholders in the endpoint using values from combined_params first  
#         for key, value in combined_params.items():    
#             # Convert list to string if needed    
#             if isinstance(value, list):    
#                 value = ','.join(value)  # Adjust this if a different formatting is required    
  
#             # Replace placeholders with the actual values  
#             endpoint = endpoint.replace(f"{{{key}}}", value)    
    
#         # Now add logic to handle other placeholders from execution_params    
#         for key, value in execution_params.items():    
#             if isinstance(value, list):    
#                 value = ','.join(value)  # Adjust this if necessary    
  
#             # Replace execution parameters in the endpoint  
#             endpoint = endpoint.replace(f"{{{key}}}", value)    
    
#         # Append the page parameter directly to the endpoint in the query string  
#         if "&page={page}" not in endpoint:  
#             endpoint += f"&page={page}"  # Add the page number only when it's not already there  
  
#         # Log the endpoint with execution parameters before the request    
#         print(f"Final endpoint (page {page}): {endpoint}")    
    
#         # Make the API request with the constructed endpoint    
#         response = api_name.make_request(request_name, endpoint, execution_params) 
    
#         if not response:  # Stop if no response or empty response    
#             break     
            
#         alerts.extend(response)    
#         page += 1  # Increment page for the next iteration    
    
#     return alerts    

def paginated_request(api_name, request_type, request_name, execution_params):      
    # Load the request template using ConfigLoader      
    request_template = ConfigLoader.load_request_template(request_type, request_name)      
      
    alerts = []      
    page = 1      
      
    while True:      
        # Extract the endpoint from the template    
        endpoint = request_template['endpoint']      
              
        # Create a combined dictionary of variables from the template and execution_params      
        combined_params = {**request_template['variables'], 'page': str(page)}      
      
        # Replace placeholders in the endpoint using values from combined_params first    
        for key, value in combined_params.items():      
            # Convert list to string if needed      
            if isinstance(value, list):      
                value = ','.join(map(str, value))  # Adjust this if a different formatting is required      
    
            # Replace placeholders with the actual values    
            endpoint = endpoint.replace(f"{{{key}}}", str(value))      
      
        # Now add logic to handle other placeholders from execution_params      
        for key, value in execution_params.items():      
            if isinstance(value, list):      
                value = ','.join(map(str, value))  # Adjust if necessary      
    
            # Replace execution parameters in the endpoint    
            endpoint = endpoint.replace(f"{{{key}}}", str(value))      
      
        # Append the page parameter directly to the endpoint in the query string    
        if "&page={page}" not in endpoint:    
            endpoint += f"&page={page}"  # Add the page number only when it's not already there    
    
        # Log the endpoint with execution parameters before the request      
        print(f"Final endpoint (page {page}): {endpoint}")      
      
        # Make the API request with the constructed endpoint  
        # Pass the custom endpoint and all execution parameters to make_request  
        response = api_name.make_request(  
            request_name,   
            custom_endpoint=endpoint,  # Pass as named parameter  
            **execution_params  # Unpack execution_params as keyword arguments  
        )  
      
        if not response:  # Stop if no response or empty response      
            break       
              
        alerts.extend(response)      
        page += 1  # Increment page for the next iteration      
      
    return alerts  


execution_params = {
        "repo_name":"dal", 
        "repo_owner":"AMD-Radeon-Driver",
        "branch":"amd-dal",
        "state":"",
        "rules":rules,
        #"rules":"cpp/comparison-with-wider-type,cpp/memory-may-not-be-freed,cpp/memory-never-freed,cpp/missing-null-test,cpp/inconsistent-null-check,cpp/inconsistent-nullness-testing", 
        "from_date":"2025-07-09T00:00:00Z",
        "to_date":"2025-07-10T23:59:59Z"
    }

#response = paginated_request(api_name=github_api, request_type="github", request_name="get_code_scanning_results", execution_params=execution_params)
#response = paginated_request(github_api, "get_code_scanning_results", repo_name=repo, repo_owner=owner, branch=branch, state=state, rules=rules, from_date=from_date, to_date=to_date)
# response = paginated_request(  
#         github_api,
#         "get_code_scanning_results",  
#         repo_name=repo,  
#         repo_owner=owner,  
#         branch=branch,  
#         state=state,  
#         rules=rules,  
#         from_date=from_date,  
#         to_date=to_date  
#     )
#print("API response message:")
#print(response)



#dev novi codeql
#bb97be0b686a4bc7b8ca39ce15e9399a

#Email sender: AI-CodeReview<a1.atgmerosa+GerritVerifier@amd.com>




#test send_email - OK
#email = FunctionLibrary.send_email("atlsmtp10.amd.com", 25, "vladan.antic@nesto.com", "Testing Email send", formatted, "igor.mirosavljevic@amd.com")

#from_date = "2025-03-18T00:00:00Z"
#to_date = "2025-03-20T00:00:00Z"
#from_date = ""
#to_date = ""

# from_date = globals().get('from_date', None)
# to_date = globals().get('to_date', None)
# if from_date and to_date:
#     print(f"Fetching alerts from owner/repo, from {from_date} to {to_date}")
# elif from_date:
#     print(f"Fetching alerts from {from_date} to now {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}")
# elif to_date:
#     print(f"Fetching alerts up to {to_date}")
# else:
#     print("No date range specified")
    


# formatter.update_context({"signoff_user": "Test_user", "signoff_email": "test@test.com"})
# sign_off_message = formatter.format("sign_off_message")
# if sign_off_message:
#     print(sign_off_message)
# else:
#     print("Signoff skipped")

# label_list = "demo, skip-ci"
# label_list = [label.strip() for label in label_list.split(',')]
# print(label_list)

# reviewer_list = "imirosav, vlaantic"
# reviewer_list = [reviewer.strip() for reviewer in reviewer_list.split(',')]
# print(reviewer_list)

# removed from 
#"sign_off_message": "Signed-off-by: {signoff_user} <{signoff_email}>",

#NEW FORMATTER TEST (TEAM ORIENTED TEMPLATES)
# alrt= "ALRT_001"
# owner = "my_org"
# repo = "my_repo"
# formatter_context = {
#     "alert_number": alrt,
#     "owner": owner,
#     "repo": repo
# }
# f = Formatter("codeql_templates", team_name="demo_external", context=formatter_context)

# ticket_id = f.format("ticket_id")
# branch = f.format("base_branch")
# #detect_fp = f.format("detect_fp")
# print(ticket_id)
# print(branch)
# f.update_context({"ticket_id": ticket_id, "branch": branch})

# print(f.format("generate_branch_name"))
# #fallback to default "amd/dev/swjenci/{ticket_id}/codeql-fix-{alert_number}"
# #output "amd/dev/swjenci/SWDEV-522354/codeql-fix-ALRT_001" - OK

# print(f.format("email_subject"))
# #fallback to default "CodeQL Fix Summary for {owner}/{repo} branch {branch}"
# #output "CodeQL Fix Summary for my_org/my_repo branch amd/stg/kmd" - OK

# print(f.format("email_recipients"))
# #output "dl.CodeQLFixGenPilotKMD, matthieu.chanchee@amd.com, vladan.antic@amd.com" - OK

# print(f.format("detect_fp"))
# print(f.format("rules"))



#'path': 'windows_dm/dal3/WindowsDM.cpp',
#'start_line': 25529,

# git clone https://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@github.amd.com/AMD-Radeon-Driver/dal.git
# cd dal
# git checkout amd-dal
# git blame -L 25529,25529 windows_dm/dal3/WindowsDM.cpp 



#GIT BLAME NOT POSSIBLE VIA REST API
#BLAME on specific lines in alert

# blame = FunctionLibrary.get_last_modifier(repo_path=r"C:\GIT\TESTING\dal", file_path="windows_dm/dal3/WindowsDM.cpp", line_number=25529)
# #Jenkins, Sw
# blame = FunctionLibrary.get_last_modifier(repo_path=r"C:\GIT\TESTING\dal", file_path="dc/resource/dcn42/dcn42_resource.c", line_number=1130)
# #Siemek, Tomasz
# blame = FunctionLibrary.get_last_modifier(repo_path=r"C:\GIT\TESTING\dal", file_path="dc/resource/dcn42/dcn42_resource.c", line_number=1131)
# #Dmytro
# blame = FunctionLibrary.get_last_modifier(repo_path=r"C:\GIT\TESTING\dal", file_path="windows_dm/DalWDDM/DalWDDM_Private.cpp", line_number=5294)
# #Michael Ruan
# blame = FunctionLibrary.get_last_modifier(repo_path=r"C:\GIT\TESTING\dal", file_path="dc/hwss/dcn314/dcn314_hwseq.c", line_number=155)
# #Hogyun Lim
# blame = FunctionLibrary.get_last_modifier(repo_path=r"C:\GIT\TESTING\dal", file_path="dc/hwss/dcn314/dcn314_hwseq.c", line_number=100)
# print(blame)



# GRAPHQL BLAME
graphql_api = SpecificAPI("graphql", environment="enterprise")
# all - OK, response_filter - OK
#response = graphql_api.make_request("blame", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch_name="amd-dal", file_path="dc/hwss/dcn314/dcn314_hwseq.c")
# post_filter -
#response = graphql_api.make_request("blame", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch_name="amd-dal", file_path="dc/hwss/dcn314/dcn314_hwseq.c", email="Paul.Hsieh@amd.com")
#response = graphql_api.make_request("blame", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch_name="amd-dal", file_path="dc/hwss/dcn314/dcn314_hwseq.c", start_line=103)

#blame_data = response['data']['repository']['ref']['target']['blame']['ranges']
#line_to_check = 105


# blame = FunctionLibrary.blame_for_line(blame_data, line_to_check)
# if blame:
#     author = blame['commit']['author']
#     print(f"Line {line_to_check} was last modifed by {author['name']} ({author.get('user', {}).get('login')})")
#     print(f"Line {line_to_check} was last modifed by {author.get('user', {}).get('login')}")
# else:
#     print(f"No blame information found for line {line_to_check}")
# git_blame = True
# service_accounts = "swjenci, hsiehp"
# # service_accounts = {s.strip() for s in service_accounts.split(", ") if s.strip()}
# # print(f"Service accounts: {service_accounts}")
# fallback_list = "dev_a, dev_b"
# # fallback_list = {s.strip() for s in fallback_list.split(", ") if s.strip()}
# start_line = 100
# end_line = 106

# if git_blame is True:
#     response = graphql_api.make_request("blame", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch_name="amd-dal", file_path="dc/hwss/dcn314/dcn314_hwseq.c")
#     blame_data = response['data']['repository']['ref']['target']['blame']['ranges']
#     blame_list = FunctionLibrary.blame_for_lines(blame_data, start_line, end_line)
#     blame_list = [r.strip() for r in blame_list.split(", ") if r.strip()]
#     filtered_list = [r for r in blame_list if r not in service_accounts]
#     if filtered_list:
#         final_list = filtered_list
#     else:
#         last_file_mod = github_api.make_request("get_last_committer", repo_name="dal", repo_owner="AMD-Radeon-Driver", branch="amd-dal", file_path="dc/hwss/dcn314/dcn314_hwseq.c")[0]
#         if last_file_mod and last_file_mod not in service_accounts:
#             final_list = last_file_mod
#         else:
#             final_list = fallback_list
#     #response = github_api.make_request("add_reviewers_to_pr", repo_name="AICodeReview", repo_owner="AMD-SW-Infra", pr_number=160, reviewers=final_list)
#     print(f"Assign {final_list} to reviewers")


# print("API response message:")
#print(response)

#get teams
#curl -X GET -H "Authorization: Bearer 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" -H "Accept: 'application/vnd.github.v3+json" https://github.amd.com/api/v3/orgs/AMD-Radeon-Driver/teams
#add group to reviewers
# curl -X POST -H "Authorization: Bearer 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" -H "Accept: application/vnd.github.v3+json" -d '{"team_reviewers": ["AMD-GOQDIAGS/dl-diag_tng_codegen_reviewers"]}' https:///github.amd.com/api/v3/repos/AMD-SW-Infra/AICodeReview/pulls/160/requested_reviewers
# {
#   "message": "Reviews may only be requested from collaborators. One or more of the teams you specified is not a collaborator of the AMD-SW-Infra/AICodeReview repository.",
#   "documentation_url": "https://docs.github.com/enterprise-server@3.12/rest/pulls/review-requests#request-reviewers-for-a-pull-request"
# }



#"response_filter": ["data.repository.ref.target.blame.ranges.commit.author.user.login", "data.repository.ref.target.blame.ranges.startingLine"]

            # "post_filter": [
            #     {
            #         "type": "value_match",
            #         "field": "data.repository.ref.target.blame.ranges.commit.author.email",
            #         "param_name": "email"
            #     }
            # ]

# # Parse the JSON alert data  
# alert = json.loads(alert_data)  
  
# # Extract the necessary information  
# # Dynamically extracting the owner from the url field  
# owner = alert['html_url'].split('/')[3]  # Owner is at index 3 of the URL  
# repo = alert['html_url'].split('/')[4]  # Extract repo from URL  
# branch = alert['most_recent_instance']['ref'].split('/')[-1]  # Extract branch from ref  
# file_path = alert['most_recent_instance']['location']['path']  # File path  
# start_line = alert['most_recent_instance']['location']['start_line']  # Start line  
  
# # Output the extracted information  
# print(f"Owner: {owner}")  
# print(f"Repo: {repo}")  
# print(f"Branch: {branch}")  
# print(f"File Path: {file_path}")  
# print(f"Start Line: {start_line}") 

#get PR details
#curl -X GET -H "Authorization: Bearer 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" -H "Accept: 'application/vnd.github.v3+json" https://github.amd.com/api/v3/repos/AMD-Radeon-Driver/dal/pulls/22031


# ##OPEN QUESTIONS:

# #logs - what to do with them?



#   {
#     "name": "dl.ai_code_review",
#     "id": 2307,
#     "node_id": "MDQ6VGVhbTIzMDc=",
#     "slug": "dl-ai_code_review",
#     "description": "Based on dl.ai_code_review",
#     "privacy": "closed",
#     "notification_setting": "notifications_enabled",
#     "url": "https://github.amd.com/api/v3/organizations/7061/team/2307",
#     "html_url": "https://github.amd.com/orgs/AMD-SW-Infra/teams/dl-ai_code_review",
#     "members_url": "https://github.amd.com/api/v3/organizations/7061/team/2307/members{/member}",
#     "repositories_url": "https://github.amd.com/api/v3/organizations/7061/team/2307/repos",
#     "permission": "pull",
#     "ldap_dn": "CN=dl.ai_code_review,OU=Groups/DLs,DC=amd,DC=com",
#     "parent": null
#   },


# aicg_request = [
#         {
#             "org": repo_name.split("/")[0],
#             "commitId": "Unknown", # For Coverity/CodeQL this will be from PR_Platform
#             "pullRequestId": "Unknown", # from PR_Platform
#             "fileName": file_path.split("/")[-1],
#             "filePath": file_path,
#             "aiCode": [
#                 code_change
#             ],
#             "sourceApplication": source_application,
#             "promptExcerpt": "string",
#             "promptTokens": prompt_tokens,
#             "suffixTokens": 0,
#             # "userId": "Unknown", # not required
#             "requestId": request_id,
#             "details": {
#                 "requestURL": source_application,
#                 "language": EXTENSION_TO_LANGUAGE.get(file_path.split(".")[-1], "Unknown"),
#                 "editor": "Unknown",
#                 "plugin": "Unknown",
#                 "model": model,
#                 "uI_Type": "Unknown"
#             },
#             "hasTelemetry": True,
#             "appSubCategory": "ToolName",
#             "teamName": user,
#             # "commentID": "string", # uncomment if relevant
#             # "aiCodeRequestType": "CODING_STANDARD", # uncomment if relevant
#             "reactionPositive": 0,
#             "reactionNegative": 0,
#             # "processed": True, # not required
#             "codeSimilarityPercentage": 0,
#             "metaData": "string"
#         }
#     ]


# dbproxy_api = SpecificAPI("dbproxy", environment="prod")

def expand_alert_numbers(alert_numbers_str):  
    """  
    Expands a string like "1123, 1130-1135, 1140-1150, 1172"  
    into a list of integers: [1123, 1130, 1131, ..., 1135, 1140, ..., 1150, 1172]  
    """  
    alert_numbers = []  
    for part in alert_numbers_str.split(','):  
        part = part.strip()  
        if not part:  
            continue  
        # Match range like 1130-1135  
        m = re.match(r'^(\d+)\s*-\s*(\d+)$', part)  
        if m:  
            start = int(m.group(1))  
            end = int(m.group(2))  
            if start > end:  
                raise ValueError(f"Invalid alert range: {part}")  
            alert_numbers.extend(range(start, end + 1))  
        else:  
            # Single number  
            try:  
                alert_numbers.append(int(part))  
            except ValueError:  
                raise ValueError(f"Invalid alert number: {part}")  
    return alert_numbers

# print("FROM CODE")
# alert_numbers = "1123, 1130-1135, 1137, 1140-1150, 1172"
# print(f"Original: {alert_numbers}")
# alert_numbers = expand_alert_numbers(alert_numbers)
# print(f"Expanded: {alert_numbers}")
# print("FROM CLASS")
# alert_numbers = "1123, 1130-1135, 1137, 1140-1150, 1172"
# alert_numbers = FunctionLibrary.expand_alert_numbers(alert_numbers)
# print(f"Class: {alert_numbers}")


# def write_skipped_alerts_to_file(skipped_alert_numbers=None, alert_limit=None):  
#     with open('skipped_alerts.txt', 'w') as f:  
#         if skipped_alert_numbers:  
#             f.write(f"CodeQL Fix Generation processes up to {alert_limit} alerts per run, hence the alerts below were skipped. Please feel free to paste them into the Historical Issue Pipeline to run the tool on those.\n")
#             f.write(f"Skipped alerts: {skipped_alert_numbers}")  

# alert_limit = 10
# skipped_alerts = "101, 102, 104, 106"
# FunctionLibrary.write_skipped_alerts_to_file(skipped_alerts, alert_limit)


# def get_team_name(owner, repo, branch=None, config_path=None):
#     """
#     Get the team name based on the owner, repo, and optionally branch.
#     Reads configuration from a JSON file (config/teams_mapping.json).

#     Args:
#         owner (str): The repository owner.
#         repo (str): The repository name.
#         branch (str, optional): The branch name. Defaults to None.
#         config_path (str, optional): Path to the JSON configuration file. Defaults to 'config/teams_mapping.json'.

#     Returns:
#         str: The team name or a default value if no match is found.
#     """
#     # Default path to the JSON configuration file
#     if not config_path:
#         # Use a relative path based on the location of this script
#         base_dir = os.path.dirname(os.path.abspath(__file__))  # Path to helpers directory
#         config_path = os.path.join(base_dir, '..', 'config', 'teams_mapping.json')  # Navigate to config/teams_mapping.json

#     # Convert inputs to lowercase for case-insensitive matching
#     owner_lower = owner.lower() if owner else ""
#     repo_lower = repo.lower() if repo else ""
#     branch_lower = branch.lower() if branch else None

#     # Read and parse the JSON configuration file
#     try:
#         with open(config_path, 'r', encoding='utf-8') as f:
#             config = json.load(f)
#     except FileNotFoundError:
#         raise FileNotFoundError(f"The configuration file {config_path} does not exist.")
#     except json.JSONDecodeError as e:
#         raise ValueError(f"Error decoding JSON configuration file {config_path}: {e}")

#     # Use case-insensitive lookup
#     for config_owner, owner_repos in config.items():
#         if config_owner.lower() == owner_lower:
#             for config_repo, repo_rules in owner_repos.items():
#                 if config_repo.lower() == repo_lower:
#                     # If a branch is provided, check for a branch-specific team name
#                     if branch_lower:
#                         for pattern, team in repo_rules.items():
#                             if fnmatch.fnmatch(branch_lower, pattern.lower()):
#                                 return team
#                     # If branch not specified or no match found, use the default rule
#                     return repo_rules.get("default", f"{owner}/{repo}")

#     # Return owner/repo as the team name if no match found
#     return f"{owner}/{repo}"


#team = get_team_name("AMD-Radeon-Driver", "drivers", "amd/stg/kmd", "config/teams_mapping_by_team.json")
#print(f"Mapping extracted: {team}")
#name = get_team_name("AMD-Radeon-Driver", "drivers", "amd/stg/xgl_prm", "config/teams_mapping_by_team.json").get("team_name")
#print(f"Extracted name: {name}")


# from urllib.parse import urlparse
# gha_url = "https://github.com/AMD-Radeon-Driver/drivers"
# server, owner, repo = urlparse(gha_url).netloc, *urlparse(gha_url).path.strip("/").split("/")
# if server == "github.com":
#     git_env = "emu"
# else:
#     git_env = "enterprise"
# print(f"server: '{server}', owner: '{owner}', repo: '{repo}', git_env: '{git_env}'")


# TEAM_NAME=$(python -c "from utils.utility_functions import FunctionLibrary; print(FunctionLibrary.get_team_name('amd-radeon-driver','drivers','amd/stg/kmd'))" | sed -n "s/.*'team_name': '\([^']*\)'.*/\1/p")
# amd-radeon-driver
# amdlog-tools
# amd/main
# "team_name": "gfx core"

# TEAM_NAME=$(python -c "from utils.utility_functions import FunctionLibrary; print(FunctionLibrary.get_team_name('amd-radeon-driver','amdlog-tools','amd/main'))" | sed -n "s/.*'team_name': '\([^']*\)'.*/\1/p")
# TEAM_NAME=$(python -c "from utils.utility_functions import FunctionLibrary; print(FunctionLibrary.get_team_name('sw-infra-emu','ai-pr-platform','main'))" | sed -n "s/.*'team_name': '\([^']*\)'.*/\1/p")


#target_branches: "amd/bg-release/24.30/test,amd/bg-release/25.10/test"
#target_branches=["AMD-Radeon-Driver/drivers/amd/stg/xgl_prm","AMD-Radeon-Driver/abcd/amd/stg/abcd"]
#target_branches="AMD-Radeon-Driver/drivers/amd/stg/xgl_prm, AMD-Radeon-Driver/abcd/amd/stg/abcd, SW-Infra-EMU/ai-pr-platform/main"
#target_branches="SW-Infra-EMU/ai-pr-platform/amd/bg-release/24.30/test,SW-Infra-EMU/ai-pr-platform/amd/bg-release/25.10/test"
#team_names = FunctionLibrary.get_team_names_from_github_paths(target_branches)
#print(f"TEAMS: {team_names}")


#test_teams = FunctionLibrary.get_team_name(owner="SW-Infra-EMU",repo="ai-pr-platform",branch="test_cp")
#print(f"BY-TEAM: {test_teams}")


#test_target="AMD-Radeon-Driver/drivers/amd/stg/xgl_prm"
test_target="AMD-Radeon-Driver/address-lib/amd/stg/pal"

#e_owner, e_repo, e_branch = FunctionLibrary.extract_components(test_target)
#print(f"O: {e_owner}, R: {e_repo}, B: {e_branch}")

def get_team_name(full_path):
    full_path = full_path.lower()
    # Split the path to get owner/repo and branch
    parts = full_path.split('/', 2)
    if len(parts) < 3:
        return None
    
    owner_repo = f"{parts[0]}/{parts[1]}"
    branch = parts[2]
    
    # Load the mapping file from the config folder
    config_path = os.path.join('config', 'teams_mapping_by_team.json')
    with open(config_path, 'r') as f:
        teams_mapping = json.load(f)
    
    # Iterate through teams to find a match
    for team_name, repos in teams_mapping.items():
        if owner_repo in repos:
            # Check if the branch matches any of the branches for this repo
            for mapped_branch in repos[owner_repo]:
                # The branch in the path starts with the mapped branch
                if branch == mapped_branch or branch.startswith(mapped_branch + '/'):
                    return team_name
    
    return None

#test_path = "AMD-Radeon-Driver/drivers/amd/acp"
test_path = "SW-Infra-EMU/ai-pr-platform/test_cp,AMD-Radeon-Driver/drivers/amd/acp"
#test_path = "sw-infra-emu/ai-pr-platform/test_cp"
#team = get_team_name(test_path)
#team = FunctionLibrary.get_team_name(test_path, "config/teams_mapping_by_team.json")
team = FunctionLibrary.get_team_name(test_path)
print(f"TEAM_NAME: {team}")

teams = FunctionLibrary.get_team_names_from_github_paths(test_path)
print(f"List of teams: {teams}")

source_branch = "cp_test_sel_#"
target_branch = "SW-Infra-EMU/ai-pr-platform/amd/bg-release/24.30/test,SW-Infra-EMU/ai-pr-platform/amd/bg-release/25.10/test"
# team_names = FunctionLibrary.get_team_names_from_github_paths(target_branch)

# target_branches = [branch.strip() for branch in target_branch.split(',')]

# for i, github_path in enumerate(target_branches):
#     team_name = team_names[i]
#     context = {
#         #"commit_id": args.commit_id,  
#         #"from_date": args.from_date, 
#         "team_name": team_name,
#         "source_branch": source_branch,
#         "target_branch": github_path,
#         "repo_url": "https://github.com/SW-Infra-EMU/ai-pr-platform"
#     }
#     print(f"Team {team_name} context: {context}")




team_names = FunctionLibrary.get_team_names_from_github_paths(target_branch)    
target_branches = [branch.strip() for branch in target_branch.split(',')]
# Group target branches by team name
team_branch_groups = {}
for i, github_path in enumerate(target_branches):
    team_name = team_names[i]
    if team_name not in team_branch_groups:
        team_branch_groups[team_name] = []
    team_branch_groups[team_name].append(github_path)

# Execute workflow for each team with their grouped branches
for team_name, branches in team_branch_groups.items():
    context = {
        #"commit_id": args.commit_id,  
        #"from_date": args.from_date, 
        "team_name": team_name,
        "source_branch": source_branch,
        "target_branch": branches,  # Now passing a list of branches for this team
        "repo_url": "https://github.com/SW-Infra-EMU/ai-pr-platform"
    }  

    print(f"Team {team_name} context: {context}")      



#test_parse_full = [{'alert_number': 765, 'url': 'https://github.com/AMD-Radeon-Driver/drivers/security/code-scanning/765', 'predicted_as_fp': False, 'pr_url': 'https://github.com/AMD-Radeon-Driver/drivers/pull/122801', 'branch_name': 'amd/dev/swjenci/swdev-6/codeql-fix-765', 'explanation': None}, {'alert_number': 765, 'url': 'https://github.com/AMD-Radeon-Driver/drivers/security/code-scanning/765', 'predicted_as_fp': False, 'pr_url': 'https://github.com/AMD-Radeon-Driver/drivers/pull/122802', 'branch_name': 'amd/dev/swjenci/swdev-6/codeql-fix-765-2', 'explanation': None}]
#test_parse = [pr['pr_url'] for pr in test_parse_full]
#print(test_parse)

def file_mapping(file_path):

    path_components = os.path.normpath(file_path).split(os.path.sep)
    root_folder = path_components[0]
    match root_folder:
        case 'dc' | 'include':
            return 'dc'
        case 'amdgpu_dm':
            return 'dm/amdgpu'
        case 'windows_dm':
            return 'dm/windows'
        case 'modules':
            if len(path_components) > 1:
                return f'modules/{path_components[1]}'
            return 'modules'
        case 'test':
            if len(path_components) > 1:
                return f'test/{path_components[1]}'
            return 'test'
        case _:
            return root_folder


test_paths = [
    "dc/resource/dcn60/dcn60_resource.c",
    "include/header.h",
    "amdgpu_dm/file.c",
    "windows_dm/dal3/WindowsDMIsr.cpp",
    "modules/color/gm/file.c",
    "modules/freesync/file.c",
    "test/diags/file.c",
    "test/scripts/fpga/file.c"
]

for path in test_paths:
    translated = file_mapping(path)
    print(f"OG: {path} -> Translated: {translated}")

    