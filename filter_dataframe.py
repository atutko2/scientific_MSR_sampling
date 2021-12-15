import pandas as pd
import pickle
from os.path import exists

def fil_df( df, dtype, fil_string, s):

    """
    Filters based on whether it is an int, string, float, or bool
    
    @param df: the dataframe to filter
    @param dtype: the type of data being filtered
    @param fill_string: the column in the dataframe to filter on
    @param s: the restrictions
    returns: the filtered dataframe
    """
    
    if(dtype == "float"):
        # if there is a lower bound but no upper (Watchers > 100)
        if( s[0] != -1.0 and s[1] == -1.0 ):
            df = df[df[fil_string] > s[0]]
        # if there is a upper bound but no lower (Watchers < 100)    
        elif( s[0] == -1.0 and s[1] != -1.0 ):
            df = df[df[fil_string] < s[1]]
        # if there is a lower bound and a upper (Watchers > 100 and Watchers < 1000)
        else:
            df = df.loc[(df[fil_string].between(s[0], s[1]))]
    
    if(dtype == "int"):
        # if there is a lower bound but no upper (Watchers > 100)
        if( s[0] != -1 and s[1] == -1 ):
            df = df[df[fil_string] > s[0]]
        # if there is a upper bound but no lower (Watchers < 100)    
        elif( s[0] == -1 and s[1] != -1 ):
            df = df[df[fil_string] < s[1]]
        # if there is a lower bound and a upper (Watchers > 100 and Watchers < 1000)
        else:
            df = df.loc[(df[fil_string].between(s[0], s[1]))]
            
    if(dtype == "string"):
        new_df = []

        tmp_string = ""
        tmp_fil = fil_string.replace(" ", "_")
        
        for l in s:
            tmp_string += l.replace(" ", "_")
            tmp_string += "_"
        tmp_string = tmp_string[:-1]
        tmp_string += ".pkl"
        path = "dataframes/" + tmp_fil + "_" + tmp_string
        if exists(path):
            df = pd.read_pickle(path)
        else:
            for x in range(len(original_df)):
                for t in s:
                    if(t in str(original_df[fil_string].iloc[x]).split(",")):
                        new_df.append(original_df.iloc[x])
                        #print(original_df.iloc[x])
                        break

            df = pd.DataFrame(new_df)
            df.to_pickle(path)
            
        
    if(dtype == "bool"):
        df = df[df[fil_string] == True]
    
    return df
    
    
def filter_dataframe(df, **kwargs):
    """
    When a user chooses a filter on the API, this filters the dataframe being looked at.
    
    @param df: the dataframe to filter
    @param **kwargs: a dictionary with all of the potential filters
    @param **kwargs keys:
                        (Floats)
                          Watchers, Commits, Branches, Releases, Contributors
                          Total Issues, Open Issues, Total Pull Requests, Open Pull Requests

                        (Ints)
                          Size, Forks, Stargazers

                        (Strings)
                          Languages, Main Language, Default Branch, License, Labels
                         

                        (Bools)
                          Is Fork, Is Archived, Has Wiki
    
    returns: the filtered dataframe
    """
    
    
    # FLOATS
    s = kwargs.get('Watchers')
    
    if s != None:
        df = fil_df(df, "float", "Watchers", s)
    
    
    s = kwargs.get('Commits')
    
    if s != None:
    
        df = fil_df(df, "float", "Commits", s)

    
    s = kwargs.get('Branches')
    
    if s != None:
    
        df = fil_df(df, "float", "Branches", s)
    
    
    s = kwargs.get('Releases')
    
    if s != None:
    
        df = fil_df(df, "float", "Releases", s)
    
    
    s = kwargs.get('Contributors')
    
    if s != None:
    
        df = fil_df(df, "float", "Contributors", s)

    
    s = kwargs.get('Total_Issues')
    
    if s != None:
        
        df = fil_df(df, "float", "Total Issues", s)

   

    s = kwargs.get('Open_Issues')
    
    if s != None:
            
        df = fil_df(df, "float", "Open Issues", s)

            
    
    s = kwargs.get('Total_Pull_Requests')
    
    if s != None:
                 
        df = fil_df(df, "float", "Total Pull Requests", s)
    
    
    s = kwargs.get('Open_Pull_Requests')
    
    if s != None:
        
        df = fil_df(df, "float", "Open Pull Requests", s)
    
    
    
    # INTS
    s = kwargs.get('Size')
    
    
    if s != None:
        
        df = fil_df(df, "int", "Size", s)
        
    
    
    s = kwargs.get('Forks')
    
    if s != None:
    
        df = fil_df(df, "int", "Forks", s)
        
        
        
    s = kwargs.get('Stargazers')
    
    if s != None:
        
        df = fil_df(df, "int", "Stargazers", s)
    
    
    # STRINGS
    s = kwargs.get('Languages')
    
    #filter dataframe by desired languages
    if s != None:
         
        df = fil_df(df, "string", "Languages", s)
    
    
    s = kwargs.get('Main_Language')
    
    #filter dataframe by desired languages
    if s != None:
        
        df = fil_df(df, "string", "Main Language", s)
        
    
    
    s = kwargs.get('Default_Branch')
    
    #filter dataframe by desired languages
    if s != None:
        
        df = fil_df(df, "string", "Default Branch", s)
        
        
        
    s = kwargs.get('License')
    
    #filter dataframe by desired languages
    if s != None:
        
        df = fil_df(df, "string", "License", s)
        
        
        
    s = kwargs.get('Labels')
    
    #filter dataframe by desired languages
    if s != None:
        
        df = fil_df(df, "string", "Labels", s)
        
        
    # BOOLS
    s = kwargs.get('Is_Fork')
    
    if s != None:
        
        df = fil_df(df, "bool", "Is Fork", s)
        
    
    s = kwargs.get('Is_Archived')
    
    if s != None:
        
        df = fil_df(df, "bool", "Is Archived", s) 
        
    s = kwargs.get('Has_Wiki')
    
    if s != None:
        
        df = fil_df(df, "bool", "Has Wiki", s) 
        
    
    return df


