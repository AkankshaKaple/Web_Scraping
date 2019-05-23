#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import csv


# In[2]:


class Data_Filteration():
    
    def __init__(self):
        self.ark = 0
    
    def column_selection(self, data):
        required = ['Contact Status', 'Designation', 'Designation 2', 'Designation 3','Location', 'Requirements', 'Size']
        for i in data.columns:
            if i not in required:
                data.drop(i, inplace=True, axis = 1)
        return data

    def Filter_Company_Type(self, data):
        type_1 = ['0-10']
        type_3 = ['501-1000','1001-5000', '5000+', '1000-5000', '500+']
        comp_type = []
        for i in data.Size:
            if i in type_1:
                comp_type.append("Type_1")
            elif i in type_3:
                comp_type.append("Type_3")
            else:
                comp_type.append("Type_2")
            
        data["Company_Type"] = comp_type
        data.drop(columns="Size", inplace=True)
        
        req_data = pd.get_dummies(data["Company_Type"], drop_first=True)
        
        req_data['id'] = np.arange(0,len(req_data))
        data['id'] = np.arange(0,len(data))
        data = data.merge(req_data)
        
        data.drop(columns="Company_Type", inplace=True)
        
        return data
    
    def Filter_Requirments(self, data):
        dict = {}
        dict["Backend"] = {'back end','devops','backend', 'python/djangobackend', 'lampstack','mango','webbackend','backenddeveloper','softwaremagento'
                           ,'mongodb','sqlserver','softwarebackend','scala','mysqldba','androidosfirmware','fluttermobile',"microservices"
                           ,'djangopythonbackend', 'backendjava','softwaredatabase','php_laravel_mysql','flutter','laravel','drupal','ror','unity'
                           ,'backendnodejs','sqldeveloper', 'sql', 'angular.js','backendengineer','angularjs/html','javabackend','magento','magento'
                           , 'mysql','phpbackend','pythonbackend', 'backed', 'nodebackend','javaspring'
                           ,'javascript/bootstrap','backend (elixir)'}

        dict["Frontend"] = {'Java','PHP','c #','dot net','lamp stack','ux/ui android','angular js 5','frontend (angular/ mean stack)','angular frontend','mern stack','mean stack','frontt end','front end',"meanstack", 'uideveloper','mobile', 'reactjs', 'ios', 'fronttend', 'frontend','androidapp'
                            ,'php', 'angular', 'react', 'java','asp .net', '.net', 'android','asp.net', 'objectivec','javamobile','uisoftware'
                            ,'ui/frontend', 'ui/ux', 'c#', 'c','fullstackfrontend','angularfrontend','dotnet','desktopapp', 'web', 'javascript'
                            ,'mean','frontend','reactnative','softwarefrontend','devopshacker','fullstackandroid','andoid', 'phplaravel'
                            ,'ui','golang', 'frontendangular/angular.js', 'frontendweb','ux','ember.jswithdjangorestapi','lamp'
                            ,'dot.net', 'ux/uiandroid','frontend/ui', 'juniorandroid','frontendreact','mobile/frontend','api', 'softwareios'
                            ,'frontned','frontendreactjs','androidframework','juniorfrontend','javaweb', 'web/ui','ionicapp','enterpriseintegration'
                            , 'frontendengineer','pythonweb','anroid','webfrontend','frotend','html', 'javascript/jquery','fulljavascript'
                            ,'iosapp', 'fortend','css', 'ux/ui','juniorfullstack','mobileapp','frontend.fullstack','androidsoftware','programer'
                            ,'webapp','frontendjs', 'softwaredeveloper', 'iosapp', 'dotnetweb','androidnative', 'webui', 'webgraphic'
                            , 'angular/react','hybridmobileapp','javaandroid', 'mobile/frontend', 'iosapplication','mobileapplication','ionic'
                            ,'angular js','node.js (angular js/ javascripy','frontend (react & native)', 'php laravel'
                            ,'objective c','hybrid mobile','front end. full stack'}

        dict['Fullstack'] = {'angular 5','full-stack','full stack','fullstack', 'hybrid','hybridmobileapplication','node.js', 'angularjs','reactfullstack', 'fullstacksoftware'
                            , 'mernstack', 'django','node', 'anjular','softwarefullstack', 'node.js(angularjs/javascripy'
                            ,'php&mysql','mean/fullstack', 'node.js(angularjs/javascripy','fullstackproduct','hybridmobile'
                            ,'python/django', 'reactjs/reactnative','angular5','stack', 'javasoftware','ux/uifullstack','python'
                            ,'angular2','nodejs','hybridmobileapplication', 'reactnativemobile', 'fullstackjavascript','angularjs5'
                            , 'nativeios', 'pythondjando','c++','openstackdevops', 'c/c++/embeddedsoftwaredeveloper'
                            ,'javafullstack', 'phpfullstack','fullstackpython','javapython', 'angularjs/nodejs','expressjs','softwarejava'
                            ,'fullstackweb', 'angular2ui','django/python','fullstack(django','fulstack','react..js','jsfullstack'
                            ,'softwaredevelopment','productdevelopment','netsuite','app', 'application', 'product','multistacksoftware'
                            ,'multistacksoftware', 'reactnativereact.js','multistacksoftware', 'reactnativereact.js','fullstack&ios','react.js'
                            ,'webfullstack','reactjs/angularjs','react native','angular 2','react js', 'node js','hybrid mobile application'
                            ,'javafullstackresearch','software','fullstackmean/mernstack','angukarreactjs'
                            ,'node.js/aws/javascript'}

        dict['Trainee'] = {'traineesoftware', 'trainee'}

        dict['Testing'] = {'tester','softwaredevelopmenttest', 'test','softwaretester','tester', 'traineesoftwaretesting'
                            ,'automationtest', 'testautomation', 'testing', 'testingengineer','sdet','automation'}

        dict['Cloud_computing'] = {'javacloud', 'cloud','awsdevops'}

        dict['Data_Science'] = {"mlsoftware", "ai", "ml", 'hadoop','datascientist','bigdata','blockchain','ml/ai','machinelearning'
                                ,'machinelearning/ai/bigdata', 'ml/dl','bigdatascala','bi/data','datascience','computervision'
                                , 'bloackchain','deeplearning', 'blockchainfrontend','mldevops','softwareblockchain'
                                ,'machine learning', 'data','big data','computer vision','data science'}

        dict['Other_tech'] = {"qa", 'softwareengineering', 'software','missing', 'sodtware'
                              ,'sofware', 'Enterprise Integration'}
        
        data['Requirements'].fillna("Missing", inplace=True)
        
        
        requirment = []
        for req in data['Requirements']:
            tech = []
            for j in req.split(','):
                j = j.lower().lstrip()
                for key,val in dict.items():
                    if j in val:
                        tech.append(key)

                    else:
                        for key,val in dict.items():
                            for k in j.replace('-',' ').replace('(',' ').replace('/',' ').split(' '):
                                k = k.lower()
                                if k in val:
                                    tech.append(key)                          

            requirment.append(tech)
            
        l = ['Backend', 'Frontend', 'Fullstack', 'Trainee', 'Testing', 'Cloud_computing', 'Data_Science', 'Other_tech']

        index=range(0,len(data))
        req_data = pd.DataFrame(index=index, columns=l)
        
        for i in range(len(data)):
            for j in requirment[i]:
                if j in l:
                    req_data[j][i] = 1
                    
        req_data.fillna(0, inplace=True)
        
        req_data = pd.get_dummies(req_data, drop_first=True)
        
        req_data['id'] = np.arange(0,len(req_data))
        
        data = data.merge(req_data)
        data.drop(columns="Requirements", inplace=True)
        
        return data

    def Filter_Location(self, data):
        import re
        location = []
        
        loc = data.Location
        
        for i in range(len(data)):
            value = re.split('; |, |/',str(loc[i]))
            if "Gurugoan" in value:
                words = [w.replace('Gurugoan', 'Gurgaon') for w in re.split('; |, |/',str(data["Location"][i]))]
                location.append(words)
            else:
                location.append(value)

        cities = ['Bengaluru', 'Mumbai', 'Pune', 'Hyderabad', 'Chennai', 'Noida', 'Delhi', 'Kolkata', 'Gurgaon']

        loc = []
        for i in location:
            a = []
            for j in i:
                j = j.split(' ')
                for l in cities:
                    if l in j:
                        a.append(l)
            loc.append(a)
        
        index=range(0,len(data))
        new_d = pd.DataFrame(index=index, columns=cities)

        for i in range(len(data)):
            for j in loc[i]:
                if j in l:
                    new_d[j][i] = 1
                    
        new_d['id'] = np.arange(0,len(new_d))
        new_d.fillna(0, inplace=True)

        data = data.merge(new_d)
        data.drop(columns="Location", inplace=True)
        return data

    def Filter_Desingation(self, data):
        
        data["Designation"].fillna("Missing", inplace=True)
        data["Designation 2"].fillna("Missing", inplace=True)
        data["Designation 3"].fillna("Missing", inplace=True)
        
        data["combined"] = data["Designation"].str.cat(data[["Designation", "Designation 2", "Designation 3"]].astype(str), sep="/")
        
        comb = (data.combined).str.split("/")
        
        founder = ["F","Founder","CF", "Co-founder", "President", "Director", "MD", "Founder & CEO"
           , "Owner", "cbo", "CEO & Cofounder",'Co-Founder & CTO', 'Co-Founder', 'Co-Founder & CPO'
           ,'Co-Founder & MD',  'Co-founder & CBO','CEO & Founder','CEO & Cofounder', 'Co-Founder', 'Co-founder', 'Sugandhi'
           ,'Co-Founder & CPO', 'Co-Founder & CEO', 'Co-Founder & CTO','CoFounder & CEO', 'Co-Founder & MD'
           , 'Co-founder & CTO','MD & CEO','Cofounder & COO', 'Cofounder', 'Founder & COO', 'Cofounder & CEO'
           , 'Cofouncder & CEO','Founder & MD','Cofounder & CTO','founder']

        vp = ["Associate VP","VP", 'SVP', 'Vice President', 'VP HOO','AVP ','VP HR', 'AVP-Technology','Excecutive Director'
             , 'City Head', 'Sr VP']

        ceo = ["CEO", "CTO", 'MD & CTO', 'Sr Pricipal Consultant',  'CMO','India Head & Chief Engg Officer','COO', 'CEO & Director']

        hr = ["HR"," VP HR", "Director-HR", 'Senior Director HR', 'Global Head-HR','Manager HR','Director HR'
              ,'HR Director','Tech HR', 'VP HR','Head HR','Director-TA', 'Director-TA']

        Head_engg = ['Head Engg',"HR & TA Head", 'Co-Founder & Data Center Automation Specialist', 'Head od Software Dev'
                    ,"Head od Software Dev", "TA", "Head TA", 'VP TA', 'Head IT', 'VP IT','Head of India Engg','GM IT'
                    , 'Director of Technology','VP of rtechnology', 'VP Tech','Director of Engg','GM IT','GM','TA Lead'
                    ,'VP Tech','Director of Technology','Global Head','Director Technology', 'Head of Tech','Director & Head Engg' 
                    , 'Head of Technology','Head Product Engg', 'Engg Manager', 'Principal Engg','Director Engg', 'Sr TA Manager']

        l = []
        for i in comb:
            if any(item in i for item in founder):
                l.append("Founder")
            elif any(item in i for item in vp):
                l.append("VP")
            elif any(item in i for item in ceo):
                l.append("CEO")
            elif any(item in i for item in hr):
                l.append("HR")
            elif all(item in i for item in ["Missing"]):
                l.append("Missing")
            elif any(item in i for item in Head_engg):
                l.append("Head_engg")
            else:
                l.append(i[0])
                            
        data["Desingations"] = l
        req_data = pd.get_dummies(data["Desingations"], drop_first=True)
        req_data['id'] = np.arange(0,len(req_data))
        
        data = data.merge(req_data)
        data.drop(columns=["Desingations","Designation","Designation 2","Designation 3", "combined"], inplace=True)
         
        return data

    def Filter_Contact_Status(self, data):
        cont_status = []
        negative = ['Not Interested']
        positive = ['Responded', 'Called','Call-Disqualified', 'Call-Qualified','postponed','Call-Yes']
        for i in data["Contact Status"]:
            if i in negative:
                cont_status.append('Negative')
            elif i in positive:
                cont_status.append("Positive")
            else:
                cont_status.append("Not_Responded")

        data["Contact_Status"] = cont_status
        data.drop(columns=["Contact Status"], inplace = True)
        
        return data


# In[3]:


filter_data = Data_Filteration()


# In[15]:


import pickle
pickle_out = open("Filtering_and_Preprocessing.pickle","wb")
pickle.dump(filter_data, pickle_out)
pickle_out.close()


# In[18]:


data = pd.ExcelFile('Data.xlsx')
df1 = pd.read_excel(data, 'Ashish')
df2 = pd.read_excel(data, 'Deepu')
df3 = pd.read_excel(data, "Rozer")
df4 = pd.read_excel(data, "Shubham")
df5 = pd.read_excel(data, "Chaetll")
data = pd.concat([df1, df2, df3, df4, df5])
data['id'] = np.arange(0,len(data))


# In[19]:


data[:6000].to_csv("Train.csv")
data[6000:].to_csv("Test.csv")


# In[6]:


data = filter_data.column_selection(data)
data = filter_data.Filter_Company_Type(data)
data = filter_data.Filter_Requirments(data)
data = filter_data.Filter_Location(data)
data = filter_data.Filter_Desingation(data)
data = filter_data.Filter_Contact_Status(data)


# In[14]:


data.to_csv('Final_data.csv')


# In[ ]:




