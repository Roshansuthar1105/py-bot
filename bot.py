from github import Github
import os

# Load GitHub token
token = os.getenv("GH_TOKEN")
repo_name = os.getenv("https://github.com/Roshansuthar1105/py-bot/")  # e.g., "username/repo"
issue_number = os.getenv("ISSUE_NUMBER")

# Authenticate
g = Github(token)
repo = g.get_repo(repo_name)
issue = repo.get_issue(int(issue_number))

# Add a label to the issue
label_name = "label1"
labels = issue.get_labels()
if not any(l.name == label_name for l in labels):
    issue.add_to_labels(label_name)

# Assign the issue to its author
issue.add_to_assignees(issue.user.login)

# -----------------------------
# 3) Add a comment tagging creator
# -----------------------------
comment_text = f"@{creator} issue assigned."
issue.create_comment(comment_text)

print(f"✅ Issue #{issue.number} labeled '{label_name}' and assigned to {issue.user.login}, and commented.")
