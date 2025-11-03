def job_seq(jobs):
    jobs.sort(key=lambda x:x[2],reverse=True)
    n=max(j[1] for j in jobs)
    slot=[None]*n
    for id,d,p in jobs:
        for i in range(d-1,-1,-1):
            if slot[i] is None:
                slot[i]=id
                break
    print("Scheduled jobs:",[j for j in slot if j])
n=int(input("enter number of jobs:"))
jobs=[tuple(input(f"job{i+1}(id deadline profit):").split()) for i in range(n)]
jobs=[(j,int(d),int(p)) for j,d,p in jobs]
job_seq(jobs)