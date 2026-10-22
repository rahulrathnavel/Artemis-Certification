import json, subprocess
args = [
 r'C:\Users\rahul\AppData\Roaming\npm\artemis-platform-cli.cmd','lifecycle','deployment','create',
 '--project','01a14414-d023-7c6f-ac0d-78711d9aeb8f','--environment','dev',
 '--entry-agent','Telecom_Supervisor','--agent-manifest',
 json.dumps({
  'Telecom_Supervisor': {'version':'1.0.0'},
  'TopUpPlan_Query_Agent': {'version':'1.0.0'},
  'UserDataPlan': {'version':'1.0.0'},
  'SIMIssueAgent': {'version':'1.0.0'},
 }), '--label','Telecom Supervisor 1.0.0 - Full Multi-Agent',
 '--description','Full telecom deployment including all specialists']
r = subprocess.run(args, text=True, capture_output=True)
print(r.stdout)
print(r.stderr)
