import simple_random_sample

def stratify_sample(df, stratify_by, dtype, **kwargs):
    """
    Split the dataframe into multiple dataframes containing each strata 
    (i.e. dfs[0] contains projects with < 10 Forks)
    
    @param df: the dataframe being stratafied
    @param stratify_by: the column to stratify
    @param dtype: the datatype
    
    Notes:
    This will always be disproportionate stratafied random sampling because the
    number of projects of each will not be equal.
    
    If stratifying by Languages it is possible the results will contain duplicates.
    This is due the existense of many languages in a single project.
    
    Only stratify by one parameter.
    Possible Strata:
    STRINGS:
    Languages
    Main Language
    License
    
    FlOATS:
    Commits
    Contributors
    Branches
    Releases
    Watchers
    Total Issues
    Open Issues
    Total Pull Requests
    Open Pull Requests
    
    INTS:
    Stargazers
    Forks
    Size
    
    """
    
    #print(len(df))
        
    stratum, dfs, percents, total_rows = create_viable_strata(df, stratify_by, dtype, **kwargs)
    
    percentage = 0.10
    s1 = kwargs.get('Percentage')
    if(s1 != None):
        percentage = s1
    
    
    samples = []
    seeds = []
    for x in range(len(dfs)):
        s, sample = simple_random_sample(dfs[x], int(len(dfs[x]) * percentage) )
        samples.append(sample)
        seeds.append(s)
    
    for s in samples:
        if(len(s) != 0):
            print(s[stratify_by])
        print(len(s))
