import pandas as pd

def f_clean(filename):


    file = filename + '.csv'

    df = pd.read_csv(file)


    trial= df.copy()

    #subsetting
    trial = df[['type','likes/views','age','hashtags','mentions']]


    #filling NA
    trial["hashtags"].fillna("gak_ada", inplace = True) 
    trial["mentions"].fillna("gak_ada", inplace = True) 




    # <h1>Feature Engineering </h1>
    # 
    # 1. Categorical Likes / Views
    # 2. Hashtags
    # 3. Mentions
    # 4. Age
    # 


    #### categorical for likes/views ####



    #video 
    temp = []

    for i in trial['type']:
        if i == 'video':
            temp.append(1)
        
        else:
            temp.append(0)
            
    trial['type_video'] = temp  


    temp = []
    #photo
    for i in trial['type']:
        if i == 'photo':
            temp.append(1)
        
        else:
            temp.append(0)

    trial['type_photo'] = temp 



    #### Hashtags ####

    #temporary values
    placeholder = trial['hashtags']


    #counter for number of hashtags

    temp = []
    for i in placeholder:
        if i == 'gak_ada':
            counter = 0
            temp.append(counter)
        else:
            counter = i.count(",") + 1
            temp.append(counter)
            
        
    #append to dataframe
    trial['num_hashtags'] = temp



    #### Mentions ####

    #temporary values
    placeholder = trial['mentions']


    #counter for number of hashtags

    temp = []
    for i in placeholder:
        if i == 'gak_ada':
            counter = 0
            temp.append(counter)
        else:
            counter = i.count(",") + 1
            temp.append(counter)
            
        
    #append to dataframe
    trial['num_mentions'] = temp

    # append m
    time = trial['age'].str.contains('m')

    placeholder = []

  

    for i in time:
        if i == True:
            placeholder.append('m')
        else:
            continue



    # append h  
    time = trial['age'].str.contains('h')

  

    for i in time:
        if i == True:
            placeholder.append('h')
        else:
            continue

    time = trial['age'].str.contains('d')

    # append d 

    for i in time:
        if i == True:
            placeholder.append('d')
        else:
            continue
            
    # append w

    time = trial['age'].str.contains('w')

    for i in time:
        if i == True:
            placeholder.append('w')
        else:
            continue


    #slicing the age feature



    trial['age_num'] = trial['age'].replace(to_replace = ['m','d','w','h'], value = '', regex=True)
    #trial['age_num'] = trial['age'].replace(to_replace = 'w', value = '', regex=True)
    #trial['age_num'] = trial['age'].replace(to_replace = 'h', value = '', regex=True)


    # multiplier


    haha = []


    for i in placeholder:
        if i == 'm':
            haha.append(1/60)
        elif i == 'h':
            haha.append(1)
        elif i == 'd':
            haha.append(24)
        else:
            haha.append(168)



    trial['multiplier'] = haha

    trial['age_num'] = pd.to_numeric(trial['age_num'], errors='coerce')

    trial['age_hours'] = trial['multiplier'] * trial['age_num']


    # <h1> Analysis </h1>



    #final df for metric analytics

    final_df = trial[['likes/views', 'age_hours', 'num_hashtags', 'num_mentions','type_photo','type_video']]

    final_df.head()





    final_df['likes/views'] = final_df['likes/views'].replace(to_replace = ',', value = '', regex=True)

    final_df['likes/views'] = pd.to_numeric(final_df['likes/views'])

    final_df.dtypes





    photo = final_df[final_df['type_photo'] == 1]

    photo = photo.rename(columns={'likes/views':'likes'})

    photo = photo.drop('type_video', axis=1)

    photocorr = photo.corr()


 


    video = final_df[final_df['type_video'] == 1]

    video = video.rename(columns={'likes/views':'views'})

    video = video.drop('type_photo', axis=1)

    videocorr = video.corr()




    ####### saving to excel #######

    df['age_hours'] = final_df['age_hours']
    df['num_hashtags'] = final_df['num_hashtags']
    df['num_mentions'] = final_df['num_mentions']
    df['type_photo'] = final_df['type_photo']
    df['type_video'] = final_df['type_video']


    with pd.ExcelWriter('clean_'+filename+'.xlsx') as writer:  

        df.to_excel(writer, sheet_name = 'full')
        photo.to_excel(writer, sheet_name = 'photo')
        video.to_excel(writer, sheet_name = 'video')
        photocorr.to_excel(writer, sheet_name = 'photo corr')
        videocorr.to_excel(writer, sheet_name = 'video corr')

