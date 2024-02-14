from kim_query import raw_query
import requests

def get_pairs_matching_criteria(types,files,term):
    """
    Searches through "data" database of OpenKIM repository to find specified text in output files

    Args:
        types:
            List of types of results or errors to search for, i.e. some subset of ["er","tr","vr"]
        files:
            Which files to look in, i.e. "pipeline.stdout","pipeline.stderr" or "pipeline.exception"
        term:
            What to look for, e.g. PipelineNoCompatibleSitesFoundForJob
    """

    if type(files) is dict:
        project = ["meta.uuid","meta.runner.kimcode","meta.subject.kimcode","meta.runner.driver.kimcode"]
    else:
        project = ["meta.uuid","meta.runner.kimcode","meta.subject.kimcode"]
    results = raw_query(query={"meta.type":{"$in":types}}, fields = {"meta.uuid":1,"meta.runner.kimcode":1,"meta.runner.driver.kimcode":1,"meta.subject.kimcode":1}, limit=0, project=project,database='data')
    matching_pairs=[]
    hits = 0
    with open("failed_requests.txt","w") as f:
        for i,result in enumerate(results):
            print("Processing result %d of %d, found %d matches"%(i,len(results),hits),end="\r")
            if type(files) is dict:
                uuid,runner,subject,driver=result              
            else:
                uuid,runner,subject=result
            for entry in files:
                if type(files) is list:
                    filename = entry
                elif type(files) is dict:
                    if driver == entry:
                        filename = files[entry]
                    else:
                        continue

                file_url="https://openkim.org/files/"+uuid+"/"+filename
                try:
                    output=requests.get(file_url).text
                    if output.find(term)!=-1:
                        matching_pairs.append([runner,subject])
                        hits += 1
                        break
                except:
                    print("Could not download file "+file_url)
                    pass
        
    return matching_pairs

