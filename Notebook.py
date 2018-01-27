
# coding: utf-8

# 

# In[ ]:

# 获得基本数据 
table=DataAPI.FdmtBSAllLatestGet(ticker=u"000001",secID=u"",reportType=u"",endDate=u"",beginDate=u"",year="",field=u"",pandas="1")
table


# In[ ]:

# 选择需要的行
#   指定 endDate, 或范围
t_table=table['2016-06-30'<table['endDate']]
tt_table=t_table['2017-08-01'>t_table['endDate']]
tt_table


# In[ ]:

#选择需要的列
table[['secID','endDate']]

#adasda
