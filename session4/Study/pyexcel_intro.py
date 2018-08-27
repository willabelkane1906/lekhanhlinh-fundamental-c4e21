import pyexcel

# 1.prepare data
data = [
    {
        'name':'vito',
        'age' : 21,
    },
    {
        'name':'michel',
        'age' : 31,
    },
    {
        'name':'corle',
        'age' : 63,
    }
]
# 2.Save
pyexcel.save_as(records=data, dest_file_name="sample.xlsx")


