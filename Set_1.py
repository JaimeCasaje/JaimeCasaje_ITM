#!/usr/bin/env python
# coding: utf-8

# In[15]:


def savings(gross_pay, tax_rate, expenses):
    return(int(int(gross_pay)-((int(gross_pay)*float(tax_rate))+int(expenses))))

def material_waste(total_material, material_units, num_jobs, job_consumption):
    return(str(int(total_material)-(int(num_jobs)*int(job_consumption)))+str(material_units))

def interest(principal, rate, periods):
    return(int(int(principal)+(int(principal)*(float(rate)*int(periods)))))

