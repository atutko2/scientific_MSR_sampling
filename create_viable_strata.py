def create_viable_strata( df, stratify_by, dtype, **kwargs ):
    """
    If the values are Int or Floats: 
	Finds a set of 10 strata with no less than 2 percent of the population
    If the values are strings:
	Either uses the passed strata - minimum 3 (i.e. if Languages: Java, Python, C++)
	Or uses all strata (i.e. if Languages: All possible languages in the dataset)

    @param df: the dataframe being stratafied
    @param stratify_by: the column to stratify
    @param dtype: the datatype
    returns: the 10 stratum and the filtered dataframes
    
    
    Notes:
         A strata is not considered viable if it does not atleast contain 2
         percent of the population. (Reasoning: if the desired population is
         1000, the sample still contains 20 projects)
         
         There needs to be a minimum of at least 3 strata. (Reasoning: a 
         population divided in half is not stratified)

         For viable strata using contributors or commits - Takes the median
         value of the column to calculate the increment between each stratum.
         
        
         For viable strata using any other float or int - Takes the highest and lowest
         value in the column, then divides the total by 10, that starts with 10
         potential strata. If they are not viable, it decreases the starting 
         increment and tries again.
    """
    
    stratify_by2 = stratify_by
    if(" " in stratify_by):
        stratify_by2 = stratify_by2.replace(" ", "_" )
    
    # if the strata is not Languages, Main Language, or License
    if(dtype == "float" or dtype == "int"):
        # get the max and min of the column to stratify
        max_col_val = df[stratify_by].max()
        min_col_val = df[stratify_by].min()
        #print(max_col_val)

        # get the total value of that column by subtracting the max from the min
        total_col = max_col_val - min_col_val

        # increment between strata (i.e. max val is 100, min is 0, with 10 strata, the increment is 10)
        if(stratify_by not in ["Commits", "Contributors", "Size"] ):
            increment = total_col/10
        # if the value being stratified are contributors, size, or commits,
        # make the start of the strata the median value because there 
        # are projects with billions of commits, or contributors
        else:
            increment = df[stratify_by].median()/2


        # create 10 potential stratas
        stratas = []
        for x in range(1, 11):
            stratas.append(min_col_val + int(x * increment))

        while( True ):                                        
        
            # create the 10 dataframes for each strata (i.e. filter the dataframe by some restrictions)
            dfs = []
            total_rows = 0
            for x in range(0, 10):
                if( x == 0 ):
                    dic = { stratify_by2: [-1.0, stratas[0]]}
                elif( x == 9):
                    dic = { stratify_by2: [stratas[x-1]+1, -1.0]}
                else:
                    dic = { stratify_by2: [stratas[x-1]+1, stratas[x]]}

                tmp_df = filter_dataframe(df, **dic)
                #print(tmp_df[stratify_by])

                # append the dataframe if actually contains data
                if(len(tmp_df) != 0 ):
                    dfs.append(tmp_df)
                    total_rows += len(tmp_df)
                tmp_df = []

            # get the total number of strata
            num_strata = len(dfs)
            #print(num_strata)
            

            # get the percents of the each strata
            percents = []
            flag = False
            for x in range(0, num_strata):
                # if the percent of any of the strata is less than 2
                # calculate new strata
                if( len(dfs[x])/total_rows * 100 < 2.0 ):
                    flag = True
                    # change the increment value by 20 percent
                    increment = increment/1.2


                    # create 10 new potential stratas
                    stratas = []
                    for x in range(1, 11):
                        stratas.append(min_col_val + int(x * increment))
                    
                    break
                percents.append(len(dfs[x])/total_rows * 100.0)
                    
            if( flag == True):
                continue
                
            # return the calculated strata
            return stratas, dfs, percents
    # else we are stratifying by License, Languages, or Main Language    
    else:
        
        s1 = kwargs.get('Languages')
        s2 = kwargs.get('Main Language')
        s3 = kwargs.get('License')
        
        # if there was no set of languages stratify by
        if((stratify_by == "Languages" or stratify_by == "Main Language" ) and s1 == None and s2 == None ):
            
            all_languages = []
            # get all the possible languages it could be
            for x in original_df['Languages']:
                if(str(x) != "nan"):
                    ls = x.split(",")
                    for l in ls:
                        if( l not in all_languages ):
                            all_languages.append(l)
            all_strata = all_languages
        # if there was no set license to stratify by
        elif(stratify_by == "License" and s3 == None ):
            all_license = []
            # get all the possible license it could be
            for x in original_df['License']:
                if(str(x) != "nan"):
                    ls = x.split(",")
                    for l in ls:
                        if( l not in all_license ):
                            all_license.append(l)
            all_strata = all_license
        # else use the strata desired was provided
        else:
            if(s1 != None):
                all_strata = s1
            elif(s2 != None):
                all_strata = s2
            else:
                all_strata = s3
        # get the total number of strata
        num_strata = len(all_strata)
        
        dfs = []
        total_rows = 0
        for s in all_strata:
            # get the dataframe containing of the projects with that language
            dic = { stratify_by2: [s]}
            new_df = filter_dataframe(df, **dic)
            #print("Strata: %s, Len: %d" % ( s, len(new_df)))
            dfs.append(new_df)
            total_rows += len(new_df)
        
        percents = []
        new_dfs = []
        for d in dfs:
            if(len(d)/total_rows * 100.0 != 0.0):
                percents.append(len(d)/total_rows * 100.0)
                new_dfs.append(d)
        
        return all_strata, new_dfs, percents
    
