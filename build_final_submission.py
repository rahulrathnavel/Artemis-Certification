import os, zipfile, shutil
from pathlib import Path
base=Path('Certification_Evidence')
outdir=base/'FINAL_SUBMISSION_PACKAGE'
if outdir.exists(): shutil.rmtree(outdir)
for d in ['01_SOP','02_Project_Export','03_Evals_Output','04_End_User_Conversation','05_Supervisor_Transcript','06_Configuration_Evidence']:
    (outdir/d).mkdir(parents=True)
shutil.copy2(base/'Telecom_Project_SOP.md', outdir/'01_SOP'/'Telecom_Project_SOP.md')
shutil.copy2(Path(r'C:\Users\rahul\Downloads\rahulrathnavel-telecom-assignment-project_.zip'), outdir/'02_Project_Export'/'rahulrathnavel-telecom-assignment-project_.zip')
shutil.copy2(base/'Submission_Screenshots'/'Evals_Telecom_Multi_agent.png', outdir/'03_Evals_Output'/'Evals_Telecom_Multi_agent.png')
for p in (base/'Submission_Screenshots').glob('T*'):
    if p.is_dir(): shutil.copytree(p, outdir/'04_End_User_Conversation'/p.name)
for src,name in [(Path(r'C:\Users\rahul\Downloads\final_debug_traces_MultiAgent_Orchestration_Supervisor_Conversation_Log (1).json'),'final_debug_trace_gradious_gpt_2026-10-22.json'),(Path(r'C:\Users\rahul\Downloads\final_debug_traces_MultiAgent_Orchestration_Supervisor_Conversation_Log (2).json'),'final_supervisor_conversation_gradious_gpt_2026-10-22.json')]:
    shutil.copy2(src, outdir/'05_Supervisor_Transcript'/name)
for p in [base/'Submission_Screenshots'/'02_supervisor_identity_goal.png', base/'Submission_Screenshots'/'03_supervisor_routing.png', base/'Submission_Screenshots'/'04_topup_agent_configuration.png', base/'Submission_Screenshots'/'05_topup_agent_tools.png', base/'Submission_Screenshots'/'06_userdata_agent_configuration.png', base/'Submission_Screenshots'/'08_userdata_agent_tools.png', base/'Submission_Screenshots'/'09_sim_agent_configuration.png', base/'Submission_Screenshots'/'10_sim_mcp_agent_tools.png', base/'Submission_Screenshots'/'11_supervisor_guardrails.png', base/'Submission_Screenshots'/'project_level_policy_guardrails.png']:
    if p.exists(): shutil.copy2(p, outdir/'06_Configuration_Evidence'/p.name)
(outdir/'README.md').write_text('Telecom multi-agent certification submission\\n\\nLive demo: https://agents.kore.ai/preview#share_token=eyJwcm9qZWN0SWQiOiIwMWExNDQxNC1kMDIzLTdjNmYtYWMwZC03ODcxMWQ5YWViOGYiLCJ0ZW5hbnRJZCI6IjAxOWVhNmE0LTcyYTEtN2NhMS04NTJkLTRmYWFhOWVmZDhjZCIsImNoYW5uZWxJZCI6IjAxYTE2MzdhLTI2MjAtNzQyMi05YWNhLTM2ZTY1ZmMzN2UwNiIsInBlcm1pc3Npb25zIjpbInNlc3Npb246c2VuZF9tZXNzYWdlIiwiYXR0YWNobWVudDpyZWFkIiwiYXR0YWNobWVudDp3cml0ZSIsInNlc3Npb246cmVhZCJdLCJleHAiOjE3OTMyNzUxMTc5OTYsInR5cGUiOiJzaGFyZSJ9.zvyBclJMtVeDda3oYRLtrcRiysJA7oR_v3ErrBoM5k8\\n\\n01_SOP: project SOP\\n02_Project_Export: Gradious project export with Evals excluded\\n03_Evals_Output: completed 100/100 Evals screenshot\\n04_End_User_Conversation: end-user conversation evidence\\n05_Supervisor_Transcript: Supervisor transcript and debug trace\\n06_Configuration_Evidence: agent and guardrail configuration screenshots\\n', encoding='utf-8')
zip_path=base/'RahulRathnavel_telecom_assignment_project.zip'
if zip_path.exists(): zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for dp,_,fs in os.walk(outdir):
        for f in fs:
            p=Path(dp)/f; z.write(p,p.relative_to(outdir))
print(zip_path, zip_path.stat().st_size)
