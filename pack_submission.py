import os, zipfile
out='Certification_Evidence/Telecom_Submission_Updated_2026-10-22.zip'
for old in ['Certification_Evidence/FINAL_SUBMISSION_PACKAGE/05_Supervisor_Transcript/final_debug_trace_2026-10-21.json','Certification_Evidence/FINAL_SUBMISSION_PACKAGE/05_Supervisor_Transcript/final_supervisor_conversation_2026-10-21.json']:
    if os.path.exists(old): os.remove(old)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    roots=['Certification_Evidence/Submission_Screenshots','Certification_Evidence/Project_Source','Certification_Evidence/FINAL_SUBMISSION_CHECKLIST_2026-10-22.md']
    for root in roots:
        if os.path.isfile(root): z.write(root,os.path.relpath(root,'Certification_Evidence'))
        else:
            for dp,_,fs in os.walk(root):
                for f in fs:
                    p=os.path.join(dp,f); z.write(p,os.path.relpath(p,'Certification_Evidence'))
print(out,os.path.getsize(out))
