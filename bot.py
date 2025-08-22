from github import Github
import os

# -----------------------------
# Load environment variables
# -----------------------------
token = os.getenv("GH_TOKEN")
repo_name = os.getenv("REPO_NAME")       # we’ll pass this from workflow
issue_number = os.getenv("ISSUE_NUMBER") # we’ll pass this from workflow

if not repo_name or not issue_number:
    raise RuntimeError("❌ Missing REPO_NAME or ISSUE_NUMBER environment variables")

# Authenticate with GitHub
g = Github(token)
repo = g.get_repo(repo_name)
issue = repo.get_issue(int(issue_number))

# -----------------------------
# 1) Add a label
# -----------------------------
label_name = "bug"   # change this to whatever label you want
if label_name not in [l.name for l in issue.get_labels()]:
    issue.add_to_labels(label_name)

# -----------------------------
# 2) Assign to issue creator
# -----------------------------
creator = issue.user.login
issue.add_to_assignees(creator)

# -----------------------------
# 3) Add a comment tagging creator
# -----------------------------
comment_text = f"@{creator} issue assigned."
issue.create_comment(comment_text)

print(f"✅ Issue #{issue.number}: labeled '{label_name}', assigned to {creator}, and commented.")
